package main

import (
	"fmt"
	"math/big"
)

func Fibonacci(n int) *big.Int {
	if n == 0 {
		return big.NewInt(0)
	}
	if n == 1 {
		return big.NewInt(1)
	}
	num1 := big.NewInt(0) //f(0)
	num2 := big.NewInt(1) //f(1)
	result := big.NewInt(0)
	for i := 2; i <= n; i++ {
		result = big.NewInt(0).Add(num1, num2)
		num1 = num2
		num2 = result
	}
	return result
}

func solution(n int) int {
	return int(Fibonacci(n).Mod(Fibonacci(n), big.NewInt(1234567)).Int64())
}

func main() {
	first := solution(3)
	fmt.Println(first)

	first = solution(5)
	fmt.Println(first)
}
