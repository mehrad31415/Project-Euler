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
public class Date {

    private int day;
    private int year;
    private int month;
    private int weekday;

    public Date(int day, int month, int year, int weekday) {
        this.day = day;
        this.month = month;
        this.year = year;
        this.weekday = weekday;
    }

    public int getDay() {
        return day;
    }

    public int getMonth() {
        return month;
    }

    public int getYear() {
        return year;
    }

    public String getWeekday() {
        switch (this.weekday) {
            case (1):
                return "Monday";
            case (2):
                return "Tuesday";
            case (3):
                return "Wednesday";
            case (4):
                return "Thursday";
            case (5):
                return "Friday";
            case (6):
                return "Saturday";
            case (7):
                return "Sunday";
            default:
                return "";
        }
    }

    public boolean leapYear() {
        int y = this.year;
        if (y % 400 == 0) {
            return true;
        }
        if (y % 100 == 0) {
            return false;
        }
        if (y % 4 == 0) {
            return true;
        }
        return false;
    }

    public int numberOfDaysInMonth() {
        switch (this.month) {
            case (1):
                return 31;
            case (2):
                if (this.leapYear()) {
                    return 29;
                } else {
                    return 28;
                }
            case (3):
                return 31;
            case (4):
                return 30;
            case (5):
                return 31;
            case (6):
                return 30;
            case (7):
                return 31;
            case (8):
                return 31;
            case (9):
                return 30;
            case (10):
                return 31;
            case (11):
                return 30;
            case (12):
                return 31;
            default:
                return -1;
        }
    }

    public void addMonth() {
        this.changeWeekday();
        if (this.month == 12) {
            this.month = 1;
            this.year++;
        } else {
            this.month++;
        }
    }

    public void changeWeekday() {
        int m = this.numberOfDaysInMonth() % 7;
        this.weekday = this.weekday + m;
        if (this.weekday > 7) {
            this.weekday = this.weekday % 7;
        }
    }
}
