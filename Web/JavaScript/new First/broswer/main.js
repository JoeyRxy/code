/* eslint-disable no-unused-vars */
/* eslint-disable no-console */
console.log("Window对象是BOM的核心，window对象是当前浏览器窗口");
console.log("所有js全局对象，函数和变量均是window对象的成员");

console.log("宽度:" + window.innerWidth + ",高度：" + window.innerHeight);

function btnClicked() {
    // window.open("./../index.html");
    // close();//window.close();
    setInterval(function () {
        alert("fuck you");
    }, 3000);
}

//计时器
function getTime() {
    var d = new Date();
    document.getElementById("time").innerHTML = d.toLocaleTimeString();
}
setInterval(function () {
    getTime();
}, 1000);