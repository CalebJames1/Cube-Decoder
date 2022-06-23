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
for(const radio of radios){
    radio.addEventListener('change', function(event){
        let selectedColor = document.querySelector('input[name="cubeSide"]:checked').value;
        radioHelper(selectedColor);
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
        return 'w';
    }else if(color === 'rgb(255, 165, 0)'){
        return 'o';
    }else if(color === 'rgb(0, 128, 0)'){
        return 'g';
    }else if(color === 'rgb(255, 0, 0)'){
        return 'r';
    }else if(color === 'rgb(0, 0, 255)'){
        return 'b';
    }else if(color === 'rgb(255, 255, 0)'){
        return 'y';
    }else{
        return 'hi';
    }
}

for(let box of document.querySelectorAll('.textBox')){
    box.addEventListener('input', function (event) {
        let color = 'gray';
        if(box.value === 'w'){
            color = 'white';
        }else if(box.value === 'o'){
            color = 'orange';
        }else if(box.value === 'g'){
            color = 'green';
        }else if(box.value === 'r'){
            color = 'red';
        }else if(box.value === 'b'){
            color = 'blue';
        }else if(box.value === 'y'){
            color = 'yellow';
        }
        document.getElementById('piece' + (multiplier * 9 + parseInt(box.getAttribute('id')))).style.backgroundColor = color;
        box.blur();
        if(box.id === '4'){
            document.getElementById('6').focus();
        }else {
            document.getElementById(parseInt(box.id) + 1 + '').focus();
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

