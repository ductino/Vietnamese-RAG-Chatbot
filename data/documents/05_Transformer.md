# Transformer

## 1. Ý tưởng chính
Transformer là kiến trúc neural network dựa mạnh vào cơ chế attention thay vì phụ thuộc hoàn toàn vào recurrent processing. Kiến trúc này trở thành nền tảng cho nhiều mô hình NLP hiện đại.

## 2. Attention
Attention cho phép mô hình xác định mức độ liên quan giữa các token khi tạo biểu diễn cho một token. Query, Key và Value là ba thành phần quan trọng của cơ chế attention.

## 3. Self-Attention
Trong self-attention, các token của cùng một chuỗi được sử dụng để tính quan hệ với nhau. Nhờ đó mô hình có thể xem xét thông tin ở nhiều vị trí trong câu.

## 4. Multi-Head Attention
Multi-head attention sử dụng nhiều attention head. Mỗi head có thể học một kiểu quan hệ khác nhau, sau đó các kết quả được kết hợp.

## 5. Positional Encoding
Transformer không xử lý tuần tự giống RNN nên cần thông tin về vị trí token. Positional encoding hoặc positional embeddings bổ sung thông tin vị trí vào biểu diễn.

## 6. Encoder và Decoder
Một Transformer có thể gồm encoder, decoder hoặc cả hai. Các mô hình encoder thường phù hợp với hiểu văn bản, trong khi decoder thường phù hợp với sinh văn bản.

## 7. Ứng dụng
Transformer được sử dụng trong machine translation, text classification, question answering, summarization và các hệ thống LLM.
