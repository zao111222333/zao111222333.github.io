---
date: 2020-04-7 00:40:12
title: "Raspberry Pi wifi ssh frp"
mathjax: false
toc: true
categories: [Blogs]
---
***

<!-- more -->
## 下载镜像

[2021-03-04-raspios-buster-armhf.zip](http://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-03-25/2021-03-04-raspios-buster-armhf.zip)


## wifi自启动

```conf /boot/wpa_supplicant.conf
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="wifi-name"
    psk="wifi-passwd"
    key_mgmt=WPA-PSK
    priority=1
}
network={
    ssid="SUSTech-wifi"
    key_mgmt=NONE
    priority=2
}
```

```
ssid:网络的ssid
psk:密码
priority:连接优先级，数字越大优先级越高（不可以是负数）
scan_ssid:连接隐藏WiFi时需要指定该值为1
key_mgmt: list of accepted authenticated key management protocols  ---支持的协议列表  
WPA-PSK = WPA pre-shared key (this requires 'psk' field)     ---一般都是这个，这就包括了WPA、WPA2开始的那些方式  
WPA-EAP = WPA using EAP authentication    ---这个就是WEP开头的，猜的，求验证  
IEEE8021X = IEEE 802.1X using EAP authentication and (optionally) dynamically generated WEP keys  
NONE = WPA is not used; plaintext or static WEP could be used  ---这个是开放的，没密码，联通、电信之类的就这个  
WPA-PSK-SHA256 = Like WPA-PSK but using stronger SHA256-based algorithms  
WPA-EAP-SHA256 = Like WPA-EAP but using stronger SHA256-based algorithms  
If not set, this defaults to: WPA-PSK WPA-EAP ---如果未设置，默认支持WAP、WEP开头那些
```

## ssh

### ssh自启动
``` shell
touch /boot/ssh
```
### 找树莓派的ip
#### 方法一
通过比较树莓派开机前后ping通的ip地址的不同获取
``` shell command before RaspberryPi Connect to WiFi
ping_ip_1=$(arp -a)
```
RaspberryPi Power On & Connect to WiFi
``` shell command after RaspberryPi Connect to WiFi
ping_ip_2=$(arp -a) && diff <(echo "$ping_ip_1") <(echo "$ping_ip_2") && unset ping_ip_1 ping_ip_2
```
从不同的ip地址中找到树莓派的ip
#### 方法二
使用sent-ip
### ssh链接树莓派

``` shell
ssh pi@192.168.2.169
```
## frp

### frp
[frp-v0.34.2](https://github.com/fatedier/frp/releases/tag/v0.34.2)
树莓派版本：
[frp_0.34.2_linux_arm.tar.gz](https://github.com/fatedier/frp/releases/download/v0.34.2/frp_0.34.2_linux_arm.tar.gz)

解压到/etc/frp

### 修改frpc.ini文件

```
[common] 
server_addr = xx.xx.xx.xx 
server_port = 7000  
[ssh] 
type = tcp 
local_ip = 127.0.0.1 
local_port = 22 
remote_port = 6000  
[web1] 
type = http 
local_port = 5000 
remote_port = 5000 
custom_domains = xx.xx.xx.xx
```
### 自启动
把systemd文件夹下的frpc.service，放到/etc/systemd/system下

``` shell
ln -s /etc/frp/frpc /usr/bin/frpc
chmod +x /usr/bin/frpc
chmod 754 systemd/frpc.service
cp systemd/frpc.service /etc/systemd/system/
systemctl start frpc
systemctl enable frpc
systemctl status frpc
ps -ef|grep frpc
```

## 内网测速
```
iperf -c 192.168.1.2
```
```
iperf -s
```
## 设置开机串口启动

### 修改config.txt文件
最后加上三行
``` config.txt
dtoverlay=pi3-miniuart-bt
start_x=1
gpu_mem=128
```
### 修改cmdline.txt文件
删除rootwait之后的内容


wget https://dl.orbbec3d.com/dist/astra/v2.1.2/AstraSDK-v2.1.2-Linux-arm.zip
wget https://dl.orbbec3d.com/dist/openni2/OpenNI_2.3.0.66.zip

## watchdog
支持的是bcm2835_wdt。可以通过指令查询

``` shell
pi@raspberrypi:~ $ sudo cat /lib/modules/$(uname -r)/modules.builtin | grep wdt
kernel/drivers/watchdog/bcm2835_wdt.ko
pi@raspberrypi:~ $ sudo cat /var/log/kern.log* | grep watchdog
Jan 31 02:17:02 raspberrypi kernel: bcm2835-wdt bcm2835-wdt: Broadcom BCM2835 watchdog timer
```
### 安装生效步骤
#### 安装watchdog驱动
``` shell
pi@raspberrypi:~ $ sudo apt update
[... output ...]
pi@raspberrypi:~ $ sudo apt install watchdog
[... output ...]
pi@raspberrypi:~ $ sudo systemctl enable watchdog
[... output ...]
```
#### 修改配置
/boot/config.txt 在后面增加一配置项
``` /boot/config.txt
dtparam=watchdog=on
```
#### 修改配置文件
/etc/watchdog.conf 里面还有温度等配置可修改
``` shell
max-load-1 = 24
watchdog-device = /dev/watchdog
realtime = yes
priority = 1
```
#### 重启
测试是否有效，控制台中输入以下指令
（会导致死机）
``` shell
:(){ :|: & };:
```