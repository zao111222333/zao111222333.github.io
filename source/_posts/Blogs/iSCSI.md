---
date: 2021-11-04 00:00:12
title: "iSCSI"
mathjax: false
toc: true
categories: [Blogs, Homelab]
---
***

<!-- more -->
## IPMITOOL
https://www.server-world.info/en/note?os=Debian_11&p=iscsi&f=3

iscsiadm -m node -T iqn.2005-10.org.freenas.ctl:dockerhost -p 192.168.107.3 --op update -n node.startup -v automatic

vim /etc/fstab
/dev/sdb1 /Docker ext4 _netdev 0 0


在clash config文件的rule内容中，加入以下：
```
- DOMAIN-SUFFIX,junzhuo.site,🎯 全球直连
（或者）
- DOMAIN-SUFFIX,junzhuo.site,DIRECT
```
相当于对于*junzhuo.site,不会进行代理