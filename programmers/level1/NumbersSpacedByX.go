package main

import "fmt"

func solution(x int, n int) []int64 {
	answer := make([]int64, n)

	answer[0] = int64(x)
	for i := 1; i < n; i++ {
		answer[i] = int64(answer[i-1]) + int64(x)
	}
	return answer
}

func main() {
	first := solution(2, 5)
	fmt.Println(first)

	first = solution(4, 3)
	fmt.Println(first)

	first = solution(-4, 2)
	fmt.Println(first)

}
