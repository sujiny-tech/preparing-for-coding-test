package main

import "fmt"

//soltuion 1. mapping charaters
// func solution(my_string string) string {
// 	answer := ""
// 	check := map[string]string{"a": "A", "b": "B",
// 		"c": "C", "d": "D", "e": "E", "f": "F",
// 		"g": "G", "h": "H", "i": "I", "j": "J", "k": "K", "l": "L", "m": "M", "n": "N",
// 		"o": "O", "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z",
// 		"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f",
// 		"G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l",
// 		"M": "m", "N": "n", "O": "o", "P": "p",
// 		"Q": "q", "R": "r", "S": "s", "T": "t",
// 		"U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z"}
// 	for i := 0; i < len(my_string); i++ {
// 		answer = answer + check[string(my_string[i])]
// 	}
// 	return answer
// }

//soltuion 2. Using ASCII-code
func solution(my_string string) string {
	answer := ""
	for i := 0; i < len(my_string); i++ {
		if my_string[i] > 91 {
			answer = answer + string(my_string[i]-32)
		} else {
			answer = answer + string(my_string[i]+32)
		}
	}
	return answer
}
func main() {
	first := solution("cccCCC")
	fmt.Println(first)

	first = solution("abCdEfghIJ")
	fmt.Println(first)
}
