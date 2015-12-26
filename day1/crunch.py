CMDS = {
    '(' : 1,
    ')' : -1
}

pos = 0
with open('input.txt') as f:
        s = f.read()
        for i, char in enumerate(s.strip()):
            if not char in CMDS:
                continue
            pos += CMDS[char]
            if pos < 0:
                    print i+1
                    break


print pos
