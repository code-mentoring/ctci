package main

import "fmt"

/* 1.8 - Zero Matrix:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0. */

func main() {
	matrix := [][]int{
		{1, 2, 0},
		{4, 5, 6},
		{7, 8, 9},
	}

	zeroMatrix(matrix)
}

func zeroMatrix(matrix [][]int) {
	fmt.Println(matrix)
	columns := []int{}

	for i := range matrix {
		for j, element := range matrix[i] {
			if element == 0 {
				zeroRow(matrix[i])
				columns = append(columns, j)
			}
		}
	}

	for _, column := range columns {
		for i := range matrix {
			matrix[i][column] = 0
		}
	}

	fmt.Println(matrix)
}

func zeroRow(row []int) {
	for i := range row {
		row[i] = 0
	}
}
