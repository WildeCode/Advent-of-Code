def main(input):
    print(part1(input))
    print(part2(input))

def part1(input):
    moves = input.split('\n')
    x = 0
    y = 0
    for move in moves:
        move = move.split()
        direction = move[0]
        distance = int(move[1])
        if direction == "forward":
            x += distance
        elif direction == "down":
            y += distance
        elif direction == "up":
            y -= distance
    return x*y
    
def part2(input):
    moves = input.split('\n')
    x = 0
    y = 0
    aim = 0
    for move in moves:
        move = move.split()
        direction = move[0]
        distance = int(move[1])
        if direction == "forward":
            x += distance
            y += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
    return x*y

def get_input(filename): 
    file = open(filename, 'r')
    input = file.read()
    return input    

filename = '/home/axel/Code/Advent of Code/2021/Day 2/input'
main(get_input(filename))