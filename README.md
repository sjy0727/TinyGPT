# TinyGPT
 
## 开始训练

* https://zhuanlan.zhihu.com/p/601044938
* https://blog.yanjingang.com/?p=7102#41

```bash
$ python train.py \
       --dataset=poetry_char \
       --n_layer=4 \
       --n_head=4 \
       --n_embd=64 \
       --eval_iters=1 \
       --block_size=64 \
       --batch_size=8 \
       --max_iters=10000
```

部分参数说明：

* out_dir: checkpoints 保存路径，默认为 "out"
* dataset: 数据集
* n_layer: 神经网络的层数
* n_head: 注意力头的数量
* n_embd: 词向量、位置向量以及内部特征向量的维数
* eval_iters: 评估迭代次数
* block_size: 块大小
* batch_size: 批大小
* max_iters: 训练迭代次数
* device: 默认为 "cuda"，若在 CPU 上运行则需设置为 "cpu"
* compile: 使用 PyTorch2.0 中的 torch.compile() 加速模型训练，默认为 "True"，若在 PyTorch < 2.0 环境中运行，则需设置为 "
  False"

```bash
$ python train.py config/train_poetry.py
```

## 推理

```bash
$ python sample.py  --num_samples=1 --out_dir=out-poetry --device=mps
```