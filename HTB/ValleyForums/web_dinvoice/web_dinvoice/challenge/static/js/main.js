$(document).ready(function() {
	$('#create-btn').on('click', showForm);
	$('#save-btn').on('click', addInvoice);
    $('#edit-save-btn').on('click', editInvoice);

    $('.edit-btn').on('click', function(){
        showEdit($(this).data('invoiceId'));
    });
    $('.del-btn').on('click', function(){
        removeInvoice($(this).data('invoiceId'));
    });
    $('.cancel-btn').on('click', showMain);

	window.easyMDE = new EasyMDE({element: $('#markdown_content')[0], renderingConfig: {singleLineBreaks: false},autofocus: true});
    window.editMDE = new EasyMDE({element: $('#edit_md_content')[0], renderingConfig: {singleLineBreaks: false},autofocus: true});

});

const showMain = () => {
    $('#invoices_view').slideDown();
    $('#edit_markdown_view').slideUp();
	$('#markdown_view').slideUp();
}

const showForm = () => {
	$('#invoices_view').slideUp();
	$('#markdown_view').slideDown();
}

const showEdit = async (invoice) => {
    await fetch(`/invoice/markdown/${invoice}.md`, {
		method: 'GET',
		credentials: 'include',
	})
	.then(async (response) => {
		if (response.status == 200) {
            resData = await response.json();
            window.editMDE.value(resData.content);
        }
        else {
            window.editMDE.value('Invoice content not found!');
        }
        $('#invoices_view').slideUp();
	    $('#edit_markdown_view').slideDown();
        $('#invoice-id').val(invoice);
	})
	.catch((error) => {
		console.log(error);
	});
}

const removeInvoice = async (invoice) => {
	await fetch('/api/invoice/delete', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({invoice}),
	})
	.then((response) => {
		location.reload();
	})
	.catch((error) => {
		console.log(error);
	});
}

const addInvoice = async () => {

	$('#save-btn').prop('disabled', true);

	let card = $('#resp-msg');
	card.hide();

	let loading = $('#loading_view');
	loading.show();
	$('.pdf_frame').hide();

	let markdown_content = window.easyMDE.value();

	if ($.trim(markdown_content) === '') {
		$('#save-btn').prop('disabled', false);
		card.text('Please add some content first!');
		card.attr('class', 'alert alert-danger');
		card.show();
		loading.hide();
		return;
	}

	await fetch('/api/invoice/add', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({markdown_content}),
		})
		.then((response) => response.json()
			.then((data) => {
				if (response.status == 200) {
					window.setTimeout(function() {
						loading.hide();
						location.reload();
						}, 2500);
						return;
				} else {
					loading.hide();
					card.text(data.message);
					card.attr('class', 'alert alert-danger');
					card.show();
				}
			}))
		.catch((error) => {
			loading.hide();
			card.text(error);
			card.attr('class', 'alert alert-danger');
			card.show();
            $('#save-btn').prop('disabled', false);
		});
}

const editInvoice = async () => {

	$('#edit-save-btn').prop('disabled', true);

	let card = $('#resp-msg');
	card.hide();

	let loading = $('#loading_view');
	loading.show();
	$('.pdf_frame').hide();

	let markdown_content = window.editMDE.value();
    let invoice = $('#invoice-id').val();

	if ($.trim(markdown_content) === '') {
		$('#edit-save-btn').prop('disabled', false);
		card.text('Please add some content first!');
		card.attr('class', 'alert alert-danger');
		card.show();
		loading.hide();
		return;
	}

	await fetch('/api/invoice/update', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({markdown_content, invoice}),
		})
		.then((response) => response.json()
			.then((data) => {
				if (response.status == 200) {
					window.setTimeout(function() {
						loading.hide();
						location.reload();
						}, 2500);
						return;
				} else {
					loading.hide();
					card.text(data.message);
					card.attr('class', 'alert alert-danger');
					card.show();
				}
			}))
		.catch((error) => {
			loading.hide();
			card.text(error);
			card.attr('class', 'alert alert-danger');
			card.show();
            $('#edit-save-btn').prop('disabled', false);
		});
}
