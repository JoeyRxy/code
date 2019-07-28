package m.FFT;

public class Complex {

    public double re;
    public double im;

    public Complex() {
        this.re = 0;
        this.im = 0;
    }

    public Complex(double re, double im) {
        this.re = re;
        this.im = im;
    }

    /**
     * 复数乘法
     * 
     * @param o
     * @return
     */
    public Complex product(Complex o) {
        Complex res = new Complex(o.re * this.re - o.im * this.im, o.re * this.im + o.im * this.re);
        return res;
    }

    /**
     * 加法
     * 
     * @param o
     * @return
     */
    public Complex plus(Complex o) {
        Complex res = new Complex(o.re + this.re, o.im + this.im);
        return res;
    }

    /**
     * 减法
     * 
     * @param o
     * @return
     */
    public Complex minus(Complex o) {
        Complex res = new Complex(this.re - o.re, this.im - o.im);
        return res;
    }

    /**
     * X的共轭
     * 
     * @return X的共轭
     */
    public Complex conjugate() {
        return new Complex(re, -im);
    }

    @Override
    public String toString() {
        String s;
        if (im < 0)
            s = re + " - " + (-im) + " j";
        else if (im == 0)
            s = re + "\t";
        else if (re == 0)
            s = "\t" + im + "i";
        else
            s = re + " + " + im + " j";
        return s;
    }
}