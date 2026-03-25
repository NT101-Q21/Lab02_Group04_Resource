# Lab02_Group04_Resource

## MỤC TIÊU
- Hiểu cấu trúc Feistel: Hiện thực hóa vòng lặp Feistel và quan sát hiệu ứng thác đổ (avalanche effect) khi thay đổi dữ liệu đầu vào.
- Phân tích các chế độ AES: So sánh sự khác biệt về bản mã và khả năng bảo mật giữa các chế độ ECB, CBC, CFB, OFB và CTR.
- Đánh giá tính kháng phân tích: Sử dụng thuật toán DES để kiểm tra sự thay đổi của bản mã khi bản rõ hoặc khóa thay đổi một lượng rất nhỏ.
- Nghiên cứu lan truyền lỗi: Phân tích mức độ ảnh hưởng của một bit lỗi trong bản mã đến dữ liệu giải mã trên các chế độ hoạt động khác nhau.
- So sánh các thuật toán đối xứng: Đánh giá ưu nhược điểm của DES, 2DES, 3DES và AES.
- Lý thuyết số ứng dụng: Xây dựng các công cụ kiểm tra số nguyên tố (Miller-Rabin), tính GCD và lũy thừa module với số mũ lớn.

## NỘI DUNG
- Nhiệm vụ 2.1: Cấu trúc Feistel & Avalanche Effect
    - Hiện thực hàm feistel_round dựa trên định lý mật mã.
    - Mã hóa các bản rõ chỉ khác nhau 1 bit ($M_1=0xAB$ và $M_2=0xAC$) qua 4 vòng để theo dõi sự khuếch tán sai khác.

- Nhiệm vụ 2.2: Chế độ hoạt động của AES
    - Sử dụng thư viện pycryptodome để mã hóa chuỗi văn bản có tính lặp lại cao.
    - Chứng minh nhược điểm lộ mô hình dữ liệu của chế độ ECB so với CBC.
    - Tổng hợp bảng so sánh ưu/khuyết điểm của ECB, CBC, CFB, OFB và CTR.

- Nhiệm vụ 2.3: Kiểm tra Hamming Distance với DES
    - Mã hóa chuỗi "STAYHOME" và "STAYHOMA" bằng DES.
    - Tính toán khoảng cách Hamming và tỷ lệ thay đổi bit (thường dao động quanh mức 45-58%) để xác nhận tính kháng phân tích sai biệt.

- Nhiệm vụ 2.4: Đặc tính lan truyền lỗi (Error Propagation)
    - Mã hóa dữ liệu 1000 byte bằng AES-128 và chủ động làm hỏng 1 bit tại byte thứ 26.

- Nhiệm vụ 2.5: So sánh DES, 3DES và AES
    - Phân tích sự tiến hóa về độ dài khóa (56 bit lên đến 256 bit) và cấu trúc thuật toán.
    - Giải thích lý do không dùng Double-DES (2DES).

- Nhiệm vụ 2.6: Thuật toán số học cơ bản
    - Tạo số nguyên tố ngẫu nhiên (8, 16, 64 bits).
    - Sử dụng kiểm tra Miller-Rabin để tìm 10 số nguyên tố lớn nhất nhỏ hơn số Mersenne thứ 10 ($2^{89}-1$).
    - Tính toán Ước số chung lớn nhất (GCD) bằng thuật toán Euclid và Lũy thừa Module nhanh.