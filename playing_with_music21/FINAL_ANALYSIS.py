import music21 as m21
import tempo2_notes as t2n
import numpy as np
import matplotlib.pyplot as plt
import making_og_notes as og

#################
measures_count = 12
refer01 = t2n.variant_gen(np.array([1.0,1.0,1.0]), measures_count)[1]
#################

#og.og_notes(measures_count)

#refer21, var21= t2n.variant_gen(np.array([1.0,1.0,1.0]), measures_count)

############

#RESULT0
var11= t2n.variant_gen(np.array([.999,1.0,1.0]), measures_count)[1]
#plt.plot([i for i in range(len(refer01))], [refer01[i][1].pitch.frequency for i in range(len(refer01))])
#plt.hold
#plt.plot([i for i in range(len(var11))], [var11[i][1].pitch.frequency for i in range(len(refer01))])
#plt.ylabel("Pitch frequency")
#plt.xlabel("Pitch frequency")
#plt.grid()
#plt.show()
#plt.title("Result1: Not all the pitches have changed. The variant still sounds a bit like the reference.")

############
"""
#RESULT1
non_variants_count_list = []
for i in range(2, 31):
    var = t2n.variant_gen(np.array([i,1.0,1.0]), measures_count)[1]
    non_variants_count = 0
    for i in  [abs(refer01[i][1].pitch.frequency - var[i][1].pitch.frequency) for i in range(len(refer01))]:
        if i <= 10**-6:
            non_variants_count += 1
    non_variants_count_list.append(non_variants_count)

plt.plot([i for i in range(2,31)], non_variants_count_list)
plt.ylabel("Number of non variants")
plt.xlabel("Initial condition of x")
plt.grid()
plt.show()
plt.title("Result2: Number of variants doesn't just increase as you get away from reference")
"""
#############

#print(number_of_variants01)
#print(number_of_variants02)

#plt.plot([i for i in range(len(refer01))],[refer01[i][1].pitch.frequency for i in range(len(refer01))], 'b')
#plt.hold
#plt.plot([i for i in range(len(var01))],[var01[i][1].pitch.frequency for i in range(len(var01))], 'r')
#plt.hold
#plt.plot([refer01[i][0] for i in range(len(var11))],[var11[i][1].pitch.frequency for i in range(len(var11))], 'go')

"""
plt.plot([i for i in range(len(refer01))],[abs(refer01[i][1].pitch.frequency - var01[i][1].pitch.frequency) for i in range(len(refer01))], 'go')
plt.hold
plt.plot([i for i in range(len(refer01))],[abs(refer01[i][1].pitch.frequency - var11[i][1].pitch.frequency) for i in range(len(refer01))], 'bo')
"""
