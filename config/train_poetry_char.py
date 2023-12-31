#!/usr/bin/env python
# -*- encoding : utf-8 -*-
"""
@Author :sunjunyi
@Time   :2023/8/28 18:13
"""
# train a miniature character-level model
# good for debugging and playing on macbooks and such

out_dir = 'out-poetry-char'
eval_interval = 250  # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10  # don't print too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False  # override via command line if you like
wandb_project = 'poetry-char'
wandb_run_name = 'mini-gpt'

dataset = 'poetry_char'
gradient_accumulation_steps = 1
batch_size = 32
block_size = 256  # context of up to 256 previous characters
vocab_size = 21184  # bert-base-chinese词表中的字典大小 64倍向上取整

# baby GPT model :)
n_layer = 4
n_head = 4
n_embd = 128
dropout = 0.2

learning_rate = 1e-3  # with baby networks can afford to go a bit higher
max_iters = 5000
lr_decay_iters = 5000  # make equal to max_iters usually
min_lr = 1e-4  # learning_rate / 10 usually
beta2 = 0.99  # make a bit bigger because number of tokens per iter is small

warmup_iters = 100  # not super necessary potentially

# on macbook also add
device = 'cuda'  # run on cpu only
compile = False  # do not torch compile the model
