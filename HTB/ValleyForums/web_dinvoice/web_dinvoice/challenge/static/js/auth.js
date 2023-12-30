$(document).ready(() => {
	// set input events
	$('#login-btn').on('click', () => {
		auth('login')
	});
    $('#register-btn').on('click', () => {
		auth('register')
	});

});

function toggleInputs(state) {
	$("#username").prop("disabled", state);
	$("#password").prop("disabled", state);
	$("#login-btn").prop("disabled", state);
	$("#register-btn").prop("disabled", state);
}


async function auth(intent) {

	toggleInputs(true);

	let card = $("#resp-msg");
	card.attr("class", "alert alert-info");
	card.hide();

	let user = $("#username").val();
	let pass = $("#password").val();

	await fetch(`/api/${intent}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
                username: user,
                password: pass
            }),
		})
		.then((response) => response.json()
			.then((resp) => {
				card.attr("class", "alert alert-danger");
				if (response.status == 200) {
					card.attr("class", "alert alert-success");
                    if (intent == 'login') {
                        window.location.href = '/dashboard';
                    }
				}
				card.text(resp.message);
				card.show();
			}))
		.catch((error) => {
			card.text(error);
			card.attr("class", "alert alert-danger");
			card.show();
		});

	toggleInputs(false);
}