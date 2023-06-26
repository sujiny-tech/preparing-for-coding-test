package main

import "fmt"

func solution(left int, right int) int {

	answer := 0

	for j := left; j <= right; j++ {
		first := 0
		for i := 1; i <= j; i++ {
			if j%i == 0 {
				first = first + 1
			}
		}
		if first%2 == 0 {
			answer = answer + j
		} else {
			answer = answer - j
		}
	}
	return answer
}
func main() {
	ans1 := solution(13, 17)
	fmt.Println("answer1:", ans1)

	ans1 = solution(24, 27)
	fmt.Println("answer2:", ans1)

}
