package main

import "fmt"

func solution(num int) int {
	answer := 0
	if num == 1 {
		return 0
	}
	for num != 1 {
		if num%2 == 0 {
			num = num / 2
		} else {
			num = num*3 + 1
		}
		answer += 1
		if answer >= 500 {
			answer = -1
			break
		}
	}
	return answer
}
func main() {
	first := solution(6)
	fmt.Println(first)

	first = solution(16)
	fmt.Println(first)

	first = solution(626331)
	fmt.Println(first)

}
