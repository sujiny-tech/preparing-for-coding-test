package main

import (
	"fmt"
	"sort"
)

func solution(arr []int, divisor int) []int {
	answer := []int{}
	for i := 0; i < len(arr); i++ {
		if arr[i]%divisor == 0 {
			answer = append(answer, arr[i])
		}
	}

	if len(answer) == 0 {
		return []int{-1}
	}

	sort.Slice(answer, func(i, j int) bool {
		return answer[i] < answer[j]
	})
	return answer
}
func main() {
	first := solution([]int{5, 9, 7, 10}, 5)
	fmt.Println(first)

	first = solution([]int{2, 36, 1, 3}, 1)
	fmt.Println(first)

	first = solution([]int{3, 2, 6}, 10)
	fmt.Println(first)

}
