package main

import (
	"fmt"
	"strconv"
)

func solution(s string) int {

	// if string(s[0]) == "-" {
	// 	a, _ := strconv.Atoi(string(s[1:]))
	// 	return (-1) * a
	// } else {
	// 	a, _ := strconv.Atoi(s)
	// 	return a
	// }
	a, _ := strconv.Atoi(s)
	return a
}

func main() {
	first := solution("-1234")
	fmt.Println(first)

	first = solution("1234")
	fmt.Println(first)

}
