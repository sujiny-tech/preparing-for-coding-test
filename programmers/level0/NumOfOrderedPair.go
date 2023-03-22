package main

import "fmt"

func solution(n int) int {
	answer := 0
	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			if i*j == n {
				answer = answer + 1
			} else if i*j > n {
				break
			}
		}
	}

	return answer
}

func main() {
	first := solution(20)
	fmt.Println(first)
	first = solution(100)
	fmt.Println(first)
}
