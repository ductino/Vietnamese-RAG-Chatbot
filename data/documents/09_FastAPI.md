# FastAPI

## 1. FastAPI là gì?
FastAPI là framework Python hiện đại để xây dựng web API. Nó sử dụng Python type hints và hỗ trợ tự động tạo tài liệu API.

## 2. Endpoint
Endpoint là địa chỉ mà client gọi để thực hiện một chức năng. Các HTTP method phổ biến gồm GET, POST, PUT, PATCH và DELETE.

## 3. Request và Response
Request chứa dữ liệu client gửi lên server. Response là dữ liệu server trả về. Với API JSON, response thường chứa object hoặc list được tuần tự hóa thành JSON.

## 4. Pydantic
Pydantic được sử dụng để khai báo và kiểm tra dữ liệu đầu vào thông qua model. Điều này giúp API xác định rõ kiểu dữ liệu mong đợi.

## 5. API cho RAG Chatbot
Một RAG chatbot có thể cung cấp endpoint POST /chat. Client gửi câu hỏi trong JSON, backend thực hiện embedding, retrieval và gọi LLM, sau đó trả về answer cùng danh sách nguồn.

## 6. Tài liệu API
FastAPI có thể tạo giao diện Swagger UI tại /docs và ReDoc tại /redoc. Đây là cách thuận tiện để kiểm tra endpoint trong quá trình phát triển.

## 7. Triển khai
Trong development có thể chạy FastAPI bằng server hỗ trợ ASGI. Khi triển khai thực tế cần quan tâm đến process workers, reverse proxy, logging, environment variables và bảo mật.
