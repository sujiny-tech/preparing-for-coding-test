package main

import (
	"fmt"
	"strconv"
)

func solution(n int64) []int {
	str_n := strconv.Itoa(int(n))
	n_len := len(str_n)
	answer := make([]int, n_len)

	for i := 0; i < n_len; i++ {
		answer[i], _ = strconv.Atoi(string(str_n[n_len-1-i]))
	}
	return answer
}

func main() {
	first := solution(12345)
	fmt.Println(first)
}
