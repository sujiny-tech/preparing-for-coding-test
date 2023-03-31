package main

import (
	"fmt"
	"math"
	"strconv"
)

func solution(n int64) int64 {
	str_n := strconv.Itoa(int(n))
	l_str_n := len(str_n) //자릿수
	num := int64(math.Pow(10, float64(l_str_n-1)))

	arr := make([]int64, l_str_n)
	i := 0
	for num >= 1 { //자릿수에 해당하는 수(0~9) 배열에 넣기
		arr[i] = n / num
		n = n - (num * arr[i])
		num = num / 10
		i++
	}
	fmt.Println(arr)
	temp := int64(0)
	for i := 0; i < l_str_n; i++ { //내림차순 Sort
		for j := i + 1; j < l_str_n; j++ {
			if arr[j] > arr[i] {
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp
			}
		}
	}

	fmt.Println(arr)
	i = 0
	answer := int64(0)
	num = int64(math.Pow(10, float64(l_str_n-1)))
	for i < l_str_n { //정수로 바꾸기
		answer = answer + (arr[i] * num)
		i++
		num = num / 10
	}

	return answer
}

func main() {
	first := solution(118372)
	fmt.Println(first)

}
