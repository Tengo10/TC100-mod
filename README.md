# Teckin TC100 IP-CAMERA

## Overview

Internal Pictures can be found at: [FCC ID](https://fccid.io/2AQNX-TC100).

Nmap returns no open ports and no firmware downloads can be found on [Teckins](https://www.teckinhome.com/) website.

## Hardware

|||
|----|------|
|CPU |[ANYKA CPU AK3918](http://www.anyka.com/en/productInfo.aspx?id=113)|
|Architecture| ARM926EJ-S (armv5)|
|Kernel|Linux 3.4.35 armv5tejl|
|DRAM| 64 MiB|
|SPI flash| 16 MiB|
|WiFi|[RTL8188FTV](https://www.realtek.com/en/products/communications-network-ics/item/rtl8188ftv)

## Firmware

Firmware can be extracted using UBoot and a SD card.

### Binwalk output:

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

### IPCtool Output

```
chip:
  vendor: CLOUD39EV3_AK3918EV300_MNBD
  model: unknown
ethernet:
  mac: "34:20:03:a9:e2:bc"
rom:
  - type: nor
    block: 4K
    partitions:
      - name: spi0.0
        size: 0x800000
        sha1: cc3226cd
      - name: KERNEL
        size: 0x200000
        sha1: 6d267074
      - name: MAC
        sha1: ea3c6ba8
      - name: KERNEL
        size: 0x200000
        sha1: 6d267074
      - name: MAC
        size: 0x1000
        sha1: 65d77247
      - name: ENV
        size: 0x1000
        sha1: f599b558
      - name: A
        size: 0x180000
        path: /,squashfs
        sha1: afc0ddc2
      - name: B
        size: 0x7d000
        path: /etc/jffs2,jffs2,rw
      - name: C
        size: 0x3b6000
        path: /usr,squashfs
        sha1: 5c668a25
    size: 15M
ram:
  total: 64M
firmware:
  kernel: "3.4.35 (Wed Nov 25 07:07:55 UTC 2020)"
  toolchain: gcc version 4.8.5 (anyka (gcc-4.8.5 + binutils-2.24 + ulcibc-0.9.33.2)(20170223))
  libc: uClibc 0.9.33.2
  god-app: anyka_ipc
```

## Firmware Mods


### Firmware Backup

> The included Python script works quite well, __however for both a SD card is needed__

Manual way:

1. Connect a Serial to USB Converter to the JTAG port on the main PCB, Baud: 115200
2. Boot into U-Boot by pressing a button when prompted
3. Write flash contents to SD card:
    ```
    sf probe 0
    sf read 0x82000000 0x0 0x7EE000
    fatwrite mmc 0 0x82000000 firmware.bin 0x7EE000
    ```
4. Done! 
### Changing the Password

1. Connect a Serial to USB Converter to the JTAG port on the main PCB, Baud: 115200
2. Boot into U-Boot by pressing a button when prompted
3. Change environmental variables and reboot:

    ```
    env set bootargs console=ttySAK0,115200n8 root=/dev/mtdblock4 rootfstype=squashfs init=/bin/sh mem=64M memsize=64M
    env save
    reset
    ```

4. Init Linux and change password:

    ```
    ./etc/init.d/rcS
    passwd root
    ```
 
5. reboot the camera into U-Boot
6. Change environmental variables back and reboot:

    ```
    env set bootargs console=ttySAK0,115200n8 root=/dev/mtdblock4 rootfstype=squashfs init=/sbin/init mem=64M memsize=64M
    env save
    reset
    ```
7. Done!

### Updating Firmware Imagines

The whole firmware is split into 5 partitions. 

1. uboot.bin: contains the bootloader
2. uImage: contains the Linux Kernel
3. root.sqfs4: contains the linux root directory
4. usr.sqfs4: contains most of the Teckin binaries
5. usr.jffs2: contains only cloud service and sensor configs

U-Boot offers some simple to use tools. Just put files named as written above onto the SD card and run tfdown(jffs2fs/kernel/rootfs/squashfs/uboot/boot).

