def generate(n):
    rows = [[1]]
    for i in range(1, n):
        rows.append([0] * (i + 1))
        for j in range(i+1):
            if j == 0:
                rows[i][j] = 1
            else:
                try:
                    rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
                except IndexError:
                    rows[i][j] = 1
    print(rows)
    for s in range(n): 
        if s < 5:   
            print(' ' * (n-s+1), ' '.join(str(x) for x in rows[s]))
        else:
            print(' ' * (n-s), ' '.join(str(x) for x in rows[s]), ' ' * (n-s))
        
generate(7)