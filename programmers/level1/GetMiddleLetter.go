package main

import "fmt"

func solution(s string) string {

	if len(s)%2 == 0 {
		index := len(s) / 2
		return string(s[index-1 : index+1])
	} else {
		index := len(s) / 2
		return string(s[index])
	}
}

func main() {
	first := solution("abcde")
	fmt.Println(first)

	first = solution("qwer")
	fmt.Println(first)
}
