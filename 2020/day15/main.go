package day15

import (
	"strconv"
	"strings"
)

func parse_data(input []string) []int {
	strs := strings.Split(input[0], ",")
	ints := make([]int, len(strs))

	for i, s := range strs {
		ints[i], _ = strconv.Atoi(s)
	}
	return ints
}

func do_stuff(input []string, target int) string {
	var turns = parse_data(input)
	//var turns = parse_data([]string{"0,3,6"}) // test data
	//var turns = parse_data([]string{"2,1,3"}) // test data
	lastTurn := make(map[int]int)

	for i := 0; i < len(turns)-1; i++ {
		num := turns[i]
		//println("starting num", num)
		lastTurn[num] = i + 1
	}

	i := len(turns)
	spoken := turns[len(turns)-1]
	for len(turns) <= target {
		//println("Turn", i, "spoken:", spoken)

		// Get the last turn that number was spoken
		last, found := lastTurn[spoken]
		if found {
			lastTurn[spoken] = i
			spoken = i - last
		} else {
			lastTurn[spoken] = i
			spoken = 0
		}
		turns = append(turns, spoken)
		i++
	}

	return strconv.Itoa(turns[target-1]) // Turn target, minus 1 because of 0-indexing
}
func Part1(input []string) string {
	return do_stuff(input, 2020)
}

func Part2(input []string) string {
	return do_stuff(input, 30000000)
}
