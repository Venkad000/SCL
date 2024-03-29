﻿SCIENTIFIC COMPUTING LAB
WORKSHEET 1
                                                                                20PT06






1. Find Augmented Matrix Corresponding to given Linear System


        import re
n=int(input("Enter the number of equations:"))
equations=[]
for i in range(n):
        equations.append(input())


arr=[]
for eq in equations:
        arr.append(re.findall('[0-9+-]+', eq))
    
print(arr)




2.Check which of the following matrices are in REF or RREF.


        R=int(input("Enter the number of rows of the matrix:"))
C=int(input("Enter the number of columns of the matrix:"))
arr=[]
 
for i in range(R):              
        a =[]
        for j in range(C):         
             a.append(int(input()))
        arr.append(a)
    
flag=True
for i in range(0, R):
        for j in range(0, C):
            if arr[i][j]!=0:
                if arr[i][j]!=1:
                    flag=False
                    break
                for x in range(0, R):
                    if arr[x][j]!=0 and x!=i:
                        flag=False
                        break
                break
        if flag==False:
            break
           


if flag:
        print('The given Matrix is  in reduced row echelon form')
else:
        print("The given Matrix is not in reduced row echelon form")




3.Gauss-Jordan Elimination method to find the RREF


        matrix = [[1, 1, 2, 8], [-1, -2, 3, 1], [3, -7, 4, 10]]
rows = len(matrix)
columns = len(matrix[0])
non_zero_index = -1


def non_zero(row):
for i in range(len(row)):
if row[i] != 0:
return i


# Arrange the rows by leftmost non-zero entry
matrix.sort(key = non_zero)
for i in range(0, rows):
# Making the first non-zero element 1
for j in range(columns):
if not math.isclose(matrix[i][j], 0.0):
non_zero_index = j
matrix[i] = [x / matrix[i][j] for x in matrix[i]]
break
# Making leading coefficient column corresponding values 0
for j in range(rows):
if j == i:
continue
else:
                                    ratio = matrix[j][non_zero_index] /matrix[i][non_zero_index]
                               row = [x * ratio for x in matrix[i]]
                                    matrix[j] = [x - y for x, y in zip(matrix[j], row)]


print("The given matrix in RREF is:")
for row in matrix:
print(row)
rank = rows
zeros = [0] * columns
for row in matrix:
if row == zeros:
rank -= 1
print("\nRank =", rank)




4.Solutions for a linear system using Gauss-Jordan elimination.


        def non_zero(row):
for i in range(len(row)):
if row[i] != 0:
return i


def rref(matrix):
rows = len(matrix)
columns = len(matrix[0])
non_zero_index = -1
# Arrange the rows by leftmost non-zero entry
matrix.sort(key = non_zero)
for i in range(0, rows):
# Making the first non-zero element 1
for j in range(columns):
if not math.isclose(matrix[i][j], 0.0):
non_zero_index = j
matrix[i] = [x / matrix[i][j] for x in matrix[i]]
break
# Making leading coefficient column corresponding values 0
for j in range(rows):
if j == i:
continue
else:
ratio = matrix[j][non_zero_index] / matrix[i][non_zero_index]
row = [x * ratio for x in matrix[i]]
matrix[j] = [x - y for x, y in zip(matrix[j], row)]
print("The given matrix in RREF is:")
for row in matrix:
print(row)
return matrix


lin_sys = ["1x1 + 1x2 + 2x3 = 8", "-1x1 - 2x2 + 3x3 = 1", "3x1 - 7x2 + 4x3
= 10"]
# Finding the augmented matrix
aug = []
for eqn in lin_sys:
row = []
for i in range(len(eqn)):
if eqn[i] == 'x':
if eqn[i - 2] == '-' or eqn[i - 3] == '-':
row.append(-int(eqn[i - 1]))
else:
row.append(int(eqn[i - 1]))
if eqn[i] == '=':
row.append(int(eqn[i + 1:]))
aug.append(row)
aug = rref(aug)
rank = len(aug)
zeros = [0] * len(aug[0])
solution = []
for row in aug:
if row == zeros:
rank -= 1
# Unique Solution
if rank == len(aug[0]) - 1:
for i in range(len(aug) - 1, -1, -1):
for j in range(len(aug[0]) - 1):
if math.isclose(aug[i][j], 0.0):
continue
else:
solution.insert(0, aug[i][len(aug[0]) - 1])
print("Unique Solution:", solution)
# Infinite Solutions
elif rank < len(aug[0]) - 1:
print("Infinite Solutions")
# No solution
else:
print("No Solution")




5.Solve the following linear system using Gauss-Seidel.


        lin_sys = ["3x + 1x2 = 11", "2x1 + 5x2 = 16"]
# Finding the augmented matrix
aug = []
for eqn in lin_sys:
row = []
for i in range(len(eqn)):
if eqn[i] == 'x':
if eqn[i - 2] == '-' or eqn[i - 3] == '-':
row.append(-int(eqn[i - 1]))
else:
row.append(int(eqn[i - 1]))
if eqn[i] == '=':
row.append(int(eqn[i + 1:]))
aug.append(row)


rows = len(aug)
columns = len(aug[0])
solutions = [0] * (columns - 1)
for i in range(10):
for j in range(rows):
x = aug[j][columns - 1]
for k in range(columns - 1):
if k != j:
x -= aug[j][k] * solutions[k]
solutions[j] = x / aug[j][j]
print("Iteration", i + 1)
print(solutions)
for i in range(columns - 1):
print("x", i + 1, " = ", solutions[i], sep = "")






6.Solve the linear system using Gauss-Jacobi Method.


        lin_sys = ["2x + 5x2 = 21", "1x1 + 2x2 = 8"]
aug = []
for eqn in lin_sys:
row = []
for i in range(len(eqn)):
if eqn[i] == 'x':
    if eqn[i - 2] == '-' or eqn[i - 3] == '-':
row.append(-int(eqn[i - 1]))
else:
row.append(int(eqn[i - 1]))
if eqn[i] == '=':
row.append(int(eqn[i + 1:]))
aug.append(row)


rows = len(aug)
columns = len(aug[0])
prev = [0] * (columns - 1)
solutions = [0] * (columns - 1)
for i in range(10):
for j in range(rows):
x = aug[j][columns - 1]
for k in range(columns - 1):
if k != j:
x -= aug[j][k] * prev[k]
solutions[j] = x / aug[j][j]


print("Iteration", i + 1)
print(solutions)
for i in range(len(solutions)):
prev[i] = solutions[i]
for i in range(columns - 1):
print("x", i + 1, " = ", solutions[i], sep = "")
