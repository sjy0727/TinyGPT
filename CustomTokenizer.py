#!/usr/bin/env python
# -*- encoding : utf-8 -*-
"""
@Author :sunjunyi
@Time   :2023/8/29 01:51
"""
import tiktoken

gpt2 = tiktoken.get_encoding("gpt2")

# In production, load the arguments directly instead of accessing private attributes
# See openai_public.py for examples of arguments for specific encodings
qa_enc = tiktoken.Encoding(
    # If you're changing the set of special tokens, make sure to use a different name
    # It should be clear from the name what behaviour to expect.
    name="my_tokenizer",
    pat_str=gpt2._pat_str,
    mergeable_ranks=gpt2._mergeable_ranks,
    special_tokens={
        **gpt2._special_tokens,
        "<|sepoftext|>": 50257,
        "<|padoftext|>": 50258,
    }
)
if __name__ == '__main__':
    print(qa_enc.encode('问题<|sepoftext|>答案<|endoftext|><|padoftext|>', allowed_special='all'))
    print(qa_enc.special_tokens_set)
