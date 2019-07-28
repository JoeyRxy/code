/* eslint-disable no-console */
var x = document.getElementById('btn1');
x.addEventListener('click', hello);

function hello() {
    alert('hello');
    console.log(this);
}

var y = document.getElementsByClassName('edit');
y.item(0).addEventListener('click', f);

function f(){
    alert("f");
}