import numpy
numpy.set_printoptions(legacy='1.13')

(rows, cols) = list(map(int, input().split()))

print(numpy.eye(rows, cols))
