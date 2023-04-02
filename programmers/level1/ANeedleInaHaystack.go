package main

import "fmt"

func solution(seoul []string) string {
	answer := ""
	for index, str := range seoul {
		if str == "Kim" {
			answer = fmt.Sprintf("김서방은 %d에 있다", index)
			break
		}
	}
	return answer
}
func main() {
	first := solution([]string{"Jane", "Kim"})
	fmt.Println(first)
}
