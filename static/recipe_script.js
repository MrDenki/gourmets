var form = document.form_test;
var btn = form.sended;
alert()
btn.addEventListener("click", sendRequest);
function sendRequest(e) {
    e.preventDefault();
    
    }
    var sends = "nick="+mes.nick + "text="+mes.text;
    request.open("POST","127.0.0.1:8000");
    request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8")
    request.onreadystatechange = reqReadyStateChange;
    request.send(sends);
}