import numpy as np
import matplotlib.pyplot as plt
import numpy.random as r
from scipy.constants import pi
import time

theta = np.linspace(0, 2 * pi, 5000)
circ = [[5, t] for t in theta]
circle = [[p[0] * np.cos(p[1]), p[0] * np.sin(p[1])] for p in circ]

def randInit(points):
    lower = 0
    indices = []
    for i in range(3):
        nextInd = r.randint(lower, len(points) - (3 - i), 1)[0]
        indices.append(nextInd)
        lower = nextInd + 1
    return indices

def evenInit(points):
    stop = len(points)
    startInt = r.randint(0, stop, 1)[0]
    jump = int(stop / 3)
    return [startInt, (startInt + jump) % stop, (startInt + 2 * jump) % stop]

def generateRandTriangles(active_segs, points):
    generated = []
    for seg in active_segs:
        i   = seg[0]
        n_i = seg[1]
        adj = 0
        if(n_i < i):
            adj = len(points)
        newVertex = r.randint(i + 1, adj + n_i, 1)[0]
        if(newVertex > len(points) - 1):
            newVertex %= len(points)
        newTri = [i, newVertex, n_i]
        generated.append(newTri)
    return generated

def genT_SplitIndices(active_segs, points):
    generated = []
    for seg in active_segs:
        i   = seg[0]
        n_i = seg[1]
        adj = 0
        if(n_i < i):
            adj = len(points)
        newVertex = int((i + n_i + adj) / 2)
        if(newVertex > len(points) - 1):
            newVertex %= len(points)
        newTri = [i, newVertex, n_i]
        generated.append(newTri)
    return generated

def randGeneration(points, iterations):
    if(iterations < 1):
        raise(ValueError)
    active_segments = []
    final_list = []
    start = randInit(points)
    final_list.append(start)
    active_segments = [[start[0], start[1]], [start[1], start[2]], [start[2], start[0]]]
    for i in range(iterations - 1):
        newTriangles = generateRandTriangles(active_segments, circle)
        temp = []
        for tri in newTriangles:
            temp.append([tri[0], tri[1]])
            temp.append([tri[1], tri[2]])
        active_segments = temp
        [final_list.append(new) for new in newTriangles]
    return final_list

def evenGeneration(points, iterations):
    if(iterations < 1):
        raise(ValueError)
    active_segments = []
    final_list = []
    start = evenInit(points)
    final_list.append(start)
    active_segments = [[start[0], start[1]], [start[1], start[2]], [start[2], start[0]]]
    for i in range(iterations - 1):
        newTriangles = genT_SplitIndices(active_segments, circle)
        temp = []
        for tri in newTriangles:
            temp.append([tri[0], tri[1]])
            temp.append([tri[1], tri[2]])
        active_segments = temp
        [final_list.append(new) for new in newTriangles]
    return final_list

# generate initial triangles, add tris on all sides
# save "new" triangles to list
# generate new2 triangles from list
# add old new to original
completed = False
while(not completed):
    try:
        triangles = randGeneration(circle, 5)
        completed = True
    except(ValueError):
        pass

for t in triangles:
    points = [circle[i] for i in t]
    print(points)
    plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]])
    plt.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]])
    plt.plot([points[2][0], points[0][0]], [points[2][1], points[0][1]])

plt.show()
plt.close()

completed = False
while(not completed):
    try:
        triangles = evenGeneration(circle, 5)
        completed = True
    except(ValueError):
        pass

for t in triangles:
    points = [circle[i] for i in t]
    print(points)
    plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]])
    plt.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]])
    plt.plot([points[2][0], points[0][0]], [points[2][1], points[0][1]])

plt.show()
plt.close()

