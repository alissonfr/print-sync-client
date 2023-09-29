const usernameInput = document.getElementById('username');
const submitButton = document.getElementById('button');
const error = document.getElementById('error');
usernameInput.addEventListener('input', validateUsername);

let isValid = false;
function validateUsername() {
    const usernameValue = usernameInput.value;
    error.innerHTML = '';

    if (!usernameValue) {
        return setError('Campo obrigatório.');
    }

    if (/[^a-zA-Z0-9]/.test(usernameValue)) {
        return setError('O nome de usuário não deve conter caracteres especiais ou espaços.');
    }

    if (usernameValue.length > 20) {
        return setError('O nome de usuário deve conter no máximo 20 caracteres.');
    }

    isValid = true;
}

function setError(message) {
    error.innerHTML = `&#9888; ${message}`;
    isValid = false;
}

submitButton.addEventListener('click', function() {
    event.preventDefault();
    if (isValid) return onSubmit();
});


function onSubmit() {
    const username = document.getElementById('username').value;
    window.pywebview.api.init_connection(username)
}