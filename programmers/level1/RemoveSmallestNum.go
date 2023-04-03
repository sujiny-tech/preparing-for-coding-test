package main

import "fmt"

func solution(arr []int) []int {

	if len(arr) == 1 {
		return []int{-1}
	}
	minnum := arr[0]
	answer := []int{}
	for i := 0; i < len(arr); i++ {
		if minnum > arr[i] {
			minnum = arr[i]
		}
	}

	for i := 0; i < len(arr); i++ {
		if arr[i] == minnum {
			continue
		} else {
			answer = append(answer, arr[i])
		}
	}
	return answer
}

func main() {

	first := solution([]int{4, 3, 2, 1})
	fmt.Println(first)

	first = solution([]int{10})
	fmt.Println(first)
}
