package main

import (
	"fmt"
	"math"
	"strconv"
)

func solution(x int) bool {
	check := x
	a := strconv.Itoa(x)
	len_a := len(a) //자릿수
	num := int(math.Pow(10.0, float64(len_a-1)))
	sum_x_digit := 0 //sum
	digit := 0       //digit
	for num >= 1 {
		digit = x / num
		sum_x_digit = sum_x_digit + digit
		x = x - (num * digit)
		num = num / 10
	}

	if check%sum_x_digit == 0 {
		return true
	}
	return false
}

func main() {
	first := solution(10)
	fmt.Println(first)

	first = solution(12)
	fmt.Println(first)

	first = solution(11)
	fmt.Println(first)

	first = solution(13)
	fmt.Println(first)
}
