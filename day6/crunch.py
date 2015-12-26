
instructions = set([
    'turn on',
    'turn off',
    'toggle'
])


def process_rect(start, end, matrix, inst):
    xrng = (start[0], end[0])
    yrng = (start[1], end[1])
    for x in range(xrng[0], xrng[1]+1):
        for y in range(yrng[0], yrng[1]+1):
            if inst == 'turn on':
                matrix[x][y] += 1
            elif inst == 'turn off':
                val = matrix[x][y]
                val = max(val - 1, 0)
                matrix[x][y] = val
            elif inst == 'toggle':
                matrix[x][y] += 2
            else:
                assert 'what?'
X_WIDTH = 1000
Y_WIDTH = 1000

if __name__ == '__main__':
    lawn_matrix = [[0 for x in range(X_WIDTH)] for x in range(Y_WIDTH)]

    with open('input.txt') as f:
        for line in f:
            for instruction in instructions:
                if line.startswith(instruction):
                    instruction_to_exec = instruction
                    break
            coords_str = line.replace(instruction_to_exec,
                                      '').strip()
            coords_to_parse = coords_str.split(' through ')
            coords_start = coords_to_parse[0].split(',')
            coord_start= (int(coords_start[0]), int(coords_start[1]))

            coords_end = coords_to_parse[1].split(',')
            coord_end = (int(coords_end[0]), int(coords_end[1]))
            process_rect(coord_start,
                         coord_end,
                         lawn_matrix,
                         instruction_to_exec)

    total_on = 0
    for row in lawn_matrix:
        for light in row:
            if light:
                total_on += light

    print total_on
