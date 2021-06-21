# Teckin TC100 IP-CAMERA

## Overview

Internal Pictures can be found at: [FCC ID](https://fccid.io/2AQNX-TC100).

Nmap returns no open ports and no firmware download can be found on [Teckins](https://www.teckinhome.com/) website.

## Hardware

|||
|----|------|
|CPU |[ANYKA CPU AK3918](http://www.anyka.com/en/productInfo.aspx?id=113)|
|Architecture| ARM926EJ-S (armv51)|
|DRAM| 64 MiB|
|SPI flash| 8 MiB|
|WiFi|[RTL8188FTV](https://www.realtek.com/en/products/communications-network-ics/item/rtl8188ftv)

## Firmware

Firmware can be extracted using UBoot and a SD card.

Binwalk output:

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
135548        0x2117C         CRC32 polynomial table, little endian
233472        0x39000         uImage header, header size: 64 bytes, header CRC: 0x3F7B7FAD, created: 2020-11-25 07:07:58, image size: 1420384 bytes, Data Address: 0x81B08000, Entry Point: 0x81B08040, data CRC: 0x5D155AF7, OS: Linux, CPU: ARM, image type: OS Kernel Image, compression type: none, image name: "Linux-3.4.35"
233536        0x39040         Linux kernel ARM boot executable zImage (little-endian)
247739        0x3C7BB         xz compressed data
247960        0x3C898         xz compressed data
2338816       0x23B000        Squashfs filesystem, little endian, version 4.0, compression:xz, size: 1204628 bytes, 337 inodes, blocksize: 131072 bytes, created: 2021-01-11 01:50:01
3911680       0x3BB000        JFFS2 filesystem, little endian
4010436       0x3D31C4        Unix path: /var/run/hostapd
4012332       0x3D392C        JFFS2 filesystem, little endian
4043316       0x3DB234        Unix path: /var/run/hostapd
4045476       0x3DBAA4        JFFS2 filesystem, little endian
4061628       0x3DF9BC        JFFS2 filesystem, little endian
4423680       0x438000        Squashfs filesystem, little endian, version 4.0, compression:xz, size: 3307414 bytes, 145 inodes, blocksize: 131072 bytes, created: 2021-01-11 01:50:01
8524156       0x82117C        CRC32 polynomial table, little endian
8622080       0x839000        uImage header, header size: 64 bytes, header CRC: 0x3F7B7FAD, created: 2020-11-25 07:07:58, image size: 1420384 bytes, Data Address: 0x81B08000, Entry Point: 0x81B08040, data CRC: 0x5D155AF7, OS: Linux, CPU: ARM, image type: OS Kernel Image, compression type: none, image name: "Linux-3.4.35"
8622144       0x839040        Linux kernel ARM boot executable zImage (little-endian)
8636347       0x83C7BB        xz compressed data
8636568       0x83C898        xz compressed data
10727424      0xA3B000        Squashfs filesystem, little endian, version 4.0, compression:xz, size: 1204628 bytes, 337 inodes, blocksize: 131072 bytes, created: 2021-01-11 01:50:01
12300288      0xBBB000        JFFS2 filesystem, little endian
12399044      0xBD31C4        Unix path: /var/run/hostapd
12400940      0xBD392C        JFFS2 filesystem, little endian
12431924      0xBDB234        Unix path: /var/run/hostapd
12434084      0xBDBAA4        JFFS2 filesystem, little endian
12450236      0xBDF9BC        JFFS2 filesystem, little endian
12812288      0xC38000        Squashfs filesystem, little endian, version 4.0, compression:xz, size: 3307414 bytes, 145 inodes, blocksize: 131072 bytes, created: 2021-01-11 01:50:01
```
