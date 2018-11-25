import music21 as m21
import creating_variation as var
import numpy as np
import matplotlib.pyplot as plt

#################

measures_count = 34
refer01 = var.variant_gen(np.array([1.0,1.0,1.0]), measures_count)[1]

#################

"""
#RESULT0
var1= var.variant_gen(np.array([.999,1.0,1.0]), measures_count)[1]
plt.plot([i for i in range(len(refer01))], [refer01[i][1].pitch.frequency for i in range(len(refer01))], 'r', label = 'Reference trajectory')
plt.hold
plt.plot([i for i in range(len(var1))], [var1[i][1].pitch.frequency for i in range(len(var1))], 'b', label = 'Variant trajectory')
plt.ylabel("Pitch frequency")
plt.xlabel("Pitch index")
plt.grid()
plt.legend(loc = 'upper right')
plt.show()
plt.title("Result1: Not all the pitches have changed. The variant still sounds a bit like the reference.")
"""

############

#RESULT1
non_variants_count_list = []
for i in np.arange(-100,101,1):
    var2 = var.variant_gen(np.array([i,1.0,1.0]), measures_count)[1]
    non_variants_count = 0
    for i in [abs(refer01[i][1].pitch.frequency - var2[i][1].pitch.frequency) for i in range(len(refer01))]:
        if i <= 10**-6:
            non_variants_count += 1
    non_variants_count_list.append(non_variants_count)

plt.plot([i for i in np.arange(-100,101,1)], non_variants_count_list)
plt.ylabel("Number of non variants")
plt.xlabel("Initial condition of x")
plt.grid()
plt.show()
plt.title("Result2: Number of non variants doesn't just decrease as you get away from reference")

#############