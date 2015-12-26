import itertools
total = 0

ribbon = 0
with open('input.txt') as f:
        for line in f:
                dims = map(int, line.split('x'))
                side1 = dims[0]*dims[1] 
                side2 = dims[1]*dims[2]
                side3 = dims[2]*dims[0]
                slack = min(side1,side2,side3)
                area = 2*side1 + 2*side2 + 2*side3 + slack

                min_perim = min(2*dims[0]+2*dims[1],
                                2*dims[1]+2*dims[2],
                                2*dims[2]+2*dims[0])

                ribbon += min_perim + (dims[0]*dims[1]*dims[2])      
                total += area

print ribbon
print total
