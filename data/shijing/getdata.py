# !/usr/bin/env python
# -*- encoding : utf-8 -*-
"""
@Author :sunjunyi
@Time   :2023/8/28 16:36
"""
# -*- coding: utf-8 -*-
"""
目标：获取数据集中诗经的数据
 示例：
  {
    "title": "关雎",
    "chapter": "国风",
    "section": "周南",
    "content": [
      "关关雎鸠，在河之洲。窈窕淑女，君子好逑。",
      "参差荇菜，左右流之。窈窕淑女，寤寐求之。",
      "求之不得，寤寐思服。悠哉悠哉，辗转反侧。",
      "参差荇菜，左右采之。窈窕淑女，琴瑟友之。",
      "参差荇菜，左右芼之。窈窕淑女，钟鼓乐之。"
    ]
  }
"""
import glob
import json
import os

# TODO:修改路径
datas_json_path_list = glob.glob("/Users/sunjunyi/PycharmProjects/chinese-poetry/诗经/*.json")  # 1. 匹配所有诗经json文件
file_name = 'shijing.txt'
# print(datas_json_path_list,"\n",len(datas_json_path_list))
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"已经删除原数据-{file_name}")

print("总共处理文件个数：", len(datas_json_path_list))
print("预处理中，请稍后。。")

for data_json_path in datas_json_path_list:  # 2. 处理匹配的每一个文件
    with open(data_json_path, "r", encoding="utf-8") as f:
        ts_data = json.load(f)
        for each_ts in ts_data:  # 3. 处理文件中每段数据，只要五言诗和2句的
            paragraphs_list = each_ts["content"]
            title = each_ts['title']
            # 只要两句的, 且是五言诗, 一句10字外加两个标点, 共12
            # if len(paragraphs_list) == 2 and len(paragraphs_list[0]) == 12 and len(paragraphs_list[1]) == 12:
            with open(file_name, "a", encoding="utf-8") as f2:
                f2.write('[Q]' + title + '[A]' + "".join(paragraphs_list) + '[END]')
                f2.write("\n")
f = open(file_name, "r", encoding="utf-8")
print(len(f.readlines()))
print("success")