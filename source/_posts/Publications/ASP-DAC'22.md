---
date: 2022-01-12 00:00:12
# date: 2021-09-12 00:00:12
title: "An Energy-Efﬁcient Bit-Split-and-Combination Systolic Accelerator for NAS-Based Multi-Precision Convolution Neural Networks"
# cover: /images/Projects/A-Parallel-Optimization-Design-for-Demosaicing&RISC-V-CPU-on-FPGA/half-flow.svg
# thumbnail: /images/Projects/A-Parallel-Optimization-Design-for-Demosaicing&RISC-V-CPU-on-FPGA/dema.svg
toc: true
tags: [nas,mutli-precision,reconfigurable-computing,accelerator,fpga]
categories: [Conference,ASP-DAC]
authors: [L. Dai, Q. Cheng, Y. Wang, G. Huang, J. Zhou, K. Li, W. Mao, H. Yu]
whoami: J. Zhou
conference: Design Automation Conference in Asia and South Pacific Region (ASP-DAC)
timelineNoDate: true
materials: [[PAPER,https://ieeexplore.ieee.org/document/9712509],
            [SILDES,/Publications/ASP-DAC'22/#Sildes],
            [VIDEO,/Publications/ASP-DAC'22/#Video],
           ]
---
---

# Abstract

<p style='text-align: justify;'>
Optimized convolutional neural network (CNN) models and energy-efﬁcient hardware design are of great importance in edge-computing applications. The neural architecture search (NAS) methods are employed for CNN model optimization with multi-precision networks. To satisfy the computation requirements, multi-precision convolution accelerators are highly desired. The existing high-precision-split (HPS) designs reduce the additional logics for reconﬁguration while resulting in low throughput for low precisions. The low-precision-combination (LPC) designs improve the low-precision throughput with large hardware cost. In this work, a bit-split-and-combination (BSC) systolic accelerator is proposed to overcome the bottlenecks. Firstly, BSC-based multiply-accumulate (MAC) unit is designed to support multi-precision computation operations. Secondly, multi-precision systolic dataﬂow is developed with improved data-reuse and transmission efﬁciency. The proposed work is designed by Chisel and synthesized in 28-nm process. The BSC MAC unit achieves maximum 2.40× and 1.64× energy efﬁciency than HPS and LPC units, respectively. Compared with published accelerator designs Gemmini, Bit-fusion and Bit-serial, the proposed accelerator achieves up to 2.94× area efﬁciency and 6.38× energy-saving performance on the multi-precision VGG16, ResNet-18 and LeNet-5 benchmarks.
</p>
<!-- more -->

# Sildes
<iframe src="/pdf/pdfjs/web/viewer.html?file=/pdf/SILDES_ASPDAC2022.pdf" width="100%" height="500px"></iframe>

# Video
<video onloadstart="this.volume=0.2" src='/video/VIDEO_ASPDAC2022.mp4' type='video/mp4' controls='controls'  width='100%' height='100%'>
</video>