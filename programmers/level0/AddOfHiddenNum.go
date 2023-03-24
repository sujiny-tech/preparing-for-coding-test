package main

import (
	"fmt"
	"strconv"
)

func solution(my_string string) int {
	numberlist := []string{"1", "2", "3", "4", "5", "6", "7", "8", "9"}
	answer := 0
	for i := 0; i < len(my_string); i++ {
		for j := 0; j < 9; j++ {
			if string(my_string[i]) == numberlist[j] {
				num, _ := strconv.Atoi(string(my_string[i]))
				answer = answer + num
			}
		}
	}
	return answer
}

func main() {
	first := solution("aAb1B2cC34oOp")
	fmt.Println(first)
	first = solution("1a2b3c4d123")
	fmt.Println(first)

}

//숨어있는 숫자의 덧셈(1)
