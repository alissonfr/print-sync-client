function onSubmit() {
    const username = document.getElementById('username').value;
    window.pywebview.api.init_connection(username)
}