n = int(input())
solution = 0

for i in range(n):
    x = list(map( int , input().split()))
    sure_problem = 0 
    for i in x:
        if i == 1:
          sure_problem += 1
    if sure_problem > 1:
        solution += 1 

print(solution)   