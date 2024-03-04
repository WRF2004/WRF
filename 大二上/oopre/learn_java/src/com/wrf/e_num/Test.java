package com.wrf.e_num;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n;
        while (scanner.hasNextLine()) {
            n = scanner.nextInt();
            for (int i = 0; i < n; i += 1 ) {
                int a = scanner.nextInt();;
                int b = scanner.nextInt();
                System.out.println(a + b);
            }
        }
    }
}
