#!/usr/bin/python3

def get_report(file_name):
    file = open(file_name, "r")
    report = file.read().split("\n") # array
    return report

def part1(report):
    # first let's figure out which bits are more commonly 1 or 0
    # a negative number indicates 0s are more common at the given index
    # a positive number indicates 1s are more common at the given index
    
    for line in report:
        if 'common_bit' not in locals():
            common_bit = [0] * len(line)
            
        i = 0
        for bit in line:
            if bit == '0':
                common_bit[i] -= 1
            if bit == '1':
                common_bit[i] += 1
            i += 1
            
    # generate gamma and epsilon rates
    gamma_rate = ''
    epsilon_rate = ''
    for bit in common_bit:
        if bit < 0:
            gamma_rate += '0'
            epsilon_rate += '1'
        if bit >= 0:
            gamma_rate += '1'
            epsilon_rate += '0'
        
    #now we convert the binary values to decimal
    gamma_rate = binary_to_decimal(gamma_rate)
    epsilon_rate = binary_to_decimal(epsilon_rate)
    power_consumption = gamma_rate * epsilon_rate
        
    return power_consumption
    
def binary_to_decimal(binary):
    decimal = 0
    power_list = []
    for i in range(len(binary)):
        power_list.append(2**i)
    binary = binary[len(binary)::-1]
    
    for i in range(len(binary)):
        decimal += int(binary[i]) * power_list[i]
        i += 1
    return decimal
    
def part2(report):
    ogr = find_ogr(report, 0) # oxygen generator rating
    csr = find_csr(report, 0) # CO2 scrubber rating
    lsr = ogr * csr # life support rating
    return lsr

def find_ogr(report, i):
    # Recursive function to find ogr
    
    common_bit = 0
    for line in report: # start finding most common bit value based on current index
        
        if line[i] == '0':
            common_bit -= 1
        elif line[i] == '1':
            common_bit += 1

    new_report = []
    j = 0
    for line in report: # time to add the lines that meet the bit criteria
        if common_bit >= 0 and line[i] == '1':
            new_report.append(line)
        elif common_bit < 0 and line[i] == '0':
            new_report.append(line)
        j += 1
    
    if len(new_report) == 1:
        return binary_to_decimal(new_report[0])
    elif len(new_report) > 1:
        return find_ogr(new_report, i+1)

def find_csr(report, i):
    # Recursive function to find csr
    
    common_bit = 0
    for line in report: # start finding most common bit value based on current index
        if line[i] == '0':
            common_bit -= 1
        elif line[i] == '1':
            common_bit += 1

    new_report = []
    for line in report: # time to add the lines that meet the bit criteria
        if common_bit >= 0 and line[i] == '0':
            new_report.append(line)
        elif common_bit < 0 and line[i] == '1':
            new_report.append(line)
    if len(new_report) == 1:
        return binary_to_decimal(new_report[0])
    else:
        return find_csr(new_report, i+1)
        

def main(filename):
    report = get_report(filename)
    print('Part 1: '+str(part1(report)))
    print('Part 2: '+str(part2(report)))

filename = "/home/axel/Code/Advent of Code/2021/Day 3/report"
#filename = "/home/axel/Code/Advent of Code/2021/Day 3/test_report"
main(filename)
