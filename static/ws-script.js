var wsLetters = document.getElementsByClassName("ws-letter");

var highlight = function(e) {
    var element = e.currentTarget;
    element.style.background = "blue";
    element.setAttribute("id", "selected")
    console.log(element.innerHTML);
}

for (var i=0; i<wsLetters.length; i++) {
    document.getElementById("demo").innerHTML += wsLetters[i].innerHTML;
    wsLetters[i].addEventListener("mousedown", highlight, false);

}
