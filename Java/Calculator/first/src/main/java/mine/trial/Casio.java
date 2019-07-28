package mine.trial;

/**
 * Casio
 */
public class Casio {
    private char[] str;

    public Casio(String s) {
        char[] tmp = s.toCharArray();
        str = new char[tmp.length + 100];//多一百个用来存储其他元素
        
    }
}