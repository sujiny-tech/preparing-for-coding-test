package main

import "fmt"

func solution(n int) int {
	answer := 0

	for i := 1; i <= n; i++ {
		for j := 1; j <= n; j++ {
			if i*j == n {
				answer = answer + i + j
			}
		}
	}
	return answer / 2
}

func main() {
	first := solution(12)
	fmt.Println(first)

	first = solution(5)
	fmt.Println(first)

}
