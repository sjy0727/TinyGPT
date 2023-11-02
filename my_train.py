#!/usr/bin/env python
# -*- encoding : utf-8 -*-
"""
@Author :sunjunyi
@Time   :2023/8/29 11:35
"""
import torch
from torch.utils.data import DataLoader
from torch.optim import AdamW
from my_dataset import QuestionAnswerDataset
from model import GPT, GPTConfig

if __name__ == '__main__':
    dataset = QuestionAnswerDataset(
        '/Users/sunjunyi/PycharmProjects/TinyGPT/data/poetry/tang_poet.txt')  # ('/Users/sunjunyi/PycharmProjects/chinese-poetry/全唐诗/poet.song.1000.json')
    loader = DataLoader(
        dataset=dataset,
        batch_size=128,
        collate_fn=dataset.collate_fn
    )

    gpt_config = GPTConfig(
        block_size=1024,
        vocab_size=21184,  # 21184,  # GPT-2 vocab_size of 50257, padded up to nearest multiple of 64 for efficiency
        n_layer=4,
        n_head=4,
        n_embd=128,
        dropout=0.2,
        bias=True  # True: bias in Linears and LayerNorms, like GPT-2. False: a bit better and faster
    )

    device = torch.device('cpu')
    model = GPT(config=gpt_config).to(device)
    optimizer = AdamW(model.parameters(), lr=1e-3)

    epochs = 10
    for epoch in range(epochs):
        for input_ids, start_pos, end_pos in loader:
            input_ids, start_pos, end_pos = input_ids.to(device), start_pos.to(device), end_pos.to(device)
            optimizer.zero_grad()
            logits, loss = model(input_ids, targets=None, task='QA', start_positions=start_pos, end_positions=end_pos)
            loss.backward()
            optimizer.step()
            print(f'epoch:{epoch} loss:{loss.item()}')

        torch.save(model.state_dict(), 'my_ckpt.ckpt')
