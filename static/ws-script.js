var wsLetters = document.getElementsByClassName("ws-letter");
var wsWordsDivs = document.getElementsByClassName("ws-word");
var wsWords = [];
var numberOfWords = wsWordsDivs.length;
var wordsFound = 0;

for (var i=0; i<wsWordsDivs.length; i++) {
    wsWords.push(wsWordsDivs[i].innerHTML);
}

console.log(wsWords);

var startingLetter;
var selected = [];
var selectedWord = "";

const timeBegun = performance.now();
console.log(timeBegun);

var startWord = function(e) {
    var element = e.currentTarget;
    startingLetter = element;
    selected.push(element);
}

var calculateWordBetween = function(e) {
    var wsLetterRectX = [];
    var wsLetterRectY = [];

    for (var i=0; i<wsLetters.length; i++) {
        wsLetterRectX.push(wsLetters[i].getBoundingClientRect().x);
        wsLetterRectY.push(wsLetters[i].getBoundingClientRect().y);
    }

    if (startingLetter == null) { return; }

    var startingRectangle = startingLetter.getBoundingClientRect();
    // startingRectangle.x += window.scrollX;
    // startingRectangle.y += window.scrollY;

    // var endingRectangle = {x: e.clientX, y: e.clientY};
    var endingRectangle = e.currentTarget.getBoundingClientRect();
    var slope = (endingRectangle.y - startingRectangle.y) / (endingRectangle.x - startingRectangle.x);

    var xLeft = Math.min(startingRectangle.x, endingRectangle.x);
    var xRight = Math.max(startingRectangle.x, endingRectangle.x);
    var yBot = Math.min(startingRectangle.y, endingRectangle.y);
    var yTop = Math.max(startingRectangle.y, endingRectangle.y);

    var leftToRight = (startingRectangle.x < endingRectangle.x);
    var topToBottom = (startingRectangle.y < endingRectangle.y);

    selected = [];
    selectedWord = "";

    if (-1/3 <= slope && slope <= 1/3) {
        // horizontal case
        for (var i=0; i<wsLetters.length; i++) {
            if (wsLetterRectY[i] == startingRectangle.y && xLeft <= wsLetterRectX[i] && wsLetterRectX[i] <= xRight) {
                wsLetters[i].classList.add("selected");
                selected.push(wsLetters[i]);
            } else {
                wsLetters[i].classList.remove("selected");
            }
        }

        if (!leftToRight) {
            selected = selected.reverse();
        }
    } else if (-2 <= slope && slope < -1/3) {
        // SW to NE diagonal
        for (var i=0; i<wsLetters.length; i++) {
            if (wsLetterRectX[i] + wsLetterRectY[i] == startingRectangle.x + startingRectangle.y && xLeft <= wsLetterRectX[i] && wsLetterRectX[i] <= xRight) {
                wsLetters[i].classList.add("selected");
                selected.push(wsLetters[i]);
            } else {
                wsLetters[i].classList.remove("selected");
            }
        }

        if (leftToRight) {
            selected = selected.reverse();
        }
    } else if (2 >= slope && slope > 1/3) {
        // NW to SE diagonal
        for (var i=0; i<wsLetters.length; i++) {
            if (wsLetterRectX[i] - wsLetterRectY[i] == startingRectangle.x - startingRectangle.y && xLeft <= wsLetterRectX[i] && wsLetterRectX[i] <= xRight) {
                wsLetters[i].classList.add("selected");
                selected.push(wsLetters[i]);
            } else {
                wsLetters[i].classList.remove("selected");
            }
        }

        if (!leftToRight) {
            selected = selected.reverse();
        }
    } else {
        // vertical
        for (var i=0; i<wsLetters.length; i++) {
            if (wsLetterRectX[i] == startingRectangle.x && yBot <= wsLetterRectY[i] && wsLetterRectY[i] <= yTop) {
                wsLetters[i].classList.add("selected");
                selected.push(wsLetters[i]);
            } else {
                wsLetters[i].classList.remove("selected");
            }
        }

        if (!topToBottom) {
            selected = selected.reverse();
        }
    }

    for (var i=0; i<selected.length; i++) {
        selectedWord += selected[i].innerHTML;
    }

    document.getElementById("word-selected").innerHTML = selectedWord;
}

function endWord() {
    for (var i=0; i<selected.length; i++) {
        selected[i].classList.remove("selected");
    }

    console.log(selectedWord);

    if (wsWords.includes(selectedWord)) {
        var r = Math.floor(Math.random() * 256);
        var g = Math.floor(Math.random() * 256);
        var b = Math.floor(Math.random() * 256);

        console.log(r + "," + g + "," + b)

        for (var i=0; i<selected.length; i++) {
            selected[i].classList.add("correct");
            selected[i].style.background = "rgba(" + r + "," + g + "," + b + ", 0.2)";
        }

        var wordElement = document.getElementById("ws-word_" + selectedWord);
        wordElement.classList.add("dead");
        wordElement.removeAttribute("id");

        wordsFound += 1;

        document.getElementById("word-counter").innerHTML = "words: " + wordsFound + "/" + numberOfWords;

        if (wordsFound == numberOfWords) {
            const timeEnded = performance.now();
            clearInterval(interval);
            alert("congratulations! your time is " + Math.round((timeEnded - timeBegun)/1000) + " seconds");
        }
    }

    startingLetter = null;
    selected = [];
    selectedWord = null;
}

let hoverTimeout;

var endWordOnHover = function(e) {
    hoverTimeout = setTimeout(() => {
        if (wsWords.includes(selectedWord)) {
            endWord();
            console.log('hover timed out on ' + selectedWord);
        }
    }, "100");
}

var cancelHover = function(e) {
    clearTimeout(hoverTimeout);
}

function startTimer() {
    var timeNow = performance.now();
    var timeElapsed = Math.round((timeNow - timeBegun) / 1000); // time in seconds
    var m = padTime(Math.floor(timeElapsed / 60));
    var s = padTime(timeElapsed % 60);
    document.getElementById("timer").innerHTML = m + ":" + s;
}

function padTime(i) {
    if (i < 10) {i = "0" + i;}
    return i;
}

for (var i=0; i<wsLetters.length; i++) {
    wsLetters[i].addEventListener("mousedown", startWord, false);
    wsLetters[i].addEventListener("mouseover", calculateWordBetween, false);
    wsLetters[i].addEventListener("mouseover", endWordOnHover, false);
    wsLetters[i].addEventListener("mouseout", cancelHover, false);
}

// document.addEventListener("mouseover", calculateWordBetween, false);
document.addEventListener("mouseup", endWord, false);

var interval = setInterval(startTimer, 500);
