var form = document.form_test;
var btn = form.sended;
btn.addEventListener("click", sendRequest);
function sendRequest(e) {
    var mes ={};

    mes.nick = form.i1.value;
    mes.them = form.i2.value;
    mes.text = form.i3.text;
    var request = new XMLHttpRequest();
    function reqReadyStateChange() {
        if (request.readyState == 4 && request.status == 200){
            alert("success!");
        //    либо html (append),
        }
        // else{
        //     alert("fail!");
        // }

    }
    var sends = "nick=" + mes.nick + "&them=" + mes.them + "&text=" + mes.text;
    request.open("GET","127.0.0.1:8000/comment/?" + sends);
    request.onreadystatechange = reqReadyStateChange;
    request.send();
    e.preventDefault();
}