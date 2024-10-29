import xcover as x
import matplotlib

# +
# x.algorithm_c?

# +
from xcover import covers

options = [[1, 4, 7], [1, 4], [4, 5, 7], [3, 5, 6], [2, 3, 6, 7], [2, 7]]
print(list(covers(options)))
# +
# matplotlib.pyplot.colormaps?

# +

matplotlib.pyplot.colormaps()[1]
# -

Map=plt.get_cmap('inferno')
Map

A=[[0,0,0],[1,1,1],[2,2,2]]
plt.imshow(A,colormap='inferno')
