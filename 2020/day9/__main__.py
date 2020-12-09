from pathlib import Path

data = [int(line.strip()) for line in open(Path(Path(__file__).parent, 'input.txt'))]


# # Sample Data
# data = [
#     35,
#     20,
#     15,
#     25,
#     47,
#     40,
#     62,
#     55,
#     65,
#     95,
#     102,
#     117,
#     150,
#     182,
#     127,
#     219,
#     299,
#     277,
#     309,
#     576,
# ]

# Sample Data Preamble
# preamble = 5

# Real Data Preamble
preamble = 25
vuln = None
for idx, i in enumerate(data):
    if idx < preamble:
        continue  # Move past Preamble

    found = False
    # Compare all combinations of previous PREAMBLE numbers
    for jdx, j in enumerate(data[idx - preamble:idx]):
        for kdx, k in enumerate(data[idx - preamble:idx]):
            if jdx == kdx:
                # skip comparison when j&k indices are the same -- same number
                continue

            if j + k == i:  # We found the vuln!
                found = True
                break  # break k loop
        if found:
            break  # break j loop
    if not found:
        print(f"part1: {i}")
        vuln = i
        break  # finally break i loop

for start_idx, i in enumerate(data):
    sum = 0
    data_rev = list(reversed(data[0:start_idx]))
    for jdx, j in enumerate(data_rev):
        if j == vuln:
            continue  # Skip the vulnerable number itself
        sum += j
        if sum > vuln:
            break
        if sum == vuln:
            print(f"part2: {min(data_rev[0:jdx + 1]) + max(data_rev[0:jdx + 1])}")
