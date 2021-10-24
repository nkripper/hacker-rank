import numpy

row_count, col_count = map(int, input().split())

my_array = []

for _ in range(row_count):
    my_array.append(list(map(int, input().split())))

my_array = numpy.array(my_array)

print(numpy.transpose(my_array))
print(my_array.flatten())
