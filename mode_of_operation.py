from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'1234567890123456'
iv  = b'abcdefghijklmnop' 
plaintext = b"UIT_LAB_UIT_LAB_UIT_LAB_UIT_LAB_"  # 32 bytes (2 blocks)

cipher_ecb = AES.new(key, AES.MODE_ECB)
ct_ecb = cipher_ecb.encrypt(plaintext)

cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
ct_cbc = cipher_cbc.encrypt(plaintext)

print("Ciphertexts:")
print(f"ECB: {ct_ecb.hex()}")
print(f"CBC: {ct_cbc.hex()}")

def split_blocks(data, block_size=16):
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]

ecb_blocks = split_blocks(ct_ecb)
cbc_blocks = split_blocks(ct_cbc)

print("\nECB blocks:")
for i, b in enumerate(ecb_blocks):
    print(f"Block {i}: {b.hex()}")

print("\nCBC blocks:")
for i, b in enumerate(cbc_blocks):
    print(f"Block {i}: {b.hex()}")