package main

import (
	"fmt"
	"strconv"
	"strings"
)

func solution(s string) string {
	slice_s := strings.Split(s, " ")

	minnum := string(slice_s[0])
	maxnum := string(slice_s[1])
	for _, num := range slice_s {
		minInt, _ := strconv.Atoi(minnum)
		maxInt, _ := strconv.Atoi(maxnum)
		numInt, _ := strconv.Atoi(num)
		if minInt > numInt {
			minnum = num
		}
		if maxInt < numInt {
			maxnum = num
		}
	}
	return minnum + " " + maxnum
}

func main() {
	first := solution("1 2 3 4")
	fmt.Println(first)

	first = solution("-1 -2 -3 -4")
	fmt.Println(first)

	first = solution("-1 -1")
	fmt.Println(first)
}
