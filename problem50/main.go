/*
problem 50
The prime , can be written as the sum of six consecutive primes: This is the longest sum of consecutive primes that adds to a prime below one-hundred. The longest sum of consecutive primes below one-thousand that adds to a prime, contains terms, and is equal to . Which prime, below one-million, can be written as the sum of the most consecutive primes?
*/
package main

import (
	"fmt"
	"math"
)

func isPrime(x int) (res bool) {
	for i := 2; i <= int(math.Sqrt(float64(x))); i++ {
		if x%i == 0 {
			return false
		}
	}
	return true
}

func primesUnderMillion() []int {
	var res []int = []int{}
	for i := 2; i < 1000000; i++ {
		if isPrime(i) {
			res = append(res, i)
		}
	}
	return res
}

func main() {
	x := primesUnderMillion()
	final := 0
	r := 0
	for _, e := range x {
		y := filter(x, e)
		s := e
		count := 1
		for _, e2 := range y {
			s += e2
			count++
			if s > 1000000 {
				break
			}
			if isPrime(s) {
				if count > final {
					final = count
					r = s
				}
			}

		}
	}
	fmt.Println(final)
	fmt.Println(r)
}

func filter(x1 []int, x2 int) (res []int) {
	for _, e := range x1 {
		if e > x2 {
			res = append(res, e)
		}
	}
	return res
}
