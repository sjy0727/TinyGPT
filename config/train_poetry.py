#!/usr/bin/env python
# -*- encoding : utf-8 -*-
"""
@Author :sunjunyi
@Time   :2023/8/28 18:13
"""
# train a miniature character-level model
# good for debugging and playing on macbooks and such
# 网络模型输出文件夹
out_dir = 'out-poetry'
eval_interval = 250  # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10  # don't print too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False  # override via command line if you like
wandb_project = 'poetry'
wandb_run_name = 'mini-gpt'

# 数据文件夹名称
dataset = 'poetry'
gradient_accumulation_steps = 1
batch_size = 8
block_size = 256  # context of up to 256 previous characters

# baby GPT model :)
# GPT模型的大小
n_layer = 4
n_head = 4
n_embd = 64
dropout = 0.2

learning_rate = 1e-3  # with baby networks can afford to go a bit higher
max_iters = 5000
lr_decay_iters = 5000  # make equal to max_iters usually
min_lr = 1e-4  # learning_rate / 10 usually
beta2 = 0.99  # make a bit bigger because number of tokens per iter is small

warmup_iters = 100  # not super necessary potentially

# on macbook also add
device = 'mps'  # run on cpu only
compile = False  # do not torch compile the model
