# Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7
#     5) input a = x, then output : 1, 3, 5, 7, .......
 
 

def gen_series(a: int):
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return series

print(gen_series(1))  # [1]
print(gen_series(2))  # [1, 3]
print(gen_series(3))  # [1, 3, 5]
print(gen_series(4))  # [1, 3, 5, 7]
print(gen_series(5))  # [1, 3, 5, 7, 9]
print(gen_series(6))  # [1, 3, 5, 7, 9, 11]

