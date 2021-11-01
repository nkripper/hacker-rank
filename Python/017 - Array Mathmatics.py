import numpy

read_lines, array_size = list(map(int, input().split()))

a_array = []
for _ in range(read_lines):
    a_array.append(list(map(int, input().split())))

    b_array = []
for _ in range(read_lines):
    b_array.append(list(map(int, input().split())))

print(numpy.add(a_array, b_array))
print(numpy.subtract(a_array, b_array))
print(numpy.multiply(a_array, b_array))
print(numpy.floor_divide(a_array, b_array))
print(numpy.mod(a_array, b_array))
print(numpy.power(a_array, b_array))

