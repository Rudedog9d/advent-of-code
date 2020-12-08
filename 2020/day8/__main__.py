from pathlib import Path

data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


# Sample Data
# data = [
#     "nop +0",
#     "acc +1",
#     "jmp +4",
#     "acc +3",
#     "jmp -3",
#     "acc -99",
#     "acc +1",
#     "jmp -4",
#     "acc +6",
# ]

def execute(program):
    """
    Execute `program`
    :param program: list of instructions to execute
    :return Tuple[int,bool]: Tuple of last Accumulator value and Success status -
                                True if program exited, False if infinite loop detected
    """
    accumulator = 0
    ptr = 0
    history = []

    while True:
        if ptr >= len(program):
            return accumulator, True
        instruction, arg = program[ptr].split()
        arg = int(arg)

        if ptr in history:
            # We're in an infinite loop, return False
            return accumulator, False
        # track ptr value and watch for infinite loops
        history.append(ptr)

        if instruction == "acc":
            accumulator += arg
        if instruction == "jmp":
            ptr += arg  # when I say jump, you jump!
            continue

        # Not a jmp, move to next instruction
        ptr += 1


print(f"part1: {execute(data)[0]}")


def try_fix():
    for i, _ in enumerate(data):
        mod_data = data.copy()
        ins, _ = data[i].split()
        if ins == "acc":
            continue  # we don't change accumulator calls, ignore
        if ins == "nop":
            mod_data[i] = mod_data[i].replace("nop", "jmp")
        if ins == "jmp":
            mod_data[i] = mod_data[i].replace("jmp", "nop")

        acc, success = execute(mod_data)
        if success:
            return acc


print(f"part2: {try_fix()}")
