package com.wrf.hello;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("HelloWorld");
        int[] reg = {12, 24, 36};
        System.out.println(reg[0]);
        for (int i =0; i < 3; i++) {
            System.out.print(reg[i]);
        }
    }
}