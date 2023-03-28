package main

import (
	"fmt"
	"math"
)

func solution(n int64) int64 {
	answer := -1

	sqr_num := int64(math.Sqrt(float64(n)))
	if (sqr_num * sqr_num) == n {
		return (int64(sqr_num) + 1) * (int64(sqr_num) + 1)
	}
	return int64(answer)
}

func main() {
	first := solution(121)
	fmt.Print(first)

	first = solution(3)
	fmt.Print(first)
}
