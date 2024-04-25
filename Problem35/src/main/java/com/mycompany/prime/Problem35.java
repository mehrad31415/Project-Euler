/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.prime;

/**
 *
 * @author mehradhq
 */
public class Problem35 {

    public static void main(String[] args) {
        int c = 0;
        for (int i = 2; i < 1000000; i++) {
            if (circ(i)) {
                c++;
            }
        }
        System.out.println(c);
    }

    public static boolean circ(int num) {
        if (!prime(num)) {
            return false;
        }
        String s = String.valueOf(num);
        String sF = String.valueOf(num);
        while (true) {
            s = gardesh(s);
            if (s.equals(sF)){
                break;
            }
            int newN = Integer.valueOf(s);
            
            if (!prime(newN)) {
                return false;
            }
        }
        return true;
    }
    public static String gardesh(String s){
        char last = s.charAt(s.length()-1);
        char[] s2 = s.toCharArray();
        String newS = ""+last;
        for (int i =0;i<s2.length-1;i++){
            newS+=s2[i];
        }
        return newS;
    }

    public static boolean prime(int num) {
        for (int i = 2; i < Math.sqrt(num) + 1; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
