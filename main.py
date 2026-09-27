import tkinter as tk
from tkinter import ttk, scrolledtext
import base64
import string
import urllib.parse

# ===================== 30种ARG常用解码函数 =====================
def decode_base64(s):
    try:
        return base64.b64decode(s.strip()).decode('utf-8','ignore')
    except:
        return "解码失败"

def decode_base32(s):
    try:
        return base64.b32decode(s.strip()).decode('utf-8','ignore')
    except:
        return "解码失败"

def decode_base16(s):
    try:
        return base64.b16decode(s.strip().upper()).decode('utf-8','ignore')
    except:
        return "解码失败"

def decode_base85(s):
    try:
        return base64.b85decode(s.strip()).decode('utf-8','ignore')
    except:
        return "解码失败"

def decode_rot13(s):
    trans = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                          "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    return s.translate(trans)

def decode_caesar_shift3(s):
    res = []
    for c in s:
        if c.isupper():
            res.append(chr((ord(c)-ord('A')-3)%26+ord('A')))
        elif c.islower():
            res.append(chr((ord(c)-ord('a')-3)%26+ord('a')))
        else:
            res.append(c)
    return "".join(res)

def decode_atbash(s):
    upper = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[::-1])
    lower = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1])
    res = []
    for c in s:
        if c.isupper():
            res.append(c.translate(upper))
        elif c.islower():
            res.append(c.translate(lower))
        else:
            res.append(c)
    return "".join(res)

def decode_url(s):
    try:
        return urllib.parse.unquote(s.strip())
    except:
        return "解码失败"

def decode_hex_text(s):
    try:
        clean = s.strip().replace(" ","")
        return bytes.fromhex(clean).decode("utf-8","ignore")
    except:
        return "解码失败"

def decode_binary_text(s):
    try:
        clean = s.strip().replace(" ","")
        data = int(clean,2)
        return data.to_bytes((data.bit_length()+7)//8,byteorder='big').decode("utf-8","ignore")
    except:
        return "解码失败"

def decode_octal_text(s):
    try:
        clean = s.strip().replace(" ","")
        data = int(clean,8)
        return data.to_bytes((data.bit_length()+7)//8,byteorder='big').decode("utf-8","ignore")
    except:
        return "解码失败"

def decode_rot5(s):
    trans = str.maketrans("0123456789","5678901234")
    return s.translate(trans)

def decode_rot18(s):
    t1 = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz","NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    t2 = str.maketrans("0123456789","5678901234")
    return s.translate(t1).translate(t2)

def decode_rot47(s):
    trans = str.maketrans(r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""",
                          r"""{|}~!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz""")
    return s.translate(trans)

def decode_vigenere(s, key="key"):
    text = s.strip()
    res = []
    key_idx = 0
    for c in text:
        if c.isupper():
            shift = ord(key[key_idx%len(key)].upper()) - ord('A')
            res.append(chr((ord(c)-ord('A')-shift)%26+ord('A')))
            key_idx +=1
        elif c.islower():
            shift = ord(key[key_idx%len(key)].lower()) - ord('a')
            res.append(chr((ord(c)-ord('a')-shift)%26+ord('a')))
            key_idx +=1
        else:
            res.append(c)
    return "".join(res)

def decode_railfence2(s):
    # 栅栏密码 2栏
    text = s.strip()
    n = len(text)
    mid = (n+1)//2
    return ''.join([text[i] for i in range(0,mid)] + [text[i] for i in range(mid,n)])

def decode_morse(s):
    morse_dict = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','/':' '}
    try:
        words = s.strip().split(" / ")
        out = ""
        for w in words:
            chars = w.split()
            for c in chars:
                out += morse_dict.get(c,"?")
            out += " "
        return out.strip()
    except:
        return "解码失败"

def decode_reverse(s):
    return s.strip()[::-1]

def decode_phonepad(s):
    # 老式手机九宫格
    d = {'2':'A','22':'B','222':'C','3':'D','33':'E','333':'F','4':'G','44':'H','444':'I','5':'J','55':'K','555':'L','6':'M','66':'N','666':'O','7':'P','77':'Q','777':'R','7777':'S','8':'T','88':'U','888':'V','9':'W','99':'X','999':'Y','9999':'Z'}
    try:
        text = s.strip().replace(" ","")
        res = ""
        i=0
        while i<len(text):
            if text[i] in "23456789":
                j=i
                while j<len(text) and text[j]==text[i] and j-i<4:
                    j+=1
                res += d.get(text[i:j],"?")
                i=j
            else:
                res+=text[i]
                i+=1
        return res
    except:
        return "解码失败"

def decode_bacon(s):
    # 培根密码 a=0,b=1
    text = s.strip().lower().replace(" ","")
    mapping = {'aaaaa':'A','aaaab':'B','aaaba':'C','aaabb':'D','aabaa':'E','aabab':'F','aabba':'G','aabbb':'H','abaaa':'I','abaab':'J','ababa':'K','ababb':'L','abb aa':'M','abbab':'N','abbba':'O','abbbb':'P','baaaa':'Q','baaab':'R','baaba':'S','baabb':'T','babaa':'U','babab':'V','babba':'W','babbb':'X','bbaaa':'Y','bbaab':'Z'}
    try:
        res=""
        for i in range(0,len(text),5):
            seg = text[i:i+5]
            res += mapping.get(seg,"?")
        return res
    except:
        return "解码失败"

def decode_ord_chr(s):
    # 数字转字符，空格分隔数字
    try:
        nums = list(map(int, s.strip().split()))
        return ''.join([chr(x) for x in nums])
    except:
        return "解码失败"

def decode_chr_ord(s):
    # 字符转ASCII数字
    return " ".join([str(ord(c)) for c in s.strip()])

def decode_whitespace(s):
    # 空白字符简易解码（空格=0，tab=1）
    txt = s
    binstr = ""
    for c in txt:
        if c == " ":
            binstr += "0"
        elif c == "\t":
            binstr += "1"
    try:
        data = int(binstr,2)
        return data.to_bytes((data.bit_length()+7)//8,"big").decode("utf-8","ignore")
    except:
        return "解码失败"

def decode_base64url(s):
    try:
        data = base64.urlsafe_b64decode(s.strip() + '===')
        return data.decode("utf-8","ignore")
    except:
        return "解码失败"

def decode_hex_escape(s):
    # \x61 这种转义
    import codecs
    try:
        return codecs.decode(s.strip(), 'unicode_escape')
    except:
        return "解码失败"

def decode_baudot(s):
    baud_map = {"00000":"","00001":"T","00010":"CR","00011":"O","00100":"SP","00101":"H","00110":"N","00111":"M","01000":"LF","01001":"L","01010":"R","01011":"G","01100":"I","01101":"P","01110":"C","01111":"V","10000":"E","10001":"Z","10010":"D","10011":"B","10100":"S","10101":"Y","10110":"F","10111":"X","11000":"A","11001":"W","11010":"J","11011":"FIGS","11100":"U","11101":"Q","11110":"K","11111":"LTRS"}
    try:
        parts = s.strip().split()
        out = "".join([baud_map.get(p,"?") for p in parts])
        return out
    except:
        return "解码失败"

def decode_binary_reverse(s):
    try:
        clean = s.strip().replace(" ","")[::-1]
        data = int(clean,2)
        return data.to_bytes((data.bit_length()+7)//8,byteorder='big').decode("utf-8","ignore")
    except:
        return "解码失败"

def decode_caesar_brute_all(s):
    out = "凯撒暴力破解全部移位:\n"
    for shift in range(1,26):
        res = []
        for c in s:
            if c.isupper():
                res.append(chr((ord(c)-ord('A')-shift)%26+ord('A')))
            elif c.islower():
                res.append(chr((ord(c)-ord('a')-shift)%26+ord('a')))
            else:
                res.append(c)
        out += f"移位{shift:2d}: {''.join(res)}\n"
    return out

def decode_skip_space(s):
    return s.strip().replace(" ","")

def decode_atbash_num(s):
    # 数字埃特巴什 0<->9,1<->8...
    trans = str.maketrans("0123456789","9876543210")
    return s.translate(trans)

# ===================== 解码器字典 共30个 =====================
decoders = {
    "Base64": decode_base64,
    "Base32": decode_base32,
    "Base16(Hex)": decode_base16,
    "Base85": decode_base85,
    "Base64URL": decode_base64url,
    "ROT13": decode_rot13,
    "ROT5": decode_rot5,
    "ROT18": decode_rot18,
    "ROT47": decode_rot47,
    "凯撒密码(移位3)": decode_caesar_shift3,
    "凯撒暴力破解(全部移位)": decode_caesar_brute_all,
    "Atbash字母埃特巴什": decode_atbash,
    "Atbash数字埃特巴什": decode_atbash_num,
    "维吉尼亚密码(key=key)": decode_vigenere,
    "栅栏密码2栏": decode_railfence2,
    "摩尔斯Morse": decode_morse,
    "URL解码": decode_url,
    "十六进制文本": decode_hex_text,
    "二进制文本": decode_binary_text,
    "反转二进制": decode_binary_reverse,
    "八进制文本": decode_octal_text,
    "文本反转(Reverse)": decode_reverse,
    "手机九宫格电话键盘": decode_phonepad,
    "培根密码Bacon": decode_bacon,
    "ASCII数字转字符": decode_ord_chr,
    "字符转ASCII数字": decode_chr_ord,
    "空白密码(空格/Tab)": decode_whitespace,
    "\\x转义十六进制": decode_hex_escape,
    "博多码Baudot": decode_baudot,
    "移除所有空格": decode_skip_space
}

def auto_detect_decode(input_text):
    """自动遍历全部解码器，输出所有成功结果"""
    result_out = "===== 自动检测结果 =====\n"
    found = False
    for name,func in decoders.items():
        res = func(input_text)
        if res != "解码失败" and res != input_text and len(res.strip())>0:
            result_out += f"【{name}】 → {res}\n"
            found = True
    if not found:
        result_out += "未找到可解码结果"
    return result_out

def run_decode():
    inp = input_box.get("1.0",tk.END)
    selected = combo.get()
    if selected == "自动检测":
        out = auto_detect_decode(inp)
    else:
        func = decoders[selected]
        out = func(inp)
    output_box.delete("1.0",tk.END)
    output_box.insert(tk.END, out)

# ===================== GUI界面 =====================
root = tk.Tk()
root.title("ARG-PDrNoxchen解码工具")
root.geometry("750x620")

# 标题
title_label = ttk.Label(root, text="ARG-PDrNoxchen解码工具", font=("Arial",16,"bold"))
title_label.pack(pady=10)

# 输入区域
ttk.Label(root,text="输入待解码文本：").pack(anchor="w",padx=20)
input_box = scrolledtext.ScrolledText(root, height=6, width=90)
input_box.pack(padx=20,pady=5)

# 下拉选择框，第一个选项是自动检测
combo = ttk.Combobox(root, values=["自动检测"] + list(decoders.keys()), state="readonly")
combo.current(0)
combo.pack(pady=5)

# 解码按钮
btn_decode = ttk.Button(root, text="执行解码", command=run_decode)
btn_decode.pack(pady=8)

# 输出区域
ttk.Label(root,text="解码结果：").pack(anchor="w",padx=20)
output_box = scrolledtext.ScrolledText(root, height=12, width=90)
output_box.pack(padx=20,pady=5)

# 底部作者信息
footer_label = ttk.Label(root, text="作者：Noxchen，作者官方网站：me.noxchen.dpdns.org",font=("Arial",10))
footer_label.pack(pady=12)

root.mainloop()