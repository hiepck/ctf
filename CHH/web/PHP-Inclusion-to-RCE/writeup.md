## PHP Inclusion to RCE
Link challenge: https://battle.cookiearena.org/challenges/web/php-inclusion-to-rce

![Alt text](image.png)

Như tiêu đề thì đây là LFI và mình phải tìm cách RCE chứ không phải một phát ăn luôn

![Alt text](image-1.png)

Trong source thì flag ở root nhưng tên file flag đã được thêm mắm muối không thể đoán, mình fuzz thử xem thế nào. Nhưng trước khi fuzz thì mình search xem có cách nào để RCE không thì tìm được được kĩ thuật `LFI to RCE via log Poisoning` có nghĩ là mình sẽ phải tìm xem log của dịch vụ nào có thể đọc và ghi được không.

![Alt text](image-3.png)

Vì webserver là Ngix nên mình thử một số payload:

![Alt text](image-4.png)

ở đây nó filter ../->'' nên mình dùng payload trên

![Alt text](image-5.png)

Giờ mình cần tạo ra lỗi khi request

![Alt text](image-6.png)

Phải send 2 lần mới nhìn thấy, và rồi lấy flag thôi

![Alt text](image-7.png)
