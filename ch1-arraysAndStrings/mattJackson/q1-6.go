package main

/* 1.6 - String Compression:
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string a a b c c c c c a a a would become a 2 b 1 c 5 a 3 , If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z). */

import (
	"fmt"
	"strings"
)

type tuple struct {
	letter string
	count  int
}

func main() {
	t := []string{"a", "a", "b", "b", "b", "b", "e", "e", "e", "d", "d", "a", "A", "A", "a"}
	makeCount(t)
}

func makeCount(characters []string) {
	for i, char := range characters {
		characters[i] = strings.ToLower(char)
	}

	fmt.Println(characters)
	counter := 1
	record := []tuple{}

	for i, char := range characters {
		if (i + 1) < len(characters) {
			if characters[i] != characters[i+1] {
				newTuple := tuple{}
				newTuple.letter = char
				newTuple.count = counter
				record = append(record, newTuple)
				counter = 1
			} else {
				counter++
			}
		} else {
			newTuple := tuple{}
			newTuple.letter = char
			newTuple.count = counter
			record = append(record, newTuple)
		}
	}
	fmt.Println(record)
}
