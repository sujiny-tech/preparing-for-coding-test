package main

import "fmt"

func solution(phone_number string) string {
	len_num := len(phone_number) - 5
	answer := ""
	for i := 0; i <= len_num; i++ {
		answer = answer + "*"
	}
	answer = answer + phone_number[len_num+1:]
	return answer
}

func main() {
	first := solution("01033334444")
	fmt.Println(first)

	first = solution("027778888")
	fmt.Println(first)

}
