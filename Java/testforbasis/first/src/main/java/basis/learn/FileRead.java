package main.java.basis.learn;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

/**
 * FileRead
 */
public class FileRead {

    public static void main(String[] args) {
        File file = new File(
                "C:\\Users\\RXY\\Documents\\MYCODE\\code\\Java\\testforbasis\\first\\src\\main\\java\\basis\\learn\\file.txt");
        InputStream inputStream = new FileInputStream(file);
        byte[] bytes = inputStream.readAllBytes();
        System.out.println(bytes);
    }
}