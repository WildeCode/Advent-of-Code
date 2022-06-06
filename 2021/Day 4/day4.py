#!/usr/bin/python3

def get_input(filename):
    file = open(filename, 'r').read()
    input = file.split('\n')
    bnums = input[0].split(',')
    lines = input[1:]
    bcards = []
    for i in range(len(lines)):
        if lines[i] == '':
            bcards.append([lines[i+1].split(),
                           lines[i+2].split(),
                           lines[i+3].split(),
                           lines[i+4].split(),
                           lines[i+5].split()])
    return bnums, bcards


def check_number(number, bcards):
    # checks the number drawn against the cards and activates those
    # numbers with a '*'

    for card in bcards:
        for row in card:
            if number in row:
                row[row.index(number)] += '*'


def check_bingo(card):
    # checks for bingo for a card

    mark = '*'
    for i in range(5):
        column = []
        for row in card:
            column.append(row[i])
            if all(mark in number for number in row):
                return card
        if all(mark in number for number in column):
            return card

def calculate_score(card, bnum):
    mark = '*'
    score = 0
    for row in card:
        for number in row:
            if mark not in number:
                score += int(number)
    score = score * int(bnum)
    return score



def main():
    filename = '/home/axel/Code/Advent of Code/2021/Day 4/input'
    bnums, bcards = get_input(filename)
    return part1(bnums, bcards), part2(bnums, bcards)

def part1(bnums, bcards):
    for number in bnums:
        check_number(number, bcards)
        for card in bcards:
            if check_bingo(card):
                return calculate_score(card, number)

def part2(bnums, bcards):
    for number in bnums:
        check_number(number, bcards)
        for card in bcards:
            if check_bingo(card):
                if len(bcards) == 1:
                    return calculate_score(card, number)
                bcards.pop(bcards.index(card))


print(main())
