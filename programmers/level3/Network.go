package main

import "fmt"

func DFS(n int, com [][]int, i int, visit []int) {
	visit[i] = 1
	for j := 0; j < n; j++ { //look-up linked point, and not visited point
		if j != i && com[j][i] == 1 && visit[j] == 0 {
			DFS(n, com, j, visit) //and look-up for linked point...
		}
	}
	//terminated ... if it not existed another linked point
}
func solution(n int, computers [][]int) int {
	// initialize visitList
	visited := []int{}
	for i := 0; i < n; i++ {
		visited = append(visited, 0)
	}

	answer := 0
	for i, _ := range computers {
		if visited[i] == 0 { //sequentially look-up
			DFS(n, computers, i, visited)
			answer = answer + 1
		}
	}

	return answer
}

func main() {
	fmt.Println("answer1 : ", solution(3, [][]int{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}}))
	fmt.Println("answer2 : ", solution(3, [][]int{{1, 1, 0}, {1, 1, 1}, {0, 1, 1}}))
}
