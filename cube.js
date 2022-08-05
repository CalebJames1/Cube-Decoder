let ulText = document.getElementById('1');
let uText = document.getElementById('2');
let urText = document.getElementById('3');
let lText = document.getElementById('4');
let rText = document.getElementById('6');
let dlText = document.getElementById('7');
let dText = document.getElementById('8');
let drText = document.getElementById('9');

let cText = document.getElementById('5');
let e = document.getElementById('piece1');
const radios = document.querySelectorAll('.cubeButtons');
let multiplier = 0;
let outputPresent = false;
for(const radio of radios){
    radio.addEventListener('change', function(event){
        let selectedColor = document.querySelector('input[name="cubeSide"]:checked').value;
        radioHelper(selectedColor);
        ulText.focus();
    });
}

function radioHelper(color){
    multiplier = 0;
    if(color === 'orange'){
        multiplier = 1;
    }else if(color === 'green'){
        multiplier = 2;
    }else if(color === 'red'){
        multiplier = 3;
    }else if(color === 'blue'){
        multiplier = 4;
    }else if(color === 'yellow'){
        multiplier = 5;
    }
    ulText.value = colorConverter(window.getComputedStyle(document.getElementById('piece' + (multiplier * 9 + 1))).backgroundColor);
    uText.value = colorConverter(window.getComputedStyle(document.getElementById('piece' + (multiplier * 9 + 2))).backgroundColor);
    urText.value = colorConverter(window.getComputedStyle(document.getElementById('piece' + (multiplier * 9 + 3))).backgroundColor);
    lText.value = colorConverter(window.getComputedStyle(document.getElementById('piece' + (multiplier * 9 + 4))).backgroundColor);
    cText.value = colorConverter(window.getComputedStyle(document.getElementById('piece' + (multiplier * 9 + 5))).backgroundColor);
    rText.value = colorConverter(window.getComputedStyle(document.getElementById('piece' + (multiplier * 9 + 6))).backgroundColor);
    dlText.value = colorConverter(window.getComputedStyle(document.getElementById('piece' + (multiplier * 9 + 7))).backgroundColor);
    dText.value = colorConverter(window.getComputedStyle(document.getElementById('piece' + (multiplier * 9 + 8))).backgroundColor);
    drText.value = colorConverter(window.getComputedStyle(document.getElementById('piece' + (multiplier * 9 + 9))).backgroundColor);

}

function colorConverter(color){
    if(color === 'rgb(128, 128, 128)'){
        return '';
    }else if(color === 'rgb(255, 255, 255)'){
        return 'W';
    }else if(color === 'rgb(255, 165, 0)'){
        return 'O';
    }else if(color === 'rgb(0, 128, 0)'){
        return 'G';
    }else if(color === 'rgb(255, 0, 0)'){
        return 'R';
    }else if(color === 'rgb(0, 0, 255)'){
        return 'B';
    }else if(color === 'rgb(255, 255, 0)'){
        return 'Y';
    }else{
        return 'hi';
    }
}

for(let box of document.querySelectorAll('.textBox')){
    box.addEventListener('input', function (event) {
        let color = 'gray';
        box.value = box.value.toUpperCase();
        if(box.value === 'W'){
            color = 'white';
        }else if(box.value === 'O'){
            color = 'orange';
        }else if(box.value === 'G'){
            color = 'green';
        }else if(box.value === 'R'){
            color = 'red';
        }else if(box.value === 'B'){
            color = 'blue';
        }else if(box.value === 'Y'){
            color = 'yellow';
        }
        document.getElementById('piece' + (multiplier * 9 + parseInt(box.getAttribute('id')))).style.backgroundColor = color;
        if(box.value != "") {
            box.blur();
            if (box.id === '4') {
                document.getElementById('6').focus();
            } else {
                document.getElementById(parseInt(box.id) + 1 + '').focus();
            }
        }
    });

    document.getElementById('white').checked = true;
}

let clearButton = document.getElementById('clearButton');
clearButton.onclick = (e) => {
    ulText.value = '';
    uText.value = '';
    urText.value = '';
    lText.value='';
    rText.value = '';
    dlText.value = '';
    dText.value = '';
    drText.value = '';
    for(let i = 1; i <= 9; i++) {
        if(i != 5) {
            document.getElementById('piece' + (multiplier * 9 + i)).style.backgroundColor = 'gray';
        }
    }
}


let outputField = document.getElementById('outputField');
let solveButton = document.getElementById('solveButton');
const userAction = async () => {
    let white = '';
    for(let i = 1; i <= 9; i++){
        if(i === 5){
            white += 'w';
        }else {
            let currentPiece = document.getElementById(`piece${i}`);
            white += currentPiece.style.backgroundColor[0];
        }
    }
    let orange = '';
    for(let i = 10; i <= 18; i++){
        if(i === 14){
            orange += 'o';
        }else {
            let currentPiece = document.getElementById(`piece${i}`);
            orange += currentPiece.style.backgroundColor[0];
        }
    }
    let green = '';
    for(let i = 19; i <= 27; i++){
        if(i === 23){
            green += 'g';
        }else {
            let currentPiece = document.getElementById(`piece${i}`);
            green += currentPiece.style.backgroundColor[0];
        }
    }
    let red = '';
    for(let i = 28; i <= 36; i++){
        if(i === 32){
            red += 'r';
        }else {
            let currentPiece = document.getElementById(`piece${i}`);
            red += currentPiece.style.backgroundColor[0];
        }
    }
    let blue = '';
    for(let i = 37; i <= 45; i++){
        if(i === 41){
            blue += 'b';
        }else {
            let currentPiece = document.getElementById(`piece${i}`);
            blue += currentPiece.style.backgroundColor[0];
        }
    }
    let yellow = '';
    for(let i = 46; i <= 54; i++){
        if(i === 50){
            yellow += 'y';
        }else {
            let currentPiece = document.getElementById(`piece${i}`);
            yellow += currentPiece.style.backgroundColor[0];
        }
    }
  let response = await fetch(`https://3nkzvyis50.execute-api.us-east-1.amazonaws.com/test2/cubesolver2?white=${white}&orange=${orange}&green=${green}&red=${red}&blue=${blue}&yellow=${yellow}`);
  let myJson = await response.json(); //extract JSON from the http response
    if(myJson['error']){
        alert(myJson['error']);
    }else {
        let crossButton = document.getElementById("crossButton");
        let flButton = document.getElementById("flButton");
        let slButton = document.getElementById("slButton");
        let llButton = document.getElementById("llButton");
        if(!outputPresent) {
            let tabs = document.getElementById("tabs");
            tabs.style.visibility = "visible";
            outputPresent = true;
        }
        crossButton.onclick = function () {
                outputSection(crossButton, 'cross')
            };
        flButton.onclick = function () {
                outputSection(flButton, 'first layer')
            };
        slButton.onclick = function () {
                outputSection(slButton, 'second layer')
            };
        llButton.onclick = function () {
                outputSection(llButton, 'last layer')
            };
        crossButton.click();
    }


function outputSection(evt, sectionName) {
  // Declare all variables
  let i, tabcontent, tablinks;
    let outputField = document.getElementById("outputField");
  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tabLinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  evt.className += " active";

  if(sectionName === "cross"){
      outputField.innerText = myJson['cross'];
  }else if(sectionName === "first layer"){
      outputField.innerText = myJson['corners'];
  }else if(sectionName === "second layer"){
      outputField.innerText = myJson['second layer'];
  }else if(sectionName === "last layer"){
      outputField.innerText = myJson['last layer'];
  }
}
}
solveButton.addEventListener('click', userAction);
