package main

import "fmt"

func solution(num int) string {
	if num%2 == 0 {
		return "Even"
	}
	return "Odd"
}

func main() {
	first := solution(3)
	fmt.Println(first)

	first = solution(4)
	fmt.Println(first)

}
