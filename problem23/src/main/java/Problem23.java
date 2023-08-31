/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author mehradhq
 */
import java.util.ArrayList;

public class Problem23 {

    public static void main(String[] args) {
        int a = 0;
        for (int i = 1; i < 28123; i++) {
            System.out.println(i);
            int count = 0;
            for (int j = 1; j < i; j++) {
                if (abundant(j) && abundant(i - j)) {
                    count = 1;
                    break;
                }
            }
            if (count == 0){
                a+=i;
            }
        }
        System.out.println(a);
    }

    public static int prop(int num) {
        int s = 0;
        for (int i = 1; i < num; i++) {
            if (num % i == 0) {
                s += i;
            }
        }
        return s;
    }

    public static boolean abundant(int num) {
        return prop(num) > num;
    }
}
