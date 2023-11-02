#!/usr/bin/env python
# -*- encoding : utf-8 -*-
"""
@Author :sunjunyi
@Time   :2023/8/29 11:40
"""
import json

import numpy as np
import torch
from torch.utils.data.dataset import Dataset
from transformers import BertTokenizerFast

from CustomTokenizer import qa_enc


class QuestionAnswerDataset(Dataset):
    def __init__(self, input_file_path):
        self.tokenizer = BertTokenizerFast.from_pretrained('bert-base-chinese')
        self.tokenizer.add_tokens(['[Q]', '[A]', '[END]'])
        self.input_file_path = input_file_path
        # self.tokenizer.convert_tokens_to_ids('[A]')
        if input_file_path.endswith('json'):
            with open(input_file_path, 'r') as f:
                self.dataset = json.load(f)
        elif input_file_path.endswith('txt'):
            with open(input_file_path, 'r') as f:
                self.dataset = f.readlines()

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        if self.input_file_path.endswith('json'):
            question = self.dataset[idx]['title']  # ["question"]
            answer = ''.join(self.dataset[idx]['paragraphs'])  # ["answer"]

            input_text = f"[Q] {question} [A] {answer} [END]"
        else:
            input_text = self.dataset[idx]
        return input_text

    def collate_fn(self, batch):
        # 设置最大长度和进行填充
        encoded_inputs = self.tokenizer.batch_encode_plus(
            batch,
            add_special_tokens=False,
            padding=True,
            truncation=True,
            # return_tensors='pt',
            max_length=1024
        )
        start_positions = list(map(lambda token: token.index(self.tokenizer.convert_tokens_to_ids('[A]')) + 1,
                                   encoded_inputs['input_ids']))
        end_positions = list(map(lambda token: token.index(self.tokenizer.convert_tokens_to_ids('[END]')) - 1,
                                 encoded_inputs['input_ids']))

        # print("填充后的编码结果：", encoded_inputs['input_ids'])
        # print(self.tokenizer.batch_decode(encoded_inputs['input_ids']))
        input_ids = torch.tensor(encoded_inputs['input_ids'])
        start_positions = torch.tensor(start_positions)
        end_positions = torch.tensor(end_positions)
        return input_ids, start_positions, end_positions
