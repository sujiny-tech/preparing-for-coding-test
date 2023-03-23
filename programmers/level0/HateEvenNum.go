package main

import "fmt"

func solution(n int) []int {
	answer := []int{}
	for i := 1; i <= n; i += 2 {
		if i%2 != 0 {
			answer = append(answer, i)
		}
	}
	return answer
}

func main() {
	first := solution(10)
	fmt.Println(first)
	first = solution(15)
	fmt.Println(first)
}
