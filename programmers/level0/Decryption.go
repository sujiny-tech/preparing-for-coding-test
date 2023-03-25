package main

import "fmt"

func solution(cipher string, code int) string {
	answer := ""
	i := code - 1
	for i < len(cipher) {
		answer = answer + string(cipher[i])
		i = i + code
	}
	return answer
}

func main() {
	first := solution("dfjardstddetckdaccccdegk", 4)
	fmt.Println(first)

	first = solution("pfqallllabwaoclk", 2)
	fmt.Println(first)
}
