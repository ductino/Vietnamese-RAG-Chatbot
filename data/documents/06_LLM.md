# Large Language Model

## 1. LLM là gì?
Large Language Model là mô hình ngôn ngữ có quy mô lớn được huấn luyện trên lượng dữ liệu văn bản đáng kể. Mục tiêu của nhiều mô hình là học cách dự đoán token tiếp theo hoặc xây dựng biểu diễn ngôn ngữ.

## 2. Token
LLM không nhất thiết xử lý nguyên từ. Văn bản thường được chia thành token, có thể là từ, phần của từ hoặc ký hiệu. Context window giới hạn lượng token mà mô hình có thể xử lý trong một lần.

## 3. Pretraining
Trong pretraining, mô hình học từ dữ liệu lớn thông qua một objective xác định trước. Giai đoạn này tạo nền tảng kiến thức và khả năng xử lý ngôn ngữ.

## 4. Inference
Inference là quá trình sử dụng mô hình đã huấn luyện để tạo kết quả cho input mới. Các tham số như temperature có thể ảnh hưởng đến mức độ đa dạng của kết quả sinh.

## 5. Prompt
Prompt là phần hướng dẫn và dữ liệu được đưa vào mô hình. Một prompt rõ ràng có thể giúp mô hình hiểu nhiệm vụ, định dạng đầu ra và phạm vi thông tin cần sử dụng.

## 6. Fine-tuning
Fine-tuning tiếp tục huấn luyện mô hình trên một tập dữ liệu chuyên biệt. Phương pháp này có thể giúp mô hình thích nghi với một nhiệm vụ hoặc phong cách cụ thể.

## 7. RAG và LLM
RAG bổ sung nguồn dữ liệu bên ngoài cho LLM. Thay vì buộc mô hình phải ghi nhớ toàn bộ tài liệu trong tham số, hệ thống truy xuất các đoạn liên quan rồi đưa chúng vào context khi sinh câu trả lời.
