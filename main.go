package main

import (
	"bufio"
	"fmt"
	"os"
	"path"
	"time"
)

func CheckError(e error) {
	// Check error and handle it
	// todo don't panic
	if e != nil {
		panic(e)
	}
}

func readData(path string) []string {
	file, err := os.Open(path)
	CheckError(err)
	defer file.Close()

	var input []string

	// iterate lines
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}

	CheckError(scanner.Err())
	return input
}

func main() {
	// todo arg for using sample_input.txt
	// todo better argument parsing
	activeYear := Build2020()
	basedir := os.Args[1]
	day := os.Args[2]
	input := readData(path.Join(basedir, "2020", day, "input.txt"))
	activeDay := activeYear[day] // todo handle when day isn't found

	start1 := time.Now()
	if activeDay.Part1 != nil {
		fmt.Println(day, "Part 1:", activeDay.Part1.(func([]string) string)(input), "(", time.Since(start1), "seconds )")
	}

	if activeDay.Part2 != nil {
		start2 := time.Now()
		fmt.Println(day, "Part 2:", activeDay.Part2.(func([]string) string)(input), "(", time.Since(start2), "seconds )")
	}
	fmt.Println("Total Execution:", time.Since(start1), "seconds")
}
