<?php

$opts = ['ftp' => $_SESSION['settings']];
$context = stream_context_create($opts);

function download_file()
{
	global $database, $context;

	try {

		$filename = $_GET['filename'];

		$stmt = $database->prepare('SELECT * FROM files WHERE owner = :owner AND filename = :filename');
		$stmt->execute([
			'owner' => $_SESSION['user'],
			'filename' => $filename
		]);
		$file = $stmt->fetch();

		if (!$file) {
			die('<script>window.close()</script>');
		}

		$ftp = @fopen("ftp://{$_SESSION['user']}:{$_SESSION['password']}@ftp/$filename", 'r', false, $context);

		if (!$ftp) {
			die('<script>window.close()</script>');
		}

		$data = '';

		while (!feof($ftp)) {
			$data .= @fread($ftp, 8192);
		}

		fclose($ftp);


		header('Content-Type: application/octet-stream');
		header('Content-Disposition: attachment; filename="' . urlencode($filename) . '"');
		echo $data;

		exit;
	} catch (Exception $e) {
		die('<script>window.close()</script>');
	}
}

function upload_file()
{
	global $database, $context;

	$filename = $_FILES['file']['name'];

	try {
		$ftp = @fopen("ftp://{$_SESSION['user']}:{$_SESSION['password']}@ftp/$filename", 'w', false, $context);

		if (!$ftp) {
			$_SESSION['flash_error'] = 'Could not upload file';
			return;
		}

		@fwrite($ftp, file_get_contents($_FILES['file']['tmp_name']));

		fclose($ftp);

		$stmt = $database->prepare('SELECT * FROM files WHERE owner = :owner AND filename = :filename');
		$stmt->execute([
			'owner' => $_SESSION['user'],
			'filename' => $filename
		]);
		$file = $stmt->fetch();

		if ($file) {
			$stmt = $database->prepare("UPDATE files SET modify_date=CURRENT_TIMESTAMP, size=:size WHERE owner=:owner AND filename=:filename");

			$stmt->execute([
				'owner' => $_SESSION['user'],
				'filename' => $filename,
				'size' => $_FILES['file']['size']
			]);
		} else {
			$stmt = $database->prepare("INSERT INTO files (owner, filename, size) VALUES (:owner, '$filename', :size)");

			$stmt->execute([
				'owner' => $_SESSION['user'],
				'size' => $_FILES['file']['size']
			]);
		}
	} catch (Exception $e) {
		$_SESSION['flash_error'] = 'Could not upload file';
	}
	header('Location: /');
	exit;
}
