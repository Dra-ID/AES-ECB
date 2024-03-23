# Source Generated with Decompyle++
# File: main_encrypted_pyc.pyc (Python 3.11)

import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import random
import marshal
import binascii
import lzma
import gzip
import bz2
import zlib
import py_compile

def encrypt_code(code, key):
    watermark = 'AmmarBN & VindraGanz'
    code_with_watermark = f'''{code}\n# Watermark: {watermark}'''
    compiled_code = compile(code_with_watermark, '<string>', 'exec')
    bytecode = marshal.dumps(compiled_code)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_bytecode = pad(bytecode, AES.block_size)
    encrypted_bytecode = cipher.encrypt(padded_bytecode)
    return binascii.b2a_base64(encrypted_bytecode)


def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = pad(message.encode(), AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return binascii.b2a_base64(encrypted_message)


def obfuscate_code(code):
    obfuscated_code = code.replace('exec', 'x_x_e_c')
    return obfuscated_code


def banner():
    print('\n\n  __   ____  ____        ____  ___  ____\n / _\\ (  __)/ ___)  ___ (  __)/ __)(  _ )\n/    \\ ) _) \\___ \\ (___) ) _)( (__  ) _ (\n\\_/\\_/(____)(____/      (____)\\___)(____/\n\n • Creator: AmmarBN\n • Github : github.com/Dra-ID\n • Info   : AES-ECB Python3 Encryption\n')


def main():
    os.system('clear')
    banner()
    input_file = input(' • Enter File Name (exam:main.py): ')

    try:
        with open(input_file, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print("File not found.")
        return

    # Generate random 16-byte key
    key = bytes([random.randint(0, 255) for _ in range(16)])
    
    # Obfuscate source code
    obfuscated_code = obfuscate_code(code)
    
    # Encrypt source code
    encrypted_code = encrypt_code(obfuscated_code, key)
    
    # Encrypt access denied message
    access_denied_message = "Cannot run: Credit has been removed, access denied"
    encrypted_message = encrypt_message(access_denied_message, key).decode('utf-8')

    # Define variable c
    c = base64.b64encode('AmmarBN & VindraGanz'.encode()).decode('utf-8')
    output_file = input_file.split('.')[0] + "_encrypted.py"

    with open(output_file, 'w') as file:
        file.write(f"import base64\n")
        file.write(f"aes_ebc=(")
        for _ in range(3000):
           file.write('"404 Not Found","404 Not Found","404 Not Found","404 Not Found","404 Not Found",\n')
        file.write(")\n")
        file.write(f"from Crypto.Cipher import AES\n")
        file.write(f"from Crypto.Util.Padding import unpad\n")
        file.write(f"import sys,marshal,binascii\n")
        file.write(f"key = {key}\n")
        file.write(f"aes_ebc2=(")
        for _ in range(3000):
           file.write('"Your Wellcome","Your Wellcome","Your Wellcome","Your Wellcome","Your Wellcome",\n')
        file.write(")\n")
        file.write(f"cipher = AES.new(key, AES.MODE_ECB)\n")
        file.write(f"__________________________________________________________________________________________________________________ = binascii.a2b_base64({encrypted_code})\n")
        file.write(f"________________________________________________________________________________________________________________ = unpad(cipher.decrypt(__________________________________________________________________________________________________________________), AES.block_size)\n")
        file.write(f"______________________________________________________________________________________________________________ = marshal.loads(________________________________________________________________________________________________________________)\n")
        file.write(f"_____________________________________________________________________________________________________________= exec\n")
        file.write(f"________________________________________________________ = '{c}'\n")
        file.write(f"_____________________________________________ = lambda: _____________________________________________________________________________________________________________(______________________________________________________________________________________________________________, globals())\n")
        file.write(f"try:\n")
        file.write(f"    if binascii.a2b_base64(________________________________________________________.encode()).decode('utf-8') != 'AmmarBN & VindraGanz':\n")
        file.write(f"        raise Exception('Cannot run: Credit has been removed, access denied')\n")
        file.write(f"    _____________________________________________()\n")
        file.write(f"except Exception as e:\n")
        file.write(f"    print('Error during execution:', e)\n")
        file.write(f"    sys.exit(1)\n")
        file.write(f"# Ngapain Setan? Mau decrypt? Tolol tukang record Minimal Izin Dulu Kontol")

#    py_compile.compile(output_file,output_file)
    print("File has been successfully encrypted. Encrypted file is saved as:", output_file)

if __name__ == "__main__":
    main()
