package main

import (
    "fmt"
    "io/ioutil"
	"strings"
	"strconv"
)

func readFile(fileName string) []int{
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Println("File reading error", err)
	}
	var numbers []int
	lines := strings.Split(string(data), "\n")
	for i := 0; i < len(lines); i++ {
		currentNumber, err := strconv.Atoi(lines[i])
		if err != nil {
			fmt.Println("Convertion error", err)
		}
		numbers = append(numbers, currentNumber)
	}

	return numbers
}

func main(){
	fmt.Println("Hello, World!")
	numbers := readFile("input.txt")
	sum := len(numbers)
	for i :=0; i < len(numbers); i++ {
		if i > 0 && numbers[i] < numbers[i-1] {
			sum--
		}
	}
	fmt.Printf("%d", sum - 1)
}