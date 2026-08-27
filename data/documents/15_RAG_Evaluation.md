# Đánh giá hệ thống RAG

## 1. Vì sao cần evaluation?
Một chatbot RAG có thể chạy thành công nhưng vẫn trả lời sai nếu retrieval lấy nhầm tài liệu hoặc LLM sử dụng context không đúng. Evaluation giúp xác định lỗi nằm ở retrieval hay generation.

## 2. Retrieval Quality
Có thể tạo bộ câu hỏi kèm các chunk hoặc tài liệu được xem là liên quan. Sau đó kiểm tra xem top-k retrieval có chứa thông tin cần thiết hay không.

## 3. Generation Quality
Câu trả lời có thể được đánh giá theo factuality, relevance, completeness và faithfulness. Faithfulness quan tâm việc câu trả lời có được hỗ trợ bởi context hay không.

## 4. Test Set
Một test set tốt nên có câu hỏi đơn giản, câu hỏi yêu cầu kết hợp nhiều đoạn, câu hỏi có từ khóa mơ hồ và câu hỏi mà knowledge base không có câu trả lời.

## 5. Negative Questions
Negative question là câu hỏi nằm ngoài phạm vi tài liệu. Hệ thống tốt nên nhận biết khi không đủ thông tin thay vì tự tạo câu trả lời.

## 6. Latency
Ngoài chất lượng, cần đo thời gian retrieval, thời gian inference và tổng thời gian phản hồi. Latency ảnh hưởng trực tiếp đến trải nghiệm chatbot.

## 7. Regression Test
Sau khi thay đổi chunk size, embedding model, retriever hoặc prompt, nên chạy lại bộ test. Điều này giúp phát hiện việc một cải tiến ở một nhóm câu hỏi lại làm giảm chất lượng ở nhóm khác.

## 8. Kết luận
RAG production-ready cần được đánh giá như một hệ thống hoàn chỉnh. Không nên chỉ nhìn vào chất lượng của LLM mà bỏ qua document parsing, chunking, embedding, retrieval và API.
