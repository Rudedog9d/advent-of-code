package day6

import "strconv"

func Part1(input []string) string {
	// store character as int32, since we're only looking for count of unique
	set := make(map[int32]struct{})
	count := 0
	for _, line := range input {
		if line == "" {
			count += len(set)
			set = make(map[int32]struct{})
			continue
		}
		for _, c := range line {
			set[c] = struct{}{}
		}
	}
	// Don't forget that final group with no trailing empty line!
	return strconv.Itoa(count + len(set))
}

func Part2(input []string) string {
	// store character as int32, since we're only looking for count of unique
	group := make(map[int32]bool)
	count := 0
	for _, line := range input {
		firstPerson := len(group) == 0
		person := make(map[int32]bool)

		// End of group, round up the answers
		if line == "" {
			for _, q := range group {
				if q {
					count += 1
				}
			}

			group = make(map[int32]bool)
			continue
		}

		for _, c := range line {
			person[c] = true

			// First person dictates the questions everyone else can answer yes too
			if firstPerson {
				group[c] = true
			}
		}

		for question, groupVal := range group {
			_, ok := person[question]
			// group has agreed thus far && person answered yes to question
			group[question] = groupVal && ok
		}
	}
	// Don't forget that final group with no trailing empty line!
	for _, q := range group {
		if q {
			count += 1
		}
	}
	return strconv.Itoa(count)
}
