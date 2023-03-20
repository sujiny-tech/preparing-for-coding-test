package main

import (
	"fmt"
)

func solution(common []int) int {
	total := len(common)
	//2023.03.20 결과 : 통과
	num1 := common[0]
	num2 := common[1]
	num3 := common[2]
	if num2-num1 == num3-num2 {
		retrun common[total-1] + (num2-num1)
	}else if num2/num1 == num3/num2 {
		return common[total-1] * (num2/num1)
	}
	return 0
	
	//2023.03.15 결과
	//테스트2 : 런타임에러 발생
	//점수 : 88.9 / 100
	//예외사항 처리 필요함
// 	check1 := common[1] - common[0]
// 	if check1 == 0 {
// 		return common[0]
// 	}
// 	check2 := common[1] / common[0]
// 	flag := true
// 	i := 1
// 	for i < (total - 1) {
// 		if (common[i+1] - common[i]) != check1 {
// 			flag = false
// 			break
// 		}
// 		i = i + 1
// 	}

// 	if flag {
// 		return common[total-1] + check1
// 	} else {
// 		if (total%2 == 0) && check2 < 0 {
// 			return (-1) * common[total-1] * check2
// 		} else {
// 			return common[total-1] * check2
// 		}
// 	}
}

func main() {
	first := []int{1, 2, 3, 4}
	second := []int{2, 4, 8}

	fmt.Println(solution(first))
	fmt.Println(solution(second))
}
