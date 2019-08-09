/* eslint-disable no-console */
/* eslint-disable no-unused-vars */
class Point {

    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.Amp = Math.sqrt(x ** 2 + y ** 2);
        this.Angle = Math.atan(y / x);
    }

    toExp() {
        return this.Amp + "Exp(j " + this.Angle + ")";
    }
}

let p;

function demo() {
    p = new Point(parseInt(document.getElementById("x").innerText, 10), parseInt(document.getElementById("y").innerText, 10));
}

function change() {
    document.getElementById("out").innerHTML = p.toExp();
}