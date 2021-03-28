m = int(input())
n = int(input())
#grid = [ [3, 10, 8, 14], [1, 11, 12, 12], [6, 2, 3, 9] ]
grid = []

for i in range(m):
    line = input().split()
    line = [int(i) for i in line]
    grid.append(line)

end_cell = (m,n)

visited = set([(1, 1)])

stack = [[1,1]]
  
while stack:
  (r, c) = stack.pop()
  #print("Popped: ", (r, c))
  x = grid[r-1][c-1]
  for i in range(1, x+1):
      mod = x % i
      if mod == 0:
        new_cell = (i, x//i)
        if new_cell [0] <= m and new_cell[1] <= n: 
          if new_cell == end_cell:
            print("Yes")
            exit()
          if new_cell not in visited:
            stack.append(new_cell)
            #print("Appended: ", new_cell)

          visited.add(new_cell)
          #print("Visited: ", visited)

  
print("no")
        