package main

import "fmt"

func solution(sides []int) int {
	a := len(sides)
	temp := 0
	answer := 2
	for i := 0; i < a; i++ {
		for j := i + 1; j < a; j++ {
			if sides[i] > sides[j] {
				temp = sides[i]
				sides[i] = sides[j]
				sides[j] = temp
			}
		}
	}
	for i := 0; i < (a / 2); i++ {
		if sides[i]+sides[i+1] > sides[a-i-1] {
			answer = 1
			break
		}
	}
	return answer
}

func main() {
	first := solution([]int{1, 2, 3})
	fmt.Println(first)
	first = solution([]int{3, 6, 2})
	fmt.Println(first)
	first = solution([]int{199, 72, 222})
	fmt.Println(first)
}
