# Retrieval-Augmented Generation

## 1. RAG là gì?
RAG là kiến trúc kết hợp retrieval và generation. Hệ thống tìm các đoạn tài liệu liên quan đến câu hỏi rồi cung cấp chúng cho LLM làm context để tạo câu trả lời. Cách tiếp cận này cho phép cập nhật knowledge base mà không nhất thiết phải huấn luyện lại toàn bộ mô hình.

## 2. Pipeline RAG
Pipeline cơ bản gồm document loading, cleaning, chunking, embedding, indexing, retrieval và generation.

## 3. Document Loading
Document loader đọc dữ liệu từ các định dạng như Markdown, TXT, DOCX hoặc PDF. Mỗi tài liệu nên đi kèm metadata như tên file, nguồn hoặc loại tài liệu để hỗ trợ truy xuất và hiển thị nguồn.

## 4. Chunking
Chunking chia tài liệu lớn thành những đoạn nhỏ hơn. Chunk quá nhỏ có thể thiếu ngữ cảnh, còn chunk quá lớn làm tăng lượng thông tin không liên quan. Có thể sử dụng overlap giữa các chunk để giảm việc cắt mất ngữ cảnh.

## 5. Embedding
Embedding chuyển văn bản thành vector số. Query và document chunk có thể được so sánh trong cùng không gian vector để tìm nội dung có ý nghĩa gần nhau.

## 6. Retrieval
Retriever nhận câu hỏi, tạo query embedding rồi tìm những chunk gần nhất trong vector store. Có thể lấy top-k kết quả và áp dụng reranking nếu cần.

## 7. Generation
LLM nhận câu hỏi cùng context được truy xuất và tạo câu trả lời. Prompt nên yêu cầu mô hình ưu tiên thông tin trong context và thừa nhận khi tài liệu không đủ dữ liệu.

## 8. Đánh giá RAG
Một hệ thống RAG cần đánh giá cả retrieval và generation. Retrieval có thể xem xét độ liên quan của chunk được tìm thấy. Generation cần đánh giá tính đúng đắn, đầy đủ, bám nguồn và mức độ không bịa thông tin.
