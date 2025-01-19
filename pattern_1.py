
# 1. Diamond Pattern
# -----------------------------------
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# -----------------------------------
# 2. Pascal's Triangle
# -----------------------------------
n = 5
for i in range(n):
    num = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

# -----------------------------------
# 3. Butterfly Pattern
# -----------------------------------
n = 5
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# # -----------------------------------
# # 4. Hollow Square with Diagonals
# # -----------------------------------
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# # -----------------------------------
# # 5. Spiral Matrix (Static Size)
# # -----------------------------------
# n = 5
# matrix = [[0] * n for _ in range(n)]
# top, left, bottom, right = 0, 0, n - 1, n - 1
# value = 1

# while top <= bottom and left <= right:
#     for i in range(left, right + 1):
#         matrix[top][i] = value
#         value += 1
#     top += 1

#     for i in range(top, bottom + 1):
#         matrix[i][right] = value
#         value += 1
#     right -= 1

#     for i in range(right, left - 1, -1):
#         matrix[bottom][i] = value
#         value += 1
#     bottom -= 1

#     for i in range(bottom, top - 1, -1):
#         matrix[i][left] = value
#         value += 1
#     left += 1

# for row in matrix:
#     print(" ".join(map(str, row)))
