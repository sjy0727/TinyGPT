#!/usr/bin/env python
# -*- encoding : utf-8 -*-
"""
@Author :sunjunyi
@Time   :2023/8/29 11:40
"""
import torch
from torch.utils.data.dataset import Dataset
from CustomTokenizer import qa_enc


# qa_enc.__setattr__('sep_token', '<|sepoftext|>')


class QuestionAnswerDataset(Dataset):
    def __init__(self, input_file_path):
        with open(input_file_path, 'r') as f:
            self.data = f.readlines()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.data[idx]
        return text,

    def collate_fn(self, batch):
        texts = batch
        input_ids = torch.tensor(list(map(lambda s: qa_enc.encode(s, allowed_special='all'))))
        start_pos =


if __name__ == '__main__':
    print(qa_enc._special_tokens['<|endoftext|>'])  # {'<|endoftext|>': 50256, '<|sepoftext|>': 50257, '<|padoftext|>': 50258}
