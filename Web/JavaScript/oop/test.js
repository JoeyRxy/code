class Star {
    constructor(u) {
        this.u = u;
    }

    //不需要function关键词
    sing(song) {
        console.log(this.u + " is singing " + song);

    }

}

const x = new Star("rxy");
console.log(x.u);

x.sing("happy birthday to you");