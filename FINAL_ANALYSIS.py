import music21 as m21
import tempo2_notes as t2n
import numpy as np
import matplotlib.pyplot as plt

refer01, var01 = t2n.variant_gen(np.array([.999,1.0,1.0]), 33)
refer11, var11= t2n.variant_gen(np.array([1.001,1.0,1.0]), 33)

plt.axes()
plt.plot([refer01[i][1].offset for i in range(len(refer01))],[refer01[i][1].pitch.frequency for i in range(len(refer01))], 'ro'); plt.grid(); plt.show()
plt.hold
plt.plot([var01[i][1].offset for i in range(len(var01))],[var01[i][1].pitch.frequency for i in range(len(var01))], 'bo'); plt.grid(); plt.show()
#plt.xlim([0,50])
#plt.xticks(np.arange(0,50,0.25))
plt.grid()
plt.show()