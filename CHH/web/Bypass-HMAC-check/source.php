<?php
include_once('./ignore/design/design.php');
$design = Design(__FILE__, 'HMAC Type Juggling');
?>
<html>
  <head>
    <title>HMAC Type Juggling</title>
  </head>
    <body>
        <div>
            <?php echo $design; ?>  
        </div>
    </body>
</html>
<?php

if (empty($_POST['hmac']) || empty($_POST['host'])) {
    echo "Please Create a HTTP Request<br>";
    echo "Method: POST <br>";
    echo "Body: hmac=xxx&host=xxx&nonce=xxx";
    exit;       
}

$secret = trim(file_get_contents('/secret.txt'));

if (isset($_POST['nonce']))
    $secret = hash_hmac('sha256', $_POST['nonce'], $secret);

$hmac = hash_hmac('sha256', $_POST['host'], $secret);

if ($hmac !== $_POST['hmac']) {
    echo "Access Deny!";
    exit;
}
echo exec("host".$_POST['host']);
?>