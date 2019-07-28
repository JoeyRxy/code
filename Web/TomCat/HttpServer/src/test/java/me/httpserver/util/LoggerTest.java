package me.httpserver.util;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

/**
 * LoggerTest
 */
public class LoggerTest {

    @Test
    public void testLog() {
        Logger.log("hello test");
    }
}