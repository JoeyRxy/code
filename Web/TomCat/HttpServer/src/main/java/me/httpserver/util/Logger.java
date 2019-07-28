package me.httpserver.util;

import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Logger
 */
public class Logger {
    /**
     * 日志记录
     * 
     * @param msg
     */
    public static void log(String msg) {
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss SSS");
        Date nowTime = new Date();
        String nowTimeStr = dateFormat.format(nowTime);
        System.out.println("[info]" + nowTimeStr + "\t" + msg);
    }

}