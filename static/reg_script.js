var form = document.reg_form
var btn_sub = form.btn_submit
var pass_inp = form.password

btn_sub.addEventListener("click", check_pass)
function check_pass(e) {
    var va = pass_inp
    var ex = 0;
    for (var i = 1; i < pass_inp.value.length; i++) {
        if (pass_inp.value.charAt(i) == pass_inp.value.charAt(i - 1)) {
            ex = 1;
        }
    }
    if (pass_inp.value.length < 8) {
        e.preventDefault();
        alert("Пароль не может быть короче 8 символов")
    }
    if (pass_inp.value.charAt(0) == pass_inp.value.charAt(pass_inp.value.length - 1)) {
        e.preventDefault();
        alert("Первый и последний символ не должны совпадать!")
    }
    if (ex == 1){
        e.preventDefault();
        alert("Символы не должны повторяться подряд!")
    }
}