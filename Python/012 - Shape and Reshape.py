import numpy

input_data = input().split()
input_data = list(map(int, input_data))

multi_array = numpy.array(input_data)
multi_array.shape = (3, 3)

print(multi_array)
