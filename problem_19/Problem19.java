/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.problem19;

/**
 *
 * @author mehradhq
 */
public class Problem19 {

    public static void main(String[] args) {
        int c = 0;
        Date date = new Date(1, 1, 1900, 1);
        while (date.getYear() < 2001) {
            if (date.getWeekday().equals("Sunday") && date.getYear() >= 1901) {
                c++;
            }
            date.addMonth();
        }
        System.out.println(c);
    }
}
