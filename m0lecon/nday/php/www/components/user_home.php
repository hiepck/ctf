<?php

if (!isset($_SESSION['user'])) {
	die;
}

function humanFileSize($size, $unit = "")
{
	if ((!$unit && $size >= 1 << 30) || $unit == "GB")
		return number_format($size / (1 << 30), 2) . " GB";
	if ((!$unit && $size >= 1 << 20) || $unit == "MB")
		return number_format($size / (1 << 20), 2) . " MB";
	if ((!$unit && $size >= 1 << 10) || $unit == "KB")
		return number_format($size / (1 << 10), 2) . " KB";
	return number_format($size) . " bytes";
}

require_once './components/file_manager.php';

if (isset($_FILES['file'])) {
	upload_file();
}
if (isset($_GET['filename'])) {
	download_file();
}


$stmt = $database->prepare('SELECT * FROM files WHERE owner = :owner');
$stmt->execute(['owner' => $_SESSION['user']]);
$files = $stmt->fetchAll();

?>

<?php include(__DIR__ . '/header.php') ?>

<nav class="navbar bg-primary bg-opacity-50">
	<div class="container-fluid">
		<a class="navbar-brand" href="#">file storage</a>
		<div>
			<div class="form-check form-switch">
				<input class="form-check-input" style="cursor: pointer" type="checkbox" role="switch" id="allowOverwrite" <?= $_SESSION['settings']['overwrite'] ? 'checked' : '' ?>>
				<label class="form-check-label" style="cursor: pointer" for="allowOverwrite">Allow file overwriting</label>
				<script>
					allowOverwrite.onchange = function() {
						console.log(allowOverwrite.checked);
						const formData = new FormData();
						formData.append('settings', JSON.stringify({
							overwrite: allowOverwrite.checked
						}));
						fetch('/', {
							method: 'POST',
							body: formData
						});
					}
				</script>
			</div>
		</div>
	</div>
</nav>

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

<div class="container pt-5">
	<div class="row">
		<div class="col-md-8 mx-auto mt-4">
			<form method="POST" class="d-flex gap-4 justify-content-center align-items-center w-100" enctype="multipart/form-data">
				<label for="file" class="form-label text-nowrap">Upload new file</label>
				<input class="form-control" type="file" id="file" name="file">
				<input type="submit" class="btn btn-primary" value="Upload">
			</form>
		</div>
	</div>
</div>

<div class="container py-5">
	<div class="row">
		<div class="col-12">
			<table class="table table-striped table-hover">
				<thead>
					<tr>
						<th class="bg-primary bg-opacity-50 px-4 py-3" scope="col">Filename</th>
						<th class="bg-primary bg-opacity-50 px-4 py-3" scope="col">Modify date</th>
						<th class="bg-primary bg-opacity-50 px-4 py-3" scope="col">Size</th>
					</tr>
				</thead>
				<tbody>
					<?php
					foreach ($files as $file) {
					?>
						<tr style="cursor: pointer;">
							<td class="px-4 py-3">
								<a href="?filename=<?= urlencode($file->filename) ?>" target="_blank">
									<?= $file->filename ?>
								</a>
							</td>
							<td class="px-4 py-3"><?= $file->modify_date ?></td>
							<td class="px-4 py-3"><?= humanFileSize($file->size) ?></td>
						</tr>
					<?php
					}
					if (count($files) === 0) {
					?>
						<tr>
							<td class="px-4 py-3 text-center fst-italic" colspan="3">No files found</td>
						</tr>
					<?php
					}
					?>
				</tbody>
			</table>
		</div>
	</div>
</div>

<?php include(__DIR__ . '/footer.php') ?>