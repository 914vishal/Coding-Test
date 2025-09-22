# Problem-3: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5
#     5) input a = 5, then output : 1, 3, 5, 7, 9
#     6) input a = 6, then output : 1, 3, 5, 7, 9
#     7) input a = x, then output : 1, 3, 5, 7, .......
    
    
def generate_series(a: int):
    limit = a if a % 2 != 0 else a - 1
    series = []
    for i in range(limit):
        series.append(2 * i + 1)
    return series

print(generate_series(1))  # [1]
print(generate_series(2))  # [1]
print(generate_series(3))  # [1, 3, 5]
print(generate_series(4))  # [1, 3, 5]
print(generate_series(5))  # [1, 3, 5, 7, 9]
print(generate_series(6))  # [1, 3, 5, 7, 9]
print(generate_series(10))  # [1, 3, 5, 7, 9, 11, 13, 15, 17]

