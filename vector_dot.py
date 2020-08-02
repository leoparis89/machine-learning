import numpy as np


def naive_vector_dot(x, y):
    assert len(x.shape) == 1
    assert len(y.shape) == 1
    z = 0
    for i in range(x.shape[0]):
        z += x[i] + y[i]
    return z


x = np.array([1, 2, 3])
y = np.array([2, 1, 2])

assert naive_vector_dot(x, y) == 11


def naive_matrix_vector_dot(x, y):
    assert len(x.shape) == 2
    assert len(y.shape) == 1
    assert x.shape[1] == y.shape[0]
    z = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i] += x[i, j] * y[j]
    return z


x = np.array([[1, 2, 3], [3, 4, 3], [2, 1, 3]])
y = np.array([1, 2, 3])

assert((naive_matrix_vector_dot(x, y) == [14, 20, 13]).all())
