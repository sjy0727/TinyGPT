#!/usr/bin/env python
# -*- encoding : utf-8 -*-
"""
┌─────────────────────────────────────────────────────────────┐
│┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐│
││Esc│!1 │@2 │#3 │$4 │%5 │^6 │&7 │*8 │(9 │)0 │_- │+= │|\ │`~ ││
│├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───┤│
││ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │{[ │}] │ BS  ││
│├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴─────┤│
││ Ctrl │ A │ S │ D │ F │ G │ H │ J │ K │ L │: ;│" '│ Enter  ││
│├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────┬───┤│
││ Shift  │ Z │ X │ C │ V │ B │ N │ M │< ,│> .│? /│Shift │Fn ││
│└─────┬──┴┬──┴──┬┴───┴───┴───┴───┴───┴──┬┴───┴┬──┴┬─────┴───┘│
│      │Fn │ Alt │         Space         │ Alt │Win│   HHKB   │
│      └───┴─────┴───────────────────────┴─────┴───┘          │
└─────────────────────────────────────────────────────────────┘

Reinforcemnet Learning from Human Feedback 终端版。

@Author :sunjunyi
@Time   :2023/8/29 12:11
"""

import os
import time
import random
from rich import box
from rich.table import Table
from rich.align import Align
from rich.console import Console

import torch
import torch.nn.functional as F

# from iTrainingLogger import iSummaryWriter

MODEL_CONFIG = {
    'model_name': 'uer/gpt2-chinese-cluecorpussmall',
    'device': 'cuda:0'
}
MIN_REWARD = -2.0
MAX_REWARD = 2.0

LOG_PATH = './logs'
LOG_NAME = 'Terminal-Human-Feedback'
# writer = iSummaryWriter(log_path=LOG_PATH, log_name=LOG_NAME)

prompts = [
    '刚收到货，感觉',
    '这部电影很',
    '说实话，真的很',
    '这次购物总的来说体验很'
]


def main():
    """
    主函数。
    """
    console = Console()
    table = Table(show_footer=False)
    table.width = console.width
    table.box = box.SQUARE
    table.row_styles = ["none", "dim"]
    console.clear()

    # add title
    table.title = (
        "[bold not italic]:robot:[/] Reinforcemnet Learning from Human Feedback - Terminal"
    )

    # add column (first line)
    table.add_column("config/key", no_wrap=True)
    table.add_column("config/value", no_wrap=True)

    # add config row to table
    for k, v in MODEL_CONFIG.items():
        table.add_row(k, v)
    table.add_row('log path', os.path.join(LOG_PATH, LOG_NAME))
    table.add_row('min ~ max reward', f'{MIN_REWARD} ~ {MAX_REWARD}')
    table.add_row('prompts', f'{prompts}')
    table.caption = "You can change config in [b not dim]Source Code[/]"

    table.columns[0].style = "bright_red"
    table.columns[0].header_style = "bold bright_red"
    table.columns[1].style = "bright_green"
    table.columns[1].header_style = "bold bright_green"
    table_centered = Align.center(table)
    console.print(table_centered)

    with console.status("[bold bright_green]Initializing Model & Env..."):
        # TODO:
        console.log('[bold magenta][Done] Initialized Model & Env.')

    step = 1
    t = time.time()
    while True:
        current_prompt = random.choice(prompts)
        console.print(f'[Step {step}]')
        console.print(f'[bright_yellow]prompt>>> {current_prompt}[/bright_yellow]')
        console.print('generating results...', end='\r')
        # query_tensor = tokenizer.encode(current_prompt, return_tensors="pt").to(MODEL_CONFIG['device'])
        # response_tensor = respond_to_batch(model, query_tensor)
        # response_txt = tokenizer.decode(response_tensor[0, :].to('cpu'))

        console.print(f'[bright_blue]result>>> response_txt[/bright_blue]')
        reward_txt = input(f'Reward ({MIN_REWARD} ~ {MAX_REWARD}): ')
        while True:
            try:
                reward_f = float(reward_txt)
                if MIN_REWARD <= reward_f <= MAX_REWARD:
                    break
                else:
                    reward_txt = input(f'Reward ({MIN_REWARD} ~ {MAX_REWARD}): ')
            except:
                reward_txt = input(f'Reward ({MIN_REWARD} ~ {MAX_REWARD}): ')
        # reward = [torch.tensor(reward_f).to(MODEL_CONFIG['device'])]

        with console.status("[bold bright_green]Updating Model..."):
            pass




if __name__ == '__main__':
    main()
