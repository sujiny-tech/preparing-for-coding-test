package main

import "fmt"

func solution(hp int) int {
	level5 := hp / 5
	level3 := (hp - 5*level5) / 3
	level1 := (hp - 5*level5 - 3*level3) / 1

	return level5 + level3 + level1
}

func main() {
	first := solution(23)
	fmt.Println(first)

	first = solution(24)
	fmt.Println(first)

	first = solution(999)
	fmt.Println(first)
}
