/*
Problem 41:
We shall say that an -digit number is pandigital if it makes use of all the digits to exactly once. For example, is a -digit pandigital and is also prime. What is the largest -digit pandigital prime that exists?
*/

package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func isPrime(num int) (res bool) {
	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return
		}
	}
	return true
}

// 9 and 8 digit numbers are always divisible by 3 so we check 7 digit numbers are the biggest numbers.
func isPandigital(num int) (res bool) {
	var x []string = []string{"1", "2", "3", "4", "5", "6", "7"}
	for _, e := range x {
		if !strings.Contains(strconv.Itoa(num), e) {
			return false
		}
	}
	return true
}

func main() {
	for i := 7654321; i >= 1234567; i-- {
		if isPandigital(i) {
			if isPrime((i)) {
				fmt.Println(i)
				break
			}
		}
	}
}
