import numpy

(n_rows, m_rows, cols) = list(map(int, input().split()))

n_array = []
for _ in range(n_rows):
    n_array.append(list(map(int, input().split())))

m_array = []
for _ in range(m_rows):
    m_array.append(list(map(int, input().split())))

print(numpy.concatenate((n_array, m_array), axis=0))
