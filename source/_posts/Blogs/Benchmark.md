---
date: 2021-05-15 00:40:12
title: "CPU Benchmark"
mathjax: false
toc: true
categories: [Benchmark]
---
***

<!-- more -->
## GeekBench
ARM:
    wget https://cdn.geekbench.com/Geekbench-5.4.0-LinuxARMPreview.tar.gz
AMD64:
    wget https://cdn.geekbench.com/Geekbench-5.4.0-Linux.tar.gz
    tar zxf Geekbench-5.4.0-Linux.tar.gz

| Device | CPU | info | frq | Single-Core Score | Multi-Core Score |
| :--    | :-: | :--: | :-: | :--: | :--: |
|  N/A  | Xeon W2295(es) | 18c36t | 4.5GHz | | |
| NanoPi NEO | Allwinner H3 | 4-core Cortex-A7 | 1.2GHz | 54 | 92 |
| Davinci-MINI | Atlas 200 DK  | 8-core ARMv8 |  | 159 | 578 |
| Khadas VIM3 | A311D  | 4-core Cortex-A73 & 2-core Cortex-A53 |  1.8G & 1.2G  | 347 | 1202 |
| Alibaba Cloud ECS | Xeon E5-2682 v4 | 1 Core |  2.49GHz  | 641 | 640 |
| N/A | G5500 | 2 Core |  3.80GHz  | 1014 | 1648 |
https://browser.geekbench.com/user/389197

## 计算圆周率

```shell
time echo "scale=5000; 4*a(1)" | bc -l -q
```
time是计时程序。scale是精度，4*a(1)  调用了反正切函数。 
由三角函数我们知道1的反正切是pi/4, pi=4* pi/4。 -l -q参数的意思请参照manpage。这一行其实就是让bc计算1的反正切，计算精度是5000位。
有的人用tcsh作为shell的需要注意指定time工具的位置，/usr/bin/time。tcsh内部有一个内部命令time，输出格式诡异。
source: 
Only Single Threading

| Device | CPU | Info | Frq | Time(5000) |
| :--    | :-: | :--: | :-: | :--: | 
|  N/A  | Xeon W2295(es) | 18c36t | 4.50 GHz | 15.956s | 
| NanoPi NEO | Allwinner H3 | 4-core Cortex-A7 | 1.2GHz | 118.814s |
| Davinci-MINI | Atlas 200 DK  | 8-core ARMv8 |  | 57.200s |
| Khadas VIM3 | A311D  | 4-core Cortex-A73 & 2-core Cortex-A53 |  1.8G & 1.2G  | 33.312s |
| Alibaba Cloud ECS | Xeon E5-2682 v4 | 1 Core |  2.49GHz  | 20.40s |
| N/A | G5500 | 2 Core |  3.80GHz  | 16.63s |
| Raspberry Pi 4B | BCM2835 | 4-core Cortex-A72 |  1.50 GHz  | 44.76s |
## sysbench
有待研究

https://github.com/akopytov/sysbench