package main

import (
	"fmt"
	"sort"
	"strconv"
)

func InsertNum(a int, arr []int) []int {
	arr = append(arr, a)
	sort.Slice(arr, func(i, j int) bool {
		return arr[i] < arr[j]
	})
	return arr
}

func solution(operations []string) []int {

	var arr []int
	for _, v := range operations {
		if string(v[0]) == "I" {
			a, _ := strconv.Atoi(v[2:])
			arr = InsertNum(a, arr)
		} else if v == "D -1" && len(arr) != 0 {
			arr = arr[1:]
		} else if v == "D 1" && len(arr) != 0 {
			l_arr := len(arr)
			arr = arr[:l_arr-1]
		}
	}
	if len(arr) == 0 {
		return []int{0, 0}
	} else if len(arr) == 1 {
		return []int{arr[0], 0}
	} else {
		len_arr := len(arr)
		return []int{arr[len_arr-1], arr[0]}
	}
}

func main() {
	fmt.Printf("answer1: %v \n", solution([]string{"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"}))
	fmt.Printf("answer2: %v \n", solution([]string{"I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"}))
}
