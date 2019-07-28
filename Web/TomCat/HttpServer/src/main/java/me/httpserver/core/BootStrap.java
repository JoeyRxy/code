package me.httpserver.core;

import java.net.ServerSocket;

import me.httpserver.util.Logger;

public class BootStrap {
    /**
     * 
     * @param args
     */
    public static void main(String[] args) {
        start();
    }

    /**
     * 
     */
    public static void start() {
        // 创建服务器端套接字，绑定端口号
        ServerSocket serverSocket;
        try {
            Logger.log("httpserver start");
            serverSocket = new ServerSocket(8080);
        } catch (Exception e) {
            e.printStackTrace();// TODO: handle exception
        }
    }
}
