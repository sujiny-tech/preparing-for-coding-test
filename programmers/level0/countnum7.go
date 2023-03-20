package main

import "fmt"

func solution(array []int) int {
	answer := 0
	i := 0

	for i < len(array) {
		a := array[i] / 10000
		array[i] = array[i] - (10000 * a)
		b := array[i] / 1000
		array[i] = array[i] - (1000 * b)
		c := array[i] / 100
		array[i] = array[i] - (100 * c)
		d := array[i] / 10
		array[i] = array[i] - (10 * d)
		e := array[i]
		if a == 7 {
			answer = answer + 1
		}
		if b == 7 {
			answer = answer + 1
		}
		if c == 7 {
			answer = answer + 1
		}
		if d == 7 {
			answer = answer + 1
		}
		if e == 7 {
			answer = answer + 1
		}
		i = i + 1
	}
	return answer
}

func main() {
	first := solution([]int{7, 77, 17})
	fmt.Println(first)
	second := solution([]int{10, 29})
	fmt.Println(second)

}
