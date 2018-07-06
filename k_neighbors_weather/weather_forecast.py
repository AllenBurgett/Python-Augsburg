pip install sklearn

from sklearn.neighbors import NearestNeighbors
from random import randint
import numpy as np

forecastdata = np.array([[randint(-25,111) for j in range(5)] for i in range(100)])
today = np.array([45, 23, 10, 1, 77]).reshape(1, -1)

nbrs = NearestNeighbors(n_neighbors=7, algorithm="auto").fit(forecastdata)
distances, indices = nbrs.kneighbors(today)

day = 1
print("Seven Day Forecast:")
for i in range(0,7):
    out = str(day) + " " + ' '.join("{0}".format(str(val)) for val in forecastdata[indices[0][i]])
    print(out)
    day += 1
