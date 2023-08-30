#!/usr/bin/env python
# -*- encoding : utf-8 -*-
"""
@Author :sunjunyi
@Time   :2023/8/29 11:40
"""
import numpy as np
import torch
from torch.utils.data.dataset import Dataset
from CustomTokenizer import qa_enc


# qa_enc.__setattr__('sep_token', '<|sepoftext|>')


class QuestionAnswerDataset(Dataset):
    def __init__(self, tokenizer,input_file_path):

        with open(input_file_path, 'r') as f:
            self.dataset = f.readlines()

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        question = self.dataset[idx]["question"]
        answer = self.dataset[idx]["answer"]

        input_text = f"[Q] {question} [A] {answer}"
        target_text = answer + " [END]"
        input_ids = self.tokenizer.encode(input_text, add_special_tokens=True)
        target_ids = self.tokenizer.encode(target_text, add_special_tokens=True)

    def collate_fn(self, batch):
        # 设置最大长度和进行填充
        encoded_inputs = self.tokenizer.batch_encode_plus(batch, add_special_tokens=True, padding=True,
                                                          truncation=True, return_tensors='np',
                                                          max_length=10)

        print("填充后的编码结果：", encoded_inputs['input_ids'])
        print(self.tokenizer.batch_decode(encoded_inputs['input_ids']))

        start_pos = token.index(tokenizer.convert_tokens_to_ids('[A]')) + 1
        end_pos = token.index(tokenizer.convert_tokens_to_ids('[END]')) - 1


if __name__ == '__main__':
    # print(qa_enc._special_tokens[
    #           '<|endoftext|>'])  # {'<|endoftext|>': 50256, '<|sepoftext|>': 50257, '<|padoftext|>': 50258}
    from transformers import BertTokenizerFast, GPT2TokenizerFast

    tokenizer = BertTokenizerFast.from_pretrained('bert-base-chinese')
    # tokenizer.add_special_tokens({'sep_token': '[STOP]'})
    # tokenizer.get_special_tokens_mask()
    # tokenizer.add_tokens()
    num_added_toks = tokenizer.add_tokens(['[Q]', '[A]', '[END]'])
    print("We have added", num_added_toks, "tokens")
    special_ids = tokenizer.convert_tokens_to_ids(['[Q]', '[A]', '[END]'])
    print("特殊标记对应的 id：", special_ids)

    print(tokenizer.all_special_tokens)

    token = tokenizer.encode(['[Q]你是谁[A]我是李白[END]', 'a'], add_special_tokens=False, padding=True)
    start_pos = token.index(tokenizer.convert_tokens_to_ids('[A]')) + 1
    end_pos = token.index(tokenizer.convert_tokens_to_ids('[END]')) - 1
    print('start:', start_pos, 'end:', end_pos)
    print(token)
    print(tokenizer.decode(token))
    print(tokenizer.all_special_tokens)
