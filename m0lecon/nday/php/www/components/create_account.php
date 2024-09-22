<?php

require_once __DIR__ . '/Hashcash.php';
const POW_BITS = 28;

if (isset($_SESSION['user'])) {
	die;
}

function create_account()
{
	global $database;

	$hashcash = new \TheFox\Pow\Hashcash();

	try {
		if (
			!$hashcash->verify($_POST['pow'])
			|| $hashcash->getBits() !== POW_BITS
			|| $hashcash->getResource() !== $_SESSION['pow']
		) {
			throw new Exception();
		}
		unset($_SESSION['pow']);
	} catch (Exception $e) {
		$_SESSION['flash_error'] = "Invalid PoW!";
		return;
	}

	$opts = ['http' => ['method' => 'POST',]];
	$context = stream_context_create($opts);
	$response = file_get_contents('http://ftp:3000/create-user', false, $context);

	$response = json_decode($response, false);

	if (isset($response->error)) {
		$_SESSION['flash_error'] = $response->error;
		return;
	}

	$stmt = $database->prepare('INSERT INTO users (username, password) VALUES (:username, :password)');
	$stmt->execute(['username' => $response->username, 'password' => $response->password]);

	$_SESSION['flash_success'] = "Account created successfully!<br />Username: <span class='font-monospace'>{$response->username}</span>, password: <span class='font-monospace'>{$response->password}</span>";
}

if (isset($_POST['create_account']) && isset($_POST['pow'])) {
	create_account();
}
if (isset($_POST['login']) && isset($_POST['username']) && isset($_POST['password'])) {
	$stmt = $database->prepare('SELECT * FROM users WHERE username = :username AND password = :password');
	$stmt->execute(['username' => $_POST['username'], 'password' => $_POST['password']]);
	$user = $stmt->fetch();

	if ($user) {
		$_SESSION['user'] = $user->username;
		$_SESSION['password'] = $user->password;
		$_SESSION['settings'] = ['overwrite' => false];
		header('Location: /');
		exit;
	} else {
		$_SESSION['flash_error'] = "Invalid username or password!";
	}
}


if (!isset($_SESSION['pow'])) {
	$_SESSION['pow'] = bin2hex(random_bytes(6));
}

?>

<?php include(__DIR__ . '/header.php') ?>

<div class="container pt-5">
	<div class="row">
		<div class="col-md-8 mx-auto text-center">
			<?php if (isset($_SESSION['flash_success'])) { ?>
				<div class="alert alert-success" role="alert">
					<?= $_SESSION['flash_success'] ?>
				</div>
			<?php
				unset($_SESSION['flash_success']);
			} ?>
			<?php if (isset($_SESSION['flash_error'])) { ?>
				<div class="alert alert-danger" role="alert">
					<?= $_SESSION['flash_error'] ?>
				</div>
			<?php
				unset($_SESSION['flash_error']);
			} ?>
		</div>
	</div>
</div>

<div class="container py-5">
	<div class="row">
		<div class="col-md-8 mx-auto text-center">
			<div class="card">
				<div class="card-body py-4">
					<h1 class="card-title">Welcome to file storage!</h1>
					<form action="" method="POST" class="w-50 mx-auto mt-5">
						<div class="mb-3 text-start">
							<label for="pow" class="form-label">Proof of Work</label>
							<input type="text" class="form-control" id="pow" name="pow">
							<div class="form-text">To create an account you need to solve a PoW with the following command: <kbd>hashcash -mCb<?= POW_BITS ?> "<?= $_SESSION['pow'] ?>"</kbd></div>
						</div>
						<input type="submit" class="btn btn-primary" value="Create account" name="create_account">
					</form>
					<p class="my-5">or</p>
					<form action="" method="POST" class="w-50 mx-auto">
						<div class="mb-3 text-start">
							<label for="username" class="form-label">Username</label>
							<input type="text" class="form-control" id="username" name="username">
						</div>
						<div class="mb-3 text-start">
							<label for="password" class="form-label">Password</label>
							<input type="password" class="form-control" id="password" name="password">
						</div>
						<input type="submit" class="btn btn-primary" value="Login" name="login">
					</form>
				</div>
			</div>
		</div>
	</div>
</div>

<?php include(__DIR__ . '/footer.php') ?>