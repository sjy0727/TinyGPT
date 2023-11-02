import os
import random

import numpy as np
import pandas as pd
import streamlit as st
import cv2

st.set_page_config(
    page_title="Video Annotation Tool",
    page_icon='📌',
    layout="wide"
)

######################### 页面定义区（侧边栏） ########################
st.sidebar.title('📌 Video Facial Emotion 标注平台')
st.sidebar.markdown('''
    ```python
    用于视频中面部情绪的标注。
    ```
''')
st.sidebar.markdown('标注思路参考自 [InstructGPT](https://arxiv.org/pdf/2203.02155.pdf) 。')
st.sidebar.markdown('RLHF 更多介绍：[想训练ChatGPT？得...](https://zhuanlan.zhihu.com/p/595579042)')
st.sidebar.header('⚙️ Model Config')
st.sidebar.write('当前标注配置（可在源码中修改）：')

# label_tab, dataset_tab = st.tabs(['Label', 'Dataset'])

# with label_tab:
#     with st.expander('🔍 Setting Prompts', expanded=True):
#         random_button = st.button('随机 prompt', help='从prompt池中随机选择一个prompt，可通过修改源码中 MODEL_CONFIG["random_prompts"] 参数来自定义prompt池。')
#         if random_button:
#             prompt_text = random.choice(MODEL_CONFIG['random_prompts'])
#         else:
#             prompt_text = st.session_state['current_prompt']


# 加载视频
uploaded_file = st.file_uploader("上传视频文件", type=["mp4"])

if uploaded_file is not None:
    video = cv2.VideoCapture(os.path.join('/Users/sunjunyi/Downloads',uploaded_file.name))
    frame_rate = int(video.get(cv2.CAP_PROP_FPS))

    frame_number = st.number_input("帧编号", value=0, min_value=0, max_value=int(video.get(cv2.CAP_PROP_FRAME_COUNT)))
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    ret, frame = video.read()
    if ret:
        st.image(frame, channels="BGR", use_column_width=True)

    emotion_options = ["喜悦", "愤怒", "悲伤", "害怕", "惊讶", "中性"]
    selected_emotion = st.selectbox("选择情绪", emotion_options)

    arousal_rating = st.slider("唤醒评分", min_value=1, max_value=10, value=5)

    st.write(f"当前帧标签: 情绪 - {selected_emotion}, 唤醒评分 - {arousal_rating}")

    st.write(f"当前标记进度: {frame_number}/{int(video.get(cv2.CAP_PROP_FRAME_COUNT))}")
else:
    st.write("请上传视频文件")
