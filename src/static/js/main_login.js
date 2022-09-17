function login() {
    user_name = document.getElementById("main_login_user_name").value
    password = document.getElementById("main_login_password").value
    http = new XMLHttpRequest()
    http.open("POST", "/login")
    http.setRequestHeader('Content-type', 'application/json')
    let data = {
        password: password,
        user_name: user_name
    }
    http.onload = function() {
        resp = JSON.parse(http.response)
        var toastLiveExample = document.getElementById('main_toast')
        var toast_content = document.getElementById("main_toast_body")
        if (resp.status == "success") {
            sessionStorage.setItem("session_token", resp.info.token)
            sessionStorage.setItem("session_expires_at", resp.info.expires_at)
            window.location.replace("/game")
        } else {
            console.error(resp)
            toast_content.innerHTML = "An error occured :( "
            var toast = new bootstrap.Toast(toastLiveExample)
            toast.show()
        }
   }

    http.send(JSON.stringify(data))
}