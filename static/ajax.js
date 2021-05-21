var form = document.form_test;
var btn = form.sended;
btn.addEventListener("click", sendRequest);
function sendRequest(e) {
    e.preventDefault();
    var mes ={};
    mes.nick = form.i1.value;
    mes.text = form.i2.text;
    var request = new XMLHttpRequest();
    function reqReadyStateChange() {
        if (request.readyState == 4 && request.status == 200){
            alert("success!");
        }
        else{
            alert("fail!" + request.readyState);
        }

    }
    var sends = "nick="+mes.nick + "text="+mes.text;
    request.open("POST","127.0.0.1:8000");
    request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8")
    request.onreadystatechange = reqReadyStateChange;
    request.send(sends);

}