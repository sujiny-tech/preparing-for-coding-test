package main

import "fmt"

func solution(rsp string) string {
	answer := ""
	winner := map[string]string{"2": "0", "0": "5", "5": "2"}
	for i := 0; i < len(rsp); i++ {
		answer = answer + string(winner[string(rsp[i])])
	}
	return answer
}

func main() {
	first := solution("2")
	fmt.Println(first)

	first = solution("205")
	fmt.Println(first)

}
