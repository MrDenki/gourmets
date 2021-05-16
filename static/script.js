var doc = document.select_ing_form.i1
doc.addEventListener("click", writeData);
function writeData(e) {
    var data1 = document.select_ing_form.select_ing
    var data2 = document.select_ing_form.write_ing
    data1.value=324
    data2.value = "Все херня"
}