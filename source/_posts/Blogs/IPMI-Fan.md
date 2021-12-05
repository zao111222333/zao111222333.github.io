---
date: 2021-11-04 00:00:12
title: "IPMI-Fan"
mathjax: false
toc: true
categories: [Homelab]
---
***

<!-- more -->
## IPMITOOL
https://www.licc.tech/article?id=33

``` shell
MyIP=192.168.2.229
MyUSER=ADMIN
MyPASSWD=ADMIN
#Set Full Speed Mode to Avoid Auto-Reset Speed
ipmitool -H ${MyIP} -U ${MyUSER} -P ${MyPASSWD} raw 0x30 0x45 0x01 0x01
#Set Fan Speed for FAN1, FAN2, ...
ipmitool -H ${MyIP} -U ${MyUSER} -P ${MyPASSWD} raw 0x30 0x70 0x66 0x01 0x00 0x30
#Set Fan Speed for FANA, FANB, ...
ipmitool -H ${MyIP} -U ${MyUSER} -P ${MyPASSWD} raw 0x30 0x70 0x66 0x01 0x01 0x30

# Set Power-On
ipmitool -H ${MyIP} -U ${MyUSER} -P ${MyPASSWD} chassis power on
```