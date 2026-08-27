# Docker

## 1. Docker là gì?
Docker là nền tảng đóng gói ứng dụng cùng dependencies vào container. Container giúp môi trường chạy ứng dụng nhất quán hơn giữa các máy.

## 2. Image và Container
Image là template dùng để tạo container. Container là instance đang chạy của image và có filesystem, process cùng cấu hình riêng.

## 3. Dockerfile
Dockerfile mô tả các bước xây dựng image. Các instruction phổ biến gồm FROM, WORKDIR, COPY, RUN, ENV và CMD.

## 4. Docker Compose
Docker Compose giúp mô tả và chạy nhiều service. Một hệ thống RAG có thể gồm backend API, vector database và các service hỗ trợ khác.

## 5. Volume
Volume giúp lưu dữ liệu bền vững bên ngoài vòng đời container. Điều này hữu ích với database hoặc vector index cần giữ lại sau khi container bị xóa.

## 6. Network
Các container có thể giao tiếp với nhau qua Docker network. Compose có thể tạo network để các service gọi nhau bằng tên service.

## 7. Docker cho AI
Docker giúp đóng gói môi trường Python, thư viện embedding, API backend và cấu hình. Khi project chạy local ổn định, container hóa giúp việc triển khai sang môi trường khác dễ hơn.
