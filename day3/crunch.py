from collections import defaultdict

houses_visited =  defaultdict(int)

robo_santa_pos = (0,0)
santa_pos = (0,0)
dirs = {
'^': (0, 1),
'>': (1, 0),
'v': (0, -1),
'<': (-1, 0)
}

with open('input_big.txt') as f:
        line = f.read()
        cnt = 0

        houses_visited[santa_pos] += 1
        houses_visited[robo_santa_pos] += 1
        for direction in line.strip():
                if cnt % 2 == 0:
                    santa_pos = (
                                santa_pos[0] + dirs[direction][0],
                                santa_pos[1] + dirs[direction][1]
                                )
                    houses_visited[santa_pos] += 1

                else:

                    robo_santa_pos = (
                                robo_santa_pos[0] + dirs[direction][0],
                                robo_santa_pos[1] + dirs[direction][1]
                                )
                    houses_visited[robo_santa_pos] += 1
                cnt += 1
total = 0
for house, visits in houses_visited.items():
    if visits >= 1:
        total += 1

print total
