package me.first.tomcat.socket;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;

/**
 * MyClinetSocket
 */
public class MyClinetSocket {

    public static void main(String[] args) {
        Socket clinetSocket = null;
        PrintWriter out = null;
        try {
            // 创建客户端套接字
            clinetSocket = new Socket("localhost", 8080);
            // 创建输入流对象
            out = new PrintWriter(clinetSocket.getOutputStream());
            // 消息
            String message = "Hello world";
            // 传输消息
            out.print(message);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // 关闭资源
            if (out != null) {
                out.close();
            }
            if (clinetSocket != null) {
                try {
                    clinetSocket.close();
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        }
    }
}