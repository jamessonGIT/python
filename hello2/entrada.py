import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

sns.lineplot(x=x, y=y)
plt.xlabel('Regressão linear')