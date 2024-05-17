rules = [x.strip() for x in open('input.txt', 'r').readlines() if x != '']
lines = [tuple(x.split()) for x in rules]
print(rules, lines)

def part1():
    lines_executed = set()
    cursor, accumulator = 0, 0

    while cursor not in lines_executed:
        instruction = lines[cursor][0]
        lines_executed.add(cursor)
        if instruction == 'jmp':
            cursor += int(lines[cursor][1])
        elif instruction == 'nop':
            cursor += 1
        elif instruction == 'acc':
            accumulator += int(lines[cursor][1])
            cursor += 1
    return accumulator

ans = part1()
print(ans)
