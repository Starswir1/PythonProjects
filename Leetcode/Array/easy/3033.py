matrix = [[1, 2, -1],
          [4, -1, 6],
          [7, 8, 9]]
for col in range(len(matrix[0])):
    max_in_col = max(matrix[row][col] for row in range(len(matrix)))  # 找到列的最大值
    # 遍历矩阵的每一行
    for row in range(len(matrix)):
        if matrix[row][col] == -1:
            matrix[row][col] = max_in_col
# for row in range(0, len(matrix)):
#     for col in range(0, len(matrix[row])):
#         if matrix[row][col] == -1:
#
#             for i in range(0, len(matrix)):
#                 arr = []
#                 a = matrix[0][i]
#                 arr.append(a)
#             matrix[row][col] = max(arr)
print(matrix)
