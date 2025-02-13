import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# barplot 長條圖, displot 直條&密度圖, relplot 散點圖 
t=sns.load_dataset('titanic')
#sns.barplot(x='pclass',y='who',data=t)
sns.barplot(x='class',y='survived',hue='who',data=t)
sns.displot(t['age'])
age=t['age'].dropna()
sns.displot(age)
plt.show()

"""f=sns.load_dataset("flights")
sns.set(style="darkgrid")
sns.relplot(x="passengers",y="year",hue="month",data=f)
plt.show()"""

"""sns.set(style="darkgrid")
i=sns.load_dataset("iris")
sns.relplot(x="petal_width",y="petal_length",hue="species",data=i)
plt.show()"""

# 3D plot
"""
sns.set(style="ticks")
ax = plt.axes(projection='3d')
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='summer_r')
plt.show()

f=sns.load_dataset('fmri')
sns.set(style="darkgrid")
sns.kdeplot(
    data=f, x="signal", y="timepoint",
    fill=True, thresh=0, levels=100, cmap="PuBuGn",
)
plt.show()
"""
