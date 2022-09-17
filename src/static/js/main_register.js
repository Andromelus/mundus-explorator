
function register() {
    user_name = document.getElementById("main_register_user_name").value
    password = document.getElementById("main_register_password").value
    console.debug(user_name, password)
    var xhttp = new XMLHttpRequest()
    xhttp.open("POST", "/register")
    xhttp.setRequestHeader('Content-type', 'application/json')
    let data = {
        password: password,
        user_name: user_name
    }
    xhttp.onload = function () {
        console.log(xhttp.response)
        resp = JSON.parse(xhttp.response)
        var toastLiveExample = document.getElementById('main_toast')
        var toast_content = document.getElementById("main_toast_body")
        if (resp.status == "success") {
            toast_content.innerHTML = "Account created ! Welcome !"
            var toast = new bootstrap.Toast(toastLiveExample)
            toast.show()
        } else {
            toast_content.innerHTML = "An error occured :( "
            var toast = new bootstrap.Toast(toastLiveExample)
            toast.show()
        }
    }
    xhttp.send(JSON.stringify(data))
}
