package main

import "fmt"

func solution(n int) int {
	answer := 2

	for i := 1; i < 1000000; i++ {
		if i*i == n {
			answer = 1
			break
		} else if i*i > n {
			answer = 2
			break
		}
	}
	return answer
}

func main() {
	first := solution(144)
	fmt.Println(first)

	first = solution(976)
	fmt.Println(first)

}
