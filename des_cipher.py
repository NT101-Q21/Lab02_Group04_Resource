from Crypto.Cipher import DES

def avalanche_test(key):
    key = key.encode('utf-8')
    p1 = b'STAYHOME'
    p2 = b'STAYHOMA'

    cipher = DES.new(key, DES.MODE_ECB)
    c1 = cipher.encrypt(p1)
    c2 = cipher.encrypt(p2)

    b1 = bin(int.from_bytes(c1, 'big'))[2:].zfill(64)
    b2 = bin(int.from_bytes(c2, 'big'))[2:].zfill(64)

    diff_bits = sum(1 for bit1, bit2 in zip(b1, b2) if bit1 != bit2)

    percentage = (diff_bits) / 64 * 100

    print(f"Key: {key}")
    print(f"Bản mã 1: {b1}")
    print(f"Bản mã 2: {b2}")
    print(f"Số bit khác nhau: {diff_bits}/64")
    print(f"Tỷ lệ thay đổi :{percentage:.2f}%")

if __name__ == "__main__":
    key = input("Nhập khóa(MSSV): ")
    avalanche_test(key)
