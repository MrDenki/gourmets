
var search = document.si_form
var textar = document.si_form.write_ing
search.addEventListener("click", searchFunction)
function searchFunction(e) {
    var target1 = e.target
    switch (target1.name) {
        case "i1":
            textar.value = "Молочные продукты";
            break;
        case "i2":
            textar.value = "Крупы";
            break;
        case "i3":
            textar.value = "Овощи";
            break;
        case "i4":
            textar.value = "Специи";
            break;
        case "i5":
            textar.value = "Мясо";
            break;
        case "i6":
            textar.value = "Напитки";
            break;
        case "i7":
            textar.value = "Макароны";
            break;
        case "i8":
            textar.value = "Фрукты";
            break;
    }
}