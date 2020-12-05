package day1

import (
	"sort"
	"strconv"
)

func stringToInt(input []string) []int {
	var data []int
	for _, element := range input {
		// todo generate this array sorted?
		val, _ := strconv.Atoi(element)
		data = append(data, val)
	}

	sort.Ints(data)
	return data
}

func Part1(input []string) string {
	data := stringToInt(input)
	for _, element := range data {
		for i := len(data) - 1; i >= 0; i-- {
			res := element + data[i]
			if res == 2020 {
				return strconv.Itoa(element * data[i])
			} else if res < 2020 {
				break // since we're sorted, if res < 2020, we've gone too far - try the next number
			}
		}
	}
	panic("could not find value!")
}

func Part2(input []string) string {
	data := stringToInt(input)
	for _, element := range data {
		for i := len(data) - 1; i >= 0; i-- {
			for j := len(data) - 1; j >= 0; j-- {
				res := element + data[i] + data[j]
				if res == 2020 {
					return strconv.Itoa(element * data[i] * data[j])
				}
			}
		}
	}
	panic("could not find value!")
}
