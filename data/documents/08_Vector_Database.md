# Vector Database

## 1. Khái niệm
Vector database hoặc vector store được thiết kế để lưu và tìm kiếm các vector biểu diễn dữ liệu. Trong RAG, vector database thường lưu embedding của document chunks cùng metadata.

## 2. Similarity Search
Khi người dùng đặt câu hỏi, query được chuyển thành vector. Hệ thống tính độ tương đồng giữa query vector và các vector trong kho dữ liệu rồi lấy những kết quả gần nhất.

## 3. Cosine Similarity
Cosine similarity đo góc giữa hai vector. Giá trị càng gần nhau về hướng thì mức độ tương đồng càng cao. Đây là một metric phổ biến trong semantic search.

## 4. Metadata
Metadata có thể chứa tên tài liệu, trang, tiêu đề, loại file hoặc thời gian cập nhật. Metadata filtering giúp hệ thống giới hạn phạm vi tìm kiếm.

## 5. Top-k
Top-k là số lượng kết quả được lấy sau retrieval. k quá thấp có thể bỏ sót thông tin, trong khi k quá cao có thể đưa nhiều context không liên quan vào prompt.

## 6. FAISS
FAISS là thư viện hỗ trợ similarity search trên vector. Nó phù hợp cho nhiều bài toán tìm kiếm vector và có thể được sử dụng làm thành phần retrieval trong ứng dụng RAG.

## 7. Thiết kế index
Khi xây dựng index, cần cân nhắc kích thước vector, metric, số lượng dữ liệu, tốc độ tìm kiếm và bộ nhớ. Với dữ liệu nhỏ, một index đơn giản thường đủ để thử nghiệm.
