package main

import "fmt"

func solution(str1 string, str2 string) int {
	checknum := len(str2)
	check := 0
	i := 0
	j := 0

	for i < len(str1) && j < len(str2) {
		if str1[i] == str2[j] {
			check = check + 1
			j = j + 1
			i = i + 1
		} else {
			i = i + 1
			j = 0
			check = 0
		}
		if check == checknum {
			break
		}
	}
	if check >= checknum {
		return 1
	}
	return 2
}

func main() {
	first := solution("ab6CDE443fgh22iJKlmn1o", "6CD")
	fmt.Println(first)

	first = solution("ppprrrogrammers", "pppp")
	fmt.Println(first)

	first = solution("AbcAbcA", "AAA")
	fmt.Println(first)
}

// 문자열 안에 문자열
