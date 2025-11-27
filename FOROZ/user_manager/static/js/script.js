function showFunction() {
    var input = document.getElementById("password");
    if (input.type === "password") {
        input.type = "text";
    } else {
        input.type = "password";
    }
}

var passwordInput = document.getElementById("password");
var field = document.getElementById("re-pass");

passwordInput.onkeyup = function () {
    var lowerCaseLetters = /[a-z]/g;
    var upperCaseLetters = /[A-Z]/g;
    var numbers = /[0-9]/g;
    if (passwordInput.value.length < 8) {
        document.getElementById("match").style.color = "#000";
        document.getElementById("match").innerHTML = " - At least 8 characters with standards";
    } else if (passwordInput.value.length >= 8 && passwordInput.value.match(lowerCaseLetters) && passwordInput.value.match(upperCaseLetters) && passwordInput.value.match(numbers)) {
        document.getElementById("match").style.color = "#cccc00";
        document.getElementById("match").innerHTML = " - Now repeat your password";
    }
}

field.onkeyup = function () {
    if (passwordInput != null && passwordInput.value === field.value) {
        document.getElementById("match").style.color = "#00cc66";
        document.getElementById("match").innerHTML = " - Gteate! your password matched";
    }
}