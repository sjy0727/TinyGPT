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
    table = Table(show_footer=False, show_header=True, header_style="bold magenta")
    table.width = console.width
    table.box = box.SQUARE
    table.row_styles = ["none", "dim"]
    console.clear()

    # add title
    table.title = (
        "[bold not italic]:robot:[/] TinyGPT to generate poetry - Terminal"
    )

    # add column (first line)
    table.add_column("config/key", no_wrap=True, justify='center')
    table.add_column("config/value", no_wrap=True, justify='center')

    # add config row to table
    for k, v in MODEL_CONFIG.items():
        table.add_row(k, v)

    table.add_row('log path', os.path.join(LOG_PATH, LOG_NAME))
    table.add_row('min ~ max reward', f'{MIN_REWARD} ~ {MAX_REWARD}')
    table.add_row('prompts', f'{prompts}')

    # 添加table描述
    table.caption = "You can change config in [b not dim]Source Code[/]"

    # table第一列风格
    table.columns[0].style = "bright_red"
    table.columns[0].header_style = "bold bright_red"

    # table第二列风格
    table.columns[1].style = "bright_green"
    table.columns[1].header_style = "bold bright_green"

    table_centered = Align.center(table)
    console.print(table_centered)

    with console.status("[bold bright_green]Initializing Model & Env..."):
        # TODO:
        time.sleep(1)
        console.log('[bold magenta][Done] Initialized Model & Env.')

    step = 1
    t = time.time()
    while True:
        console.print(f'[ Step {step} ]')
        current_prompt = console.input(f'[bright_yellow]📖(Prompt) <<< [/bright_yellow]')

        if current_prompt == 'clear()':
            console.clear()
            console.print(table_centered)
            continue

        with console.status("[bold bright_green]Generating results..."):
            time.sleep(1)

        console.print(f'[bright_blue]💬(Response) >>> {current_prompt} [/bright_blue]')
        reward_txt = console.input(f'[bright_cyan]🏆(Reward) ({MIN_REWARD} ~ {MAX_REWARD}): [/bright_cyan]')

        with console.status("[bold bright_green]Updating Model..."):
            time.sleep(1)
            console.log('[bold magenta][Done] Updated Model.')
            step += 1


if __name__ == '__main__':
    main()
