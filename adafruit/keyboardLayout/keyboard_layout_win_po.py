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
        b'\x9e'  # '!'
        b'\x9f'  # '"'
        b'\xa0'  # '#'
        b'\xa1'  # '$'
        b'\xa2'  # '%'
        b'\xa3'  # '&'
        b'\x2d'  # "'"
        b'\xa5'  # '('
        b'\xa6'  # ')'
        b'\xaf'  # '*'
        b'\x2f'  # '+'
        b'\x36'  # ','
        b'\x38'  # '-'
        b'\x37'  # '.'
        b'\xa4'  # '/'
        b'\x27'  # '0'
        b'\x1e'  # '1'
        b'\x1f'  # '2'
        b'\x20'  # '3'
        b'\x21'  # '4'
        b'\x22'  # '5'
        b'\x23'  # '6'
        b'\x24'  # '7'
        b'\x25'  # '8'
        b'\x26'  # '9'
        b'\xb7'  # ':'
        b'\xb6'  # ';'
        b'\x64'  # '<'
        b'\xa7'  # '='
        b'\xe4'  # '>'
        b'\xad'  # '?'
        b'\x1f'  # '@'
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
        b'\x9c'  # 'Y'
        b'\x9d'  # 'Z'
        b'\x25'  # '['
        b'\x35'  # '\\'
        b'\x26'  # ']'
        b'\x00'
        b'\xb8'  # '_'
        b'\x00'
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
        b'\x1c'  # 'y'
        b'\x1d'  # 'z'
        b'\x24'  # '{'
        b'\xb5'  # '|'
        b'\x27'  # '}'
        b'\x00'
        b'\x00'
    )
    NEED_ALTGR = '@[]{}£§€'
    HIGHER_ASCII = {
        0xa3: 0x20,  # '£'
        0xa7: 0x21,  # '§'
        0x20ac: 0x22,  # '€'
        0xab: 0x2e,  # '«'
        0xbb: 0xae,  # '»'
        0xe7: 0x33,  # 'ç'
        0xc7: 0xb3,  # 'Ç'
        0xba: 0x34,  # 'º'
        0xaa: 0xb4,  # 'ª'
    }
    COMBINED_KEYS = {
        0xe4: 0x2fe1,  # 'ä'
        0xeb: 0x2fe5,  # 'ë'
        0xef: 0x2fe9,  # 'ï'
        0xf6: 0x2fef,  # 'ö'
        0xfc: 0x2ff5,  # 'ü'
        0xff: 0x2ff9,  # 'ÿ'
        0xc4: 0x2fc1,  # 'Ä'
        0xcb: 0x2fc5,  # 'Ë'
        0xcf: 0x2fc9,  # 'Ï'
        0xd6: 0x2fcf,  # 'Ö'
        0xdc: 0x2fd5,  # 'Ü'
        0xa8: 0x2fa0,  # '¨'
        0xe1: 0x3061,  # 'á'
        0xe9: 0x3065,  # 'é'
        0xed: 0x3069,  # 'í'
        0xf3: 0x306f,  # 'ó'
        0xfa: 0x3075,  # 'ú'
        0xfd: 0x3079,  # 'ý'
        0xc1: 0x3041,  # 'Á'
        0xc9: 0x3045,  # 'É'
        0xcd: 0x3049,  # 'Í'
        0xd3: 0x304f,  # 'Ó'
        0xda: 0x3055,  # 'Ú'
        0xdd: 0x3059,  # 'Ý'
        0xb4: 0x3020,  # '´'
        0xe0: 0xb061,  # 'à'
        0xe8: 0xb065,  # 'è'
        0xec: 0xb069,  # 'ì'
        0xf2: 0xb06f,  # 'ò'
        0xf9: 0xb075,  # 'ù'
        0xc0: 0xb041,  # 'À'
        0xc8: 0xb045,  # 'È'
        0xcc: 0xb049,  # 'Ì'
        0xd2: 0xb04f,  # 'Ò'
        0xd9: 0xb055,  # 'Ù'
        0x60: 0xb020,  # '`'
        0xe3: 0x3161,  # 'ã'
        0xf5: 0x316f,  # 'õ'
        0xf1: 0x316e,  # 'ñ'
        0xc3: 0x3141,  # 'Ã'
        0xd5: 0x314f,  # 'Õ'
        0xd1: 0x314e,  # 'Ñ'
        0x7e: 0x3120,  # '~'
        0xe2: 0xb161,  # 'â'
        0xea: 0xb165,  # 'ê'
        0xee: 0xb169,  # 'î'
        0xf4: 0xb16f,  # 'ô'
        0xfb: 0xb175,  # 'û'
        0xc2: 0xb141,  # 'Â'
        0xca: 0xb145,  # 'Ê'
        0xce: 0xb149,  # 'Î'
        0xd4: 0xb14f,  # 'Ô'
        0xdb: 0xb155,  # 'Û'
        0x5e: 0xb120,  # '^'
    }
