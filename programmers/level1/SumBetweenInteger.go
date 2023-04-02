package main

import "fmt"

func solution(a int, b int) int64 {
	if a == b {
		return int64(b)
	} else if a > b {
		answer := 0
		for i := b; i <= a; i++ {
			answer = answer + i
		}
		return int64(answer)
	} else {
		answer := 0
		for i := a; i <= b; i++ {
			answer = answer + i
		}
		return int64(answer)
	}
}
func main() {
	first := solution(3, 5)
	fmt.Println(first)

	first = solution(3, 3)
	fmt.Println(first)

	first = solution(5, 3)
	fmt.Println(first)

}
