# Deep Learning

## 1. Tổng quan
Deep Learning là một nhánh của machine learning sử dụng mạng neural nhiều lớp. Mạng neural có khả năng học biểu diễn từ dữ liệu và đặc biệt hiệu quả với hình ảnh, âm thanh, văn bản và dữ liệu có cấu trúc phức tạp.

## 2. Neural Network
Một neural network cơ bản gồm input layer, hidden layers và output layer. Mỗi neuron thực hiện phép biến đổi tuyến tính rồi áp dụng activation function.

## 3. Activation Function
ReLU thường được sử dụng ở các hidden layer vì đơn giản và giúp giảm một số vấn đề liên quan đến gradient. Sigmoid phù hợp với một số bài toán nhị phân. Softmax thường được dùng để biến logits thành xác suất cho bài toán nhiều lớp.

## 4. Loss và Optimizer
Loss function đo mức độ sai lệch giữa dự đoán và nhãn thật. Optimizer cập nhật trọng số nhằm giảm loss. SGD và Adam là hai optimizer phổ biến.

## 5. Backpropagation
Backpropagation tính gradient của loss theo các tham số của mạng bằng quy tắc chuỗi. Sau đó optimizer sử dụng gradient để cập nhật trọng số.

## 6. CNN
Convolutional Neural Network phù hợp với dữ liệu có cấu trúc không gian như ảnh. Convolution giúp phát hiện các mẫu cục bộ, còn pooling có thể giảm kích thước biểu diễn.

## 7. RNN và LSTM
RNN được thiết kế cho dữ liệu tuần tự nhưng có thể gặp khó khăn khi chuỗi dài. LSTM bổ sung các cơ chế cổng để kiểm soát thông tin được lưu và quên, nhờ đó phù hợp hơn với nhiều bài toán sequence.
