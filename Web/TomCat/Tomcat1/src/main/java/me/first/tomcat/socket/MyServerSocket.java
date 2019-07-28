package me.first.tomcat.socket;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * MyServerSocket
 */
public class MyServerSocket {

    public static void main(String[] args) {
        ServerSocket serverSocket = null;
        Socket clientsoc = null;
        BufferedReader br = null;
        try {
            // 创建服务器套接字，绑定端口号：8080
            serverSocket = new ServerSocket(8080);
            // 创建监听网络，此时程序处于等待消息
            clientsoc = serverSocket.accept();
            // 接收客户端套接字消息
            br = new BufferedReader(new InputStreamReader(clientsoc.getInputStream()));
            String tmp;
            while ((tmp = br.readLine()) != null) {
                System.out.println(tmp);
            }
        } catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (clientsoc != null) {
                try {
                    clientsoc.close();
                } catch (IOException e) {
                    e.printStackTrace();// TODO: handle exception
                }
            }
            if (serverSocket != null) {
                try {
                    serverSocket.close();
                } catch (IOException e) {
                    e.printStackTrace();// TODO: handle exception
                }
            }
        }
    }
}