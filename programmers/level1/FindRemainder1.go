package main

import "fmt"

func solution(n int) int {

	for i := 1; i <= n; i++ {
		if n%i == 1 {
			return i
		}
	}
	return 0
}

func main() {
	first := solution(10)
	fmt.Println(first)

	first = solution(12)
	fmt.Println(first)
}
