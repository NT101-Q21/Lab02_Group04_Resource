from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def error_propagation_test(mode_name, mode_type):
    key = b'1234567890123456' 
    iv = b'1234567890123456'  
    
    plaintext = b'A' * 1000
    plaintext_padded = pad(plaintext, AES.block_size)
    
    if mode_name == 'ECB':
        cipher = AES.new(key, mode_type)
    else:
        cipher = AES.new(key, mode_type, iv=iv)
    ciphertext = bytearray(cipher.encrypt(plaintext_padded))
    
    ciphertext[25] ^= 1 
    
    if mode_name == 'ECB':
        decipher = AES.new(key, mode_type)
    else:
        decipher = AES.new(key, mode_type, iv=iv)
    decrypted_text = decipher.decrypt(ciphertext)
    
    print(f"\n--- Chế độ: {mode_name} ---")
    for i in range(0, 64, 16): 
        original_block = plaintext_padded[i:i+16]
        decrypted_block = decrypted_text[i:i+16]
        if original_block != decrypted_block:
            print(f"Khối {i//16 + 1} (byte {i}-{i+15}): BỊ HỎNG")
        else:
            print(f"Khối {i//16 + 1} (byte {i}-{i+15}): OK")

if __name__ == "__main__":
    modes = [('ECB', AES.MODE_ECB), ('CBC', AES.MODE_CBC), 
             ('CFB', AES.MODE_CFB), ('OFB', AES.MODE_OFB)]
    for name, m_type in modes:
        error_propagation_test(name, m_type)