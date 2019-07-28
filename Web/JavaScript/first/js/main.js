/* eslint-disable no-console */
// var name = prompt("what's your name?");

// function show(params) {
//     alert('hello,'+params);
// }

// show(name);


// var maList = ['apples', 'oranges'];

// function show(params) {
//     console.log(params);
// }

// show(maList[0]);
// show(maList[1]);

// maList.forEach(function (first, second) {
//     console.log(first,second);
// })

var numOne = document.getElementById("num-one");
var numTwo = document.getElementById("num-two");
var addSum = document.getElementById("add-sum");

function add() {
    var one = parseFloat(numOne.value) || 0;
    var two = parseFloat(numTwo.value) || 0;

    addSum.innerHTML = 'your sum is ' + (one + two);
}

numOne.addEventListener('input', add);
numTwo.addEventListener('input', add);
