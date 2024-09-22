<?php
session_start();

set_error_handler(function ($errno, $errstr, $errfile, $errline) {
	// error was suppressed with the @-operator
	if (0 === error_reporting()) {
		return false;
	}

	throw new ErrorException($errstr, 0, $errno, $errfile, $errline);
});

try {
	$database = new PDO("sqlite:/tmp/db.sqlite");
	$database->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);

	$database->exec('CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(32) PRIMARY KEY, 
        password VARCHAR(60)
    )');

	$database->exec('CREATE TABLE IF NOT EXISTS files (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		owner VARCHAR(32),
		filename VARCHAR(255),
		modify_date DATETIME DEFAULT CURRENT_TIMESTAMP,
		size INTEGER,
		FOREIGN KEY(owner) REFERENCES users(username)
	)');
} catch (PDOException $e) {
	die("Could not connect to the database");
}

if (!isset($_SESSION['user'])) {
	include('./components/create_account.php');
} else {
	if (isset($_POST['settings'])) {
		$data = json_decode($_POST['settings'], true);
		if (!is_array($data)) {
			die;
		}
		$_SESSION['settings'] = $data;
	} else {
		include('./components/user_home.php');
	}
}
