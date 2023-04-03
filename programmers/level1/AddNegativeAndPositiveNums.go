package main

import "fmt"

func solution(absolutes []int, signs []bool) int {
	answer := 0
	for index, check := range signs {
		if check {
			answer = answer + absolutes[index]
		} else {
			answer = answer - absolutes[index]
		}
	}
	return answer
}

func main() {
	first := solution([]int{4, 7, 12}, []bool{true, false, true})
	fmt.Println(first)

	first = solution([]int{1, 2, 3}, []bool{false, false, true})
	fmt.Println(first)
}
