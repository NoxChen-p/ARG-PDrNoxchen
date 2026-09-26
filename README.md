# ARG-PDrNoxchen 解码工具 / ARG-PDrNoxchen Decoder Tool

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Author](https://img.shields.io/badge/Author-Noxchen-orange.svg)](https://me.noxchen.dpdns.org)

---

## 项目介绍 / Project Introduction

**中文：**
基于 Python + Tkinter 开发的 ARG 解谜 GUI 解码工具，内置 30 种 ARG 常用编码解码器，只使用 Python 标准库，不需要额外 pip 安装包。

**English:**
A GUI decoding tool for ARG puzzle solving, built with Python + Tkinter. It includes 30 common ARG encoders/decoders, uses only the Python standard library, and requires no additional pip packages.

---

## 功能特性 / Features

1. 内置 30 种解码器 / Built-in 30 decoders
2. 两种模式：手动选择解码器 / 自动批量检测全部解码器并输出结果
   Two modes: manually select a decoder / automatically batch-detect all decoders and output results
3. 图形界面，粘贴文本一键解码 / Graphical interface, paste text and decode with one click
4. 纯标准库，打包 EXE 不需要额外依赖 / Pure standard library, no extra dependencies when packaging as EXE
5. 面向 ARG 解谜、密码挑战 / Designed for ARG puzzles and cipher challenges

---

## 30 个解码器清单 / List of 30 Decoders

| # | 解码器 / Decoder | 说明 / Description |
|---|---|---|
| 1 | Base64 | Base64 解码 / Base64 decoding |
| 2 | Base32 | Base32 解码 / Base32 decoding |
| 3 | Base16(Hex) | Base16 十六进制解码 / Base16 hex decoding |
| 4 | Base85 | Base85 解码 / Base85 decoding |
| 5 | Base64URL | Base64URL 解码 / Base64URL decoding |
| 6 | ROT13 | ROT13 字母移位 / ROT13 letter rotation |
| 7 | ROT5 | ROT5 数字移位 / ROT5 digit rotation |
| 8 | ROT18 | ROT18 组合移位 / ROT18 combined rotation |
| 9 | ROT47 | ROT47 ASCII 移位 / ROT47 ASCII rotation |
| 10 | 凯撒密码(移位3) / Caesar Cipher (Shift 3) | 固定移位 3 / Fixed shift 3 |
| 11 | 凯撒暴力破解(全部移位) / Caesar Brute Force (All Shifts) | 尝试所有移位 / Try all shifts |
| 12 | Atbash字母埃特巴什 / Atbash Letters | 字母反向映射 / Letter reverse mapping |
| 13 | Atbash数字埃特巴什 / Atbash Digits | 数字反向映射 / Digit reverse mapping |
| 14 | 维吉尼亚密码(key=key) / Vigenère Cipher (key=key) | 默认密钥 key / Default key `key` |
| 15 | 栅栏密码2栏 / Rail Fence Cipher (2 Rails) | 2 栏栅栏解密 / 2-rail rail fence decryption |
| 16 | 摩尔斯Morse / Morse Code | 摩尔斯电码解码 / Morse code decoding |
| 17 | URL解码 / URL Decode | URL 百分号解码 / URL percent decoding |
| 18 | 十六进制文本 / Hex Text | 十六进制转文本 / Hex to text |
| 19 | 二进制文本 / Binary Text | 二进制转文本 / Binary to text |
| 20 | 反转二进制 / Reverse Binary | 二进制位反转 / Reverse binary bits |
| 21 | 八进制文本 / Octal Text | 八进制转文本 / Octal to text |
| 22 | 文本反转(Reverse) / Text Reverse | 字符串反转 / Reverse string |
| 23 | 手机九宫格电话键盘 / Phone Keypad (T9) | 九宫格电话键盘解码 / Phone keypad decoding |
| 24 | 培根密码Bacon / Bacon Cipher | 培根密码解码 / Bacon cipher decoding |
| 25 | ASCII数字转字符 / ASCII Numbers to Characters | ASCII 码转字符 / ASCII code to characters |
| 26 | 字符转ASCII数字 / Characters to ASCII Numbers | 字符转 ASCII 码 / Characters to ASCII codes |
| 27 | 空白密码(空格/Tab) / Whitespace Cipher (Space/Tab) | 空格与 Tab 编码 / Space and Tab encoding |
| 28 | \x转义十六进制 / \x Escaped Hex | `\x` 转义十六进制解码 / `\x` escaped hex decoding |
| 29 | 博多码Baudot / Baudot Code | 博多码解码 / Baudot code decoding |
| 30 | 移除所有空格 / Remove All Spaces | 删除全部空格 / Remove all spaces |

---

## 运行方式 / How to Run

### 方式1：源码运行 / Option 1: Run from Source

**中文：**
需要 Python 3.8+，仅依赖自带 tkinter。

```bash
python main.py
```

English:
Requires Python 3.8+, only uses the built-in tkinter.

```bash
python main.py
```

方式2：EXE 版本 / Option 2: EXE Version

中文：
没有 Python 环境的用户，去项目 Releases 发布页左侧下载 Windows EXE，直接打开，不用配置环境。

English:
Users without a Python environment can download the Windows EXE from the Releases page on the left side of the project, open it directly, and do not need to configure the environment.

---

文档支持 / Documentation Support

---

开源协议 / License

MIT License，保留原作者信息。
MIT License, retain the original author information.

---

作者 / Author

· 作者 / Author: Noxchen
· 作者官网 / Author Website: me.noxchen.dpdns.org

---

免责声明 / Disclaimer

中文：
本工具仅用于学习、ARG 解谜娱乐，禁止非法使用。

English:
This tool is intended only for learning and ARG puzzle entertainment. Illegal use is prohibited.

官方网站/web：https://argpdr-3eph2g0.maozi.io/