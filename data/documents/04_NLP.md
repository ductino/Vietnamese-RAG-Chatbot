# Natural Language Processing

## 1. NLP là gì?
Natural Language Processing là lĩnh vực kết hợp ngôn ngữ và máy tính nhằm giúp hệ thống xử lý văn bản hoặc tiếng nói của con người.

## 2. Tokenization
Tokenization chia văn bản thành các đơn vị nhỏ hơn như câu, từ hoặc subword. Đây thường là bước đầu trong pipeline NLP.

## 3. Bag of Words và TF-IDF
Bag of Words biểu diễn văn bản dựa trên tần suất xuất hiện của từ. TF-IDF giảm trọng số của những từ xuất hiện phổ biến trong nhiều tài liệu và tăng trọng số cho các từ có khả năng phân biệt tài liệu.

## 4. Word Embedding
Embedding biểu diễn từ hoặc câu bằng vector số trong không gian liên tục. Những văn bản có ý nghĩa gần nhau thường có vector gần nhau theo một thước đo phù hợp.

## 5. Text Classification
Phân loại văn bản có thể được dùng cho spam detection, phân loại chủ đề và sentiment analysis. Một pipeline thường gồm tokenize, vectorize, train classifier và evaluate.

## 6. Named Entity Recognition
NER xác định các thực thể trong văn bản như người, tổ chức, địa điểm hoặc thời gian. Kết quả thường được biểu diễn bằng các nhãn như B-PER, I-PER và O.

## 7. NLP tiếng Việt
Tiếng Việt có đặc điểm từ ghép, dấu câu và cách biểu diễn tên riêng cần được xử lý phù hợp. Tokenization và normalization nên được lựa chọn dựa trên dữ liệu và mục tiêu của bài toán.
