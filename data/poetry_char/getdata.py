#!/usr/bin/env python
# -*- encoding : utf-8 -*-
"""
@Author :sunjunyi
@Time   :2023/8/28 16:36
"""
# -*- coding: utf-8 -*-
"""
目标：获取数据集中全唐诗，并提取五言诗词，两句的数据
 示例：
{
        "author": "郭向",
        "paragraphs": [
            "抱玉三朝楚，懷書十上秦。",
            "年年洛陽陌，花鳥弄歸人。"
        ],
        "title": "途中口號",
        "id": "32898701-8d9c-4b4d-b192-510564f63b2f"
    },
"""
import glob
import json
import os

# TODO:修改路径
datas_json_path_list = glob.glob("/Users/sunjunyi/PycharmProjects/chinese-poetry/全唐诗/poet*.json")  # 1. 匹配所有唐诗json文件
# print(datas_json_path_list,"\n",len(datas_json_path_list))
if os.path.exists("tang_poet.txt"):
    os.remove("tang_poet.txt")
    print("已经删除原数据-tang_poet.txt")

print("总共处理文件个数：", len(datas_json_path_list))
print("预处理中，请稍后。。")

for data_json_path in datas_json_path_list:  # 2. 处理匹配的每一个文件
    with open(data_json_path, "r", encoding="utf-8") as f:
        ts_data = json.load(f)
        for each_ts in ts_data:  # 3. 处理文件中每段数据，只要五言诗和2句的
            paragraphs_list = each_ts["paragraphs"]
            # 只要两句的, 且是五言诗, 一句10字外加两个标点, 共12
            if len(paragraphs_list) == 2 and len(paragraphs_list[0]) == 12 and len(paragraphs_list[1]) == 12:
                with open("tang_poet.txt", "a", encoding="utf-8") as f2:
                    f2.write("".join(paragraphs_list))
                    f2.write("\n")
f = open("tang_poet.txt", "r", encoding="utf-8")
print(len(f.readlines()))
print("success")
