import matplotlib.pyplot as plt

ax = plt.subplot(1,2,1)
ax.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')

ax = plt.subplot(1,2,2)
ax.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax.arrow(0, 0, 0.2, 0.1, head_width=0.05, head_length=0.1, fc='k', ec='k')
plt.show()