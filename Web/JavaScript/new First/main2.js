/* eslint-disable no-undef */
// 创建对象
// people = new Object();
// people.name = "john";
// people.age = 30;
// document.write("name:" + people.name + "age:" + people.age)
// /**
//  * 
//  * @param {String} x a string
//  * @param {String} y another String
//  */
// function my(x, y) {
//     document.write(x + y);
// }
// my("fuck", "you");
class people {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

son = new people("fuck", 200);

document.write("name : " + son.name + ", age: " + son.age);