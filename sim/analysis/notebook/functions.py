import numpy as np
import matplotlib.pyplot as plt

def clipOne(array2d):
    clipped2d = []
    for array1d in array2d:
        clipped1d = [1.0 if val >= 0.0 else -1.0 for val in array1d]
        clipped2d.append(clipped1d)

    return np.array(clipped2d)


def deleteOverlap(array2d):
    deleted_array = []
    for i, array1d in enumerate(array2d):
        if i == 0:
            deleted_array.append(array1d)
        else:
            if any(array1d != deleted_array[-1]):
                deleted_array.append(array1d)

    return np.array(deleted_array)
    

def countTuples(array2d):
    types = {}
    for i, array1d in enumerate(array2d[:-1]):
        if tuple(array1d) not in types:
            types[tuple(array1d)] = {
                    'count': 1,
                    'next': dict()
                    }
            types[tuple(array1d)]['next'][tuple(array2d[i+1])] = 1
        else:
            types[tuple(array1d)]['count'] += 1
            if tuple(array2d[i+1]) not in types[tuple(array1d)]['next']:
                types[tuple(array1d)]['next'][tuple(array2d[i+1])] = 1
            else:
                types[tuple(array1d)]['next'][tuple(array2d[i+1])] += 1

    return types
