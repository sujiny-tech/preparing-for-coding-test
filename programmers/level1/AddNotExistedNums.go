package main

import "fmt"

func solution(numbers []int) int {

	answer := 0

	for i := 0; i < 10; i++ {
		flag := false
		for j := 0; j < len(numbers); j++ {
			if i == numbers[j] {
				flag = true
				break
			}
		}
		if !flag {
			answer = answer + i
		}

	}

	return answer
}

func main() {
	first := solution([]int{1, 2, 3, 4, 6, 7, 8, 0})
	fmt.Println(first)

	first = solution([]int{5, 8, 4, 0, 6, 7, 9})
	fmt.Println(first)
}
