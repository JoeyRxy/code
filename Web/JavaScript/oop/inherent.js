class Father {
    constructor(x) {
        this.x = x;
        this.money(); //在类中使用属性和方法必须加this
    }

    money() {
        console.log(this.x); //在类中使用属性和方法必须加this
    }
}

class Son extends Father {
    constructor(x) {
        super(x);
    }

}

const x = new Son("100");

x.money();