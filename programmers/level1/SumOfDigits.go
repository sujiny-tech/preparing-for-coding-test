package main

import (
	"fmt"
	"strconv"
)

// solution 1. Using strconv package
func solution(n int) int {
	answer := 0
	str_n := strconv.Itoa(n)

	for i := 0; i < len(str_n); i++ {
		a, _ := strconv.Atoi(string(str_n[i]))
		answer = answer + a
	}
	return answer
}

// solution 2. Using strconv & math package
// func solution(n int) int {
// 	answer := 0
// 	str_n := strconv.Itoa(n)
// 	check := math.Pow(10, float64(len(str_n)-1))

// 	for check >= 1 {
// 		a := n / int(check)
// 		n = n - (int(check) * a)
// 		answer = answer + a
// 		check = check / 10
// 	}

// 	return answer
// }

func main() {
	first := solution(123)
	fmt.Println(first)

	first = solution(987)
	fmt.Println(first)

}
