package main

import (
	"fmt"
)

func solution(array []int) int {
	a := len(array)
	temp := 0
	for i := 0; i < a; i++ {
		for j := i + 1; j < a; j++ {
			if array[i] > array[j] {
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
			}
		}
	}
	return array[((a+1)/2)-1]
}

func main() {
	first := solution([]int{1, 2, 7, 10, 11})
	fmt.Println(first)
	first = solution([]int{9, -1, 0})
	fmt.Println(first)
}
