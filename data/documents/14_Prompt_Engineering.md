# Prompt Engineering

## 1. Prompt là gì?
Prompt là đầu vào hướng dẫn mô hình thực hiện một nhiệm vụ. Prompt có thể chứa vai trò, mục tiêu, dữ liệu, ràng buộc và định dạng đầu ra mong muốn.

## 2. Prompt rõ ràng
Một prompt tốt nên nói rõ nhiệm vụ, phạm vi thông tin và yêu cầu đầu ra. Nếu cần trả lời dựa trên tài liệu, prompt nên chỉ rõ context được cung cấp.

## 3. Few-shot
Few-shot prompting cung cấp một số ví dụ input-output để mô hình hiểu mẫu nhiệm vụ. Phương pháp này có thể hữu ích khi yêu cầu định dạng hoặc phân loại cụ thể.

## 4. Structured Output
Ứng dụng có thể yêu cầu mô hình trả về JSON hoặc một cấu trúc cố định. Điều này giúp backend xử lý kết quả dễ hơn.

## 5. Prompt trong RAG
Trong RAG, prompt thường gồm system instruction, câu hỏi của người dùng và các đoạn context được retrieval. Prompt nên yêu cầu mô hình không tự suy diễn khi context không chứa câu trả lời.

## 6. Hallucination
Hallucination là trường hợp mô hình tạo thông tin không được hỗ trợ hoặc không chính xác. RAG, grounding, validation và evaluation có thể giúp giảm rủi ro nhưng không đảm bảo loại bỏ hoàn toàn.

## 7. Evaluation
Prompt cần được kiểm thử trên nhiều dạng câu hỏi. Không nên đánh giá một prompt chỉ dựa trên một vài câu hỏi mẫu.
