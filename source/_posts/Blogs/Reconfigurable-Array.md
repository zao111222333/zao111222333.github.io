---
date: 2022-02-02 00:40:12
title: "Reconfigurable Array"
mathjax: false
toc: true
# tags: [technology,cleanroom,sustech]
# cover: /images/Blogs/Photolithography/Wafer.jpg
# categories: [Technology]
---

***
<!-- more -->
## PE: Multi-Precision FP Vector



| Data Type | Input Shape | Output Shape |
| :-------: | :---------: | :----------: |
|   INT8    |    4×32     |     4×1      |
|   BF16    |    4×16     |     4×1      |
|   FP16    |    4×16     |     4×1      |
|   FP32    |     2×8     |     2×1      |
|   TF32    |     2×8     |     2×1      |
|   FP64    |     1×4     |     1×1      |
<div align="center">
<img src="/images/Blogs/Reconfigurable-Array/image-20220202095944928.png" alt="Fig1. PE Structure with its Pipeline" style="zoom: 25%;" />

<img src="/images/Blogs/Reconfigurable-Array/image-20220202100249604.png" alt="Fig2. Multi-Presicion ISA" style="zoom: 50%;" />

<img src="/images/Blogs/Reconfigurable-Array/image-20220202100013999.png" alt="Fig3. PE IO Definition" style="zoom: 25%;" />
</div>

***

## Array: Reconfigurable Vector Systolic Array

<div align="center">
<img src="/images/Blogs/Reconfigurable-Array/image-20220202101602785.png" alt="Fig4. Vecotr Array Architecture" style="zoom:50%;" />
</div>

| Data Type |   Input Matrix    | Output Matrix | clk  |     Tips     |
| :-------: | :---------------: | :-----------: | :--: | :----------: |
|   INT8    | [16×32] * [32×16] |    [16×16]    |  16  | INT32 output |
|   BF16    | [16×16] * [16×16] |    [16×16]    |  16  |              |
|   FP16    | [16×16] * [16×16] |    [16×16]    |  16  |              |
|   FP32    |   [8×8] * [8×8]   |     [8×8]     |  8   |              |
|   TF32    |   [8×8] * [8×8]   |     [8×8]     |  8   |              |
|   FP64    |   [4×4] * [4×4]   |     [4×4]     |  4   |              |

<div align="center">
<img src="/images/Blogs/Reconfigurable-Array/Reconfigurable-Array.png" alt="Fig5. Configurable Vecotr Array Architecture" style="zoom:50%;" />
</div>

***

## Why Systolic?

+ Data-reuse, reducing Fanin Fanout.
+ Data-stationary, reducing toggle rate.

## Why Vector?

+ Vector, 规模效益/紧耦合可以最大限度的提高能效
+ Multi-precision本身就是vetor的, 实现高精度DataType的运算意味着可以实现更多的低精度运输

## Why Pipeline?

+ Reduce critical path, 减少信号毛刺/静态功耗, Energy Efficiency/Throughput
+ 对齐不同组建/不同模式下的critical path

***



## 进度&展望

+ PE部分正在重构, Array已经完成
+ Next Step: 评估和优化, 若效果理想, 会进行下一步的系统实现

