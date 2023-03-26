package main

import "fmt"

func solution(arr []int) float64 {
	total := 0.0

	for i := 0; i < len(arr); i++ {
		total = total + float64(arr[i])
	}
	return total / float64(len(arr))
}

func main() {
	first := solution([]int{1, 2, 3, 4})
	fmt.Println(first)

	first = solution([]int{5, 5})
	fmt.Println(first)

}
