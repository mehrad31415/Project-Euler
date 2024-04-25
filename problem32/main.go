package main

/*
problem 32
We shall say that an -digit number is pandigital if it makes use of all the digits to exactly once; for example, the -digit number, , is through pandigital. The product is unusual, as the identity, , containing multiplicand, multiplier, and product is through pandigital. Find the sum of all products whose multiplicand/multiplier/product identity can be written as a through pandigital. HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
*/
/*
9
x1 + x2 + x3 = 9
x1, x2, x3 > 0
x1 = 1, x2 = 1, x3 = 7 Invalid 9 * 9 = 81
x1 = 1, x2 = 2, x3 = 6 Invalid 9 * 99 = 891
x1 = 1, x2 = 3, x3 = 5 Invalid 9 * 999 = 8991
x1 = 1, x2 = 5, x3 = 3 Invalid 1 * 11111 = 111
x1 = 1, x2 = 6, x3 = 2 Invalid 1 * 111111 = 111111
x1 = 1, x2 = 7, x3 = 1 Invalid 1 * 1111111 = 1111111
x1 = 2, x2 = 1, x3 = 6 Invalid 99 * 9 = 891
x1 = 2, x2 = 2, x3 = 5 Invalid 99 * 99 = 9801
x1 = 2, x2 = 4, x3 = 3 Invalid
x1 = 2, x2 = 5, x3 = 2 Invalid
x1 = 2, x2 = 6, x3 = 1 Invalid
x1 = 3, x2 = 1, x3 = 5 Invalid 99 * 9 = 8991
x1 = 3, x2 = 3, x3 = 3 Invalid 111 * 111 = 12321
x1 = 3, x2 = 4, x3 = 2 Invalid
x1 = 3, x2 = 5, x3 = 1 Invalid
x1 = 4, x2 = 2, x3 = 3 Invalid
x1 = 4, x2 = 3, x3 = 2 Invalid
x1 = 4, x2 = 4, x3 = 1 Invalid
x1 = 5, x2 = 1, x3 = 3 Invalid
x1 = 5, x2 = 2, x3 = 2 Invalid
x1 = 5, x2 = 3, x3 = 1 Invalid
x1 = 6, x2 = 1, x3 = 2 Invalid
x1 = 6, x2 = 2, x3 = 1 Invalid
x1 = 7, x2 = 1, x3 = 1 Invalid

x1 = 1, x2 = 4, x3 = 4 valid
x1 = 2, x2 = 3, x3 = 4 valid
*/

import (
	"fmt"
	"strconv"
	"strings"
)

func distinctElems(x int) bool {
	var s string = strconv.Itoa(x)
	var res string = ""
	for _, e := range s {
		if !strings.Contains(res, string(e)) {
			res += string(e)
		}
	}
	if len(res) == len(s) {
		return true
	}
	return false
}

func hasZero(j int) bool {
	var s string = strconv.Itoa(j)
	for _, e := range s {
		if string(e) == "0" {
			return true
		}
	}
	return false
}

// x1 = 1, x2 = 4, x3 = 4 valid
func pandigital() []int {
	var acc []int = []int{}
	for i := 1; i < 10; i++ {
		for j := 1000; j < 10000; j++ {
			if !distinctElems(j) || hasZero(j) {
				continue
			}
			x := strconv.Itoa(i)
			y := strconv.Itoa(j)
			if strings.Contains(y, x) {
				continue
			}
			res := i * j
			if !distinctElems(res) || hasZero(res) {
				continue
			}
			z := strconv.Itoa(res)
			if len(z) != 4 {
				continue
			}
			if strings.Contains(z, x) {
				continue
			}
			if distinct(z, y) {
				fmt.Println(x, y, z)
				acc = append(acc, res)
			}
		}
	}
	return acc
}

func distinct(x, y string) bool {
	for _, e1 := range x {
		for _, e2 := range y {
			if e1 == e2 {
				return false
			}
		}
	}
	return true
}

// x1 = 2, x2 = 3, x3 = 4 valid
func pandigital2() []int {
	var acc []int = []int{}
	for i := 10; i < 100; i++ {
		if !distinctElems(i) || hasZero(i) {
			continue
		}
		for j := 100; j < 1000; j++ {
			if !distinctElems(j) || hasZero(j) {
				continue
			}
			x := strconv.Itoa(i)
			y := strconv.Itoa(j)
			if !distinct(y, x) {
				continue
			}
			res := i * j
			if !distinctElems(res) || hasZero(res) {
				continue
			}
			z := strconv.Itoa(res)
			if len(z) != 4 {
				continue
			}
			if !distinct(z, x) {
				continue
			}
			if distinct(z, y) {
				fmt.Println(x, y, z)
				acc = append(acc, res)
			}
		}
	}
	return acc
}

func main() {
	x := append(pandigital(), pandigital2()...)
	x = unique(x)
	fmt.Println(sum(x))
}

func sum(acc []int) (s int) {
	for _, e := range acc {
		s += e
	}
	return
}

func unique(acc []int) []int {
	var visited []int = []int{}
	for _, e := range acc {
		if !contain(visited, e) {
			visited = append(visited, e)
		}
	}
	return visited
}

func contain(visited []int, e int) bool {
	for _, ele := range visited {
		if ele == e {
			return true
		}
	}
	return false
}
