package main

import "fmt"

func solution(n int) string {
	answer := ""
	for i := 0; i < ((n) / 2); i++ {
		answer = answer + "수박"
	}
	if n%2 == 0 {
		return answer
	} else {
		return answer + "수"
	}
}
func main() {
	first := solution(3)
	fmt.Println(first)

	first = solution(4)
	fmt.Println(first)
}
