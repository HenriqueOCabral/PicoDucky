# SPDX-FileCopyrightText: 2021 Neradoc NeraOnGit@ri1.fr
#
# SPDX-License-Identifier: MIT
"""
This file was automatically generated using Circuitpython_Keyboard_Layouts
"""


__version__ = '0.0.3'
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


from keyboard_layout import KeyboardLayoutBase
class KeyboardLayout(KeyboardLayoutBase):
    ASCII_TO_KEYCODE = (
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2a'  # BACKSPACE
        b'\x2b'  # '\t'
        b'\x28'  # '\n'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x29'  # ESC
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2c'  # ' '
        b'\xb4'  # '!'
        b'\xb3'  # '"'
        b'\x1b'  # '#'
        b'\x33'  # '$'
        b'\xad'  # '%'
        b'\x06'  # '&'
        b'\xb1'  # "'"
        b'\xb0'  # '('
        b'\x30'  # ')'
        b'\x38'  # '*'
        b'\x1e'  # '+'
        b'\x36'  # ','
        b'\x38'  # '-'
        b'\x37'  # '.'
        b'\xaf'  # '/'
        b'\xa7'  # '0'
        b'\x9e'  # '1'
        b'\x9f'  # '2'
        b'\xa0'  # '3'
        b'\xa1'  # '4'
        b'\xa2'  # '5'
        b'\xa3'  # '6'
        b'\xa4'  # '7'
        b'\xa5'  # '8'
        b'\xa6'  # '9'
        b'\xb7'  # ':'
        b'\x35'  # ';'
        b'\x36'  # '<'
        b'\x2d'  # '='
        b'\x37'  # '>'
        b'\xb6'  # '?'
        b'\x19'  # '@'
        b'\x84'  # 'A'
        b'\x85'  # 'B'
        b'\x86'  # 'C'
        b'\x87'  # 'D'
        b'\x88'  # 'E'
        b'\x89'  # 'F'
        b'\x8a'  # 'G'
        b'\x8b'  # 'H'
        b'\x8c'  # 'I'
        b'\x8d'  # 'J'
        b'\x8e'  # 'K'
        b'\x8f'  # 'L'
        b'\x90'  # 'M'
        b'\x91'  # 'N'
        b'\x92'  # 'O'
        b'\x93'  # 'P'
        b'\x94'  # 'Q'
        b'\x95'  # 'R'
        b'\x96'  # 'S'
        b'\x97'  # 'T'
        b'\x98'  # 'U'
        b'\x99'  # 'V'
        b'\x9a'  # 'W'
        b'\x9b'  # 'X'
        b'\x9d'  # 'Y'
        b'\x9c'  # 'Z'
        b'\x09'  # '['
        b'\x14'  # '\\'
        b'\x0a'  # ']'
        b'\x00'  # '^' (Dead key)
        b'\xb8'  # '_'
        b'\x00'  # '`' (Dead key)
        b'\x04'  # 'a'
        b'\x05'  # 'b'
        b'\x06'  # 'c'
        b'\x07'  # 'd'
        b'\x08'  # 'e'
        b'\x09'  # 'f'
        b'\x0a'  # 'g'
        b'\x0b'  # 'h'
        b'\x0c'  # 'i'
        b'\x0d'  # 'j'
        b'\x0e'  # 'k'
        b'\x0f'  # 'l'
        b'\x10'  # 'm'
        b'\x11'  # 'n'
        b'\x12'  # 'o'
        b'\x13'  # 'p'
        b'\x14'  # 'q'
        b'\x15'  # 'r'
        b'\x16'  # 's'
        b'\x17'  # 't'
        b'\x18'  # 'u'
        b'\x19'  # 'v'
        b'\x1a'  # 'w'
        b'\x1b'  # 'x'
        b'\x1d'  # 'y'
        b'\x1c'  # 'z'
        b'\x05'  # '{'
        b'\x1a'  # '|'
        b'\x11'  # '}'
        b'\x1e'  # '~'
        b'\x00'
    )
    NEED_ALTGR = '#$&*<>@[\\]{|}~¤×ß÷ĐđŁł€'
    HIGHER_ASCII = {
        0x11b: 0x1f,  # 'ě'
        0x161: 0x20,  # 'š'
        0x10d: 0x21,  # 'č'
        0x159: 0x22,  # 'ř'
        0x17e: 0x23,  # 'ž'
        0xfd: 0x24,  # 'ý'
        0xe1: 0x25,  # 'á'
        0xed: 0x26,  # 'í'
        0xe9: 0x27,  # 'é'
        0x20ac: 0x08,  # '€'
        0xfa: 0x2f,  # 'ú'
        0xf7: 0x2f,  # '÷'
        0xd7: 0x30,  # '×'
        0x111: 0x16,  # 'đ'
        0x110: 0x07,  # 'Đ'
        0x142: 0x0e,  # 'ł'
        0x141: 0x0f,  # 'Ł'
        0x16f: 0x33,  # 'ů'
        0xa7: 0x34,  # '§'
        0xdf: 0x34,  # 'ß'
        0xa4: 0x31,  # '¤'
    }
    COMBINED_KEYS = {
        0x10d: 0x1fe3,  # 'č'
        0x10c: 0x1fc3,  # 'Č'
        0x10f: 0x1fe4,  # 'ď'
        0x10e: 0x1fc4,  # 'Ď'
        0x11b: 0x1fe5,  # 'ě'
        0x11a: 0x1fc5,  # 'Ě'
        0x13e: 0x1fec,  # 'ľ'
        0x13d: 0x1fcc,  # 'Ľ'
        0x148: 0x1fee,  # 'ň'
        0x147: 0x1fce,  # 'Ň'
        0x159: 0x1ff2,  # 'ř'
        0x158: 0x1fd2,  # 'Ř'
        0x161: 0x1ff3,  # 'š'
        0x160: 0x1fd3,  # 'Š'
        0x165: 0x1ff4,  # 'ť'
        0x164: 0x1fd4,  # 'Ť'
        0x17e: 0x1ffa,  # 'ž'
        0x17d: 0x1fda,  # 'Ž'
        0x2c7: 0x1fa0,  # 'ˇ'
        0xe2: 0x20e1,  # 'â'
        0xc2: 0x20c1,  # 'Â'
        0xea: 0x20e5,  # 'ê'
        0xca: 0x20c5,  # 'Ê'
        0xee: 0x20e9,  # 'î'
        0xce: 0x20c9,  # 'Î'
        0xf4: 0x20ef,  # 'ô'
        0xd4: 0x20cf,  # 'Ô'
        0xfb: 0x20f5,  # 'û'
        0xdb: 0x20d5,  # 'Û'
        0x5e: 0x20a0,  # '^'
        0x103: 0x21e1,  # 'ă'
        0x102: 0x21c1,  # 'Ă'
        0x11f: 0x21e7,  # 'ğ'
        0x11e: 0x21c7,  # 'Ğ'
        0x2d8: 0x21a0,  # '˘'
        0xe5: 0x22e1,  # 'å'
        0xc5: 0x22c1,  # 'Å'
        0x16f: 0x22f5,  # 'ů'
        0x16e: 0x22d5,  # 'Ů'
        0xb0: 0x22a0,  # '°'
        0x105: 0x23e1,  # 'ą'
        0x104: 0x23c1,  # 'Ą'
        0x119: 0x23e5,  # 'ę'
        0x118: 0x23c5,  # 'Ę'
        0x12f: 0x23e9,  # 'į'
        0x12e: 0x23c9,  # 'Į'
        0x173: 0x23f5,  # 'ų'
        0x172: 0x23d5,  # 'Ų'
        0x2db: 0x23a0,  # '˛'
        0xe0: 0x24e1,  # 'à'
        0xc0: 0x24c1,  # 'À'
        0xe8: 0x24e5,  # 'è'
        0xc8: 0x24c5,  # 'È'
        0xec: 0x24e9,  # 'ì'
        0xcc: 0x24c9,  # 'Ì'
        0xf2: 0x24ef,  # 'ò'
        0xd2: 0x24cf,  # 'Ò'
        0xf9: 0x24f5,  # 'ù'
        0xd9: 0x24d5,  # 'Ù'
        0x60: 0x24a0,  # '`'
        0x117: 0x25e5,  # 'ė'
        0x116: 0x25c5,  # 'Ė'
        0x131: 0x25e9,  # 'ı'
        0x130: 0x25c9,  # 'İ'
        0x17c: 0x25fa,  # 'ż'
        0x17b: 0x25da,  # 'Ż'
        0xb7: 0x25a0,  # '·'
        0xe1: 0x26e1,  # 'á'
        0xc1: 0x26c1,  # 'Á'
        0x107: 0x26e3,  # 'ć'
        0x106: 0x26c3,  # 'Ć'
        0xe9: 0x26e5,  # 'é'
        0xc9: 0x26c5,  # 'É'
        0xed: 0x26e9,  # 'í'
        0xcd: 0x26c9,  # 'Í'
        0x13a: 0x26ec,  # 'ĺ'
        0x139: 0x26cc,  # 'Ĺ'
        0x144: 0x26ee,  # 'ń'
        0x143: 0x26ce,  # 'Ń'
        0xf3: 0x26ef,  # 'ó'
        0xd3: 0x26cf,  # 'Ó'
        0x155: 0x26f2,  # 'ŕ'
        0x154: 0x26d2,  # 'Ŕ'
        0x15b: 0x26f3,  # 'ś'
        0x15a: 0x26d3,  # 'Ś'
        0xfa: 0x26f5,  # 'ú'
        0xda: 0x26d5,  # 'Ú'
        0xfd: 0x26f9,  # 'ý'
        0xdd: 0x26d9,  # 'Ý'
        0x17a: 0x26fa,  # 'ź'
        0x179: 0x26da,  # 'Ź'
        0xb4: 0x26a0,  # '´'
        0x151: 0x27ef,  # 'ő'
        0x150: 0x27cf,  # 'Ő'
        0x171: 0x27f5,  # 'ű'
        0x170: 0x27d5,  # 'Ű'
        0x2dd: 0x27a0,  # '˝'
        0xe4: 0x2de1,  # 'ä'
        0xc4: 0x2dc1,  # 'Ä'
        0xeb: 0x2de5,  # 'ë'
        0xcb: 0x2dc5,  # 'Ë'
        0xef: 0x2de9,  # 'ï'
        0xcf: 0x2dc9,  # 'Ï'
        0xf6: 0x2def,  # 'ö'
        0xd6: 0x2dcf,  # 'Ö'
        0xfc: 0x2df5,  # 'ü'
        0xdc: 0x2dd5,  # 'Ü'
        0xff: 0x2df9,  # 'ÿ'
        0x178: 0x2dd9,  # 'Ÿ'
        0xa8: 0x2da0,  # '¨'
        0xe7: 0x2ee3,  # 'ç'
        0xc7: 0x2ec3,  # 'Ç'
        0x123: 0x2ee7,  # 'ģ'
        0x122: 0x2ec7,  # 'Ģ'
        0x137: 0x2eeb,  # 'ķ'
        0x136: 0x2ecb,  # 'Ķ'
        0x13c: 0x2eec,  # 'ļ'
        0x13b: 0x2ecc,  # 'Ļ'
        0x146: 0x2eee,  # 'ņ'
        0x145: 0x2ece,  # 'Ņ'
        0x157: 0x2ef2,  # 'ŗ'
        0x156: 0x2ed2,  # 'Ŗ'
        0x15f: 0x2ef3,  # 'ş'
        0x15e: 0x2ed3,  # 'Ş'
        0x163: 0x2ef4,  # 'ţ'
        0x162: 0x2ed4,  # 'Ţ'
        0xb8: 0x2ea0,  # '¸'
    }
