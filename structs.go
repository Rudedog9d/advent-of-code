package main

import (
	"github.com/rudedog9d/advent-of-code/2020/day1"
	"github.com/rudedog9d/advent-of-code/2020/day2"
)

// Map of the 25 days for accessing certain functions from CLI
type ChallengeYear map[string]ChallengeDay

// Two parts each day
type ChallengeDay struct {
	Part1 interface{}
	Part2 interface{}
}

func Build2020() ChallengeYear {
	var Year2020 = make(ChallengeYear)
	Year2020["day1"] = ChallengeDay{
		Part1: day1.Part1,
		Part2: day1.Part2,
	}
	Year2020["day2"] = ChallengeDay{
		Part1: day2.Part1,
		Part2: day2.Part2,
	}

	return Year2020
}
