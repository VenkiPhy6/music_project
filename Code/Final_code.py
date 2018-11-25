import matplotlib.pyplot as plt
import numpy as np
import music21 as m21


measures_count = 34


def lorenz(start,end,step_count,initial, sigma=10, R=28, b_param=8/3):
    
    """Uncomment lines 40, 41, 42 & 43 and call this function with appropriate arguments to get Figure 1 in the report"""
    
    def func(r, t):
        x = r[0]
        y = r[1]
        z = r[2]
        fx = sigma*(y-x)
        fy = R*x - y - x*z
        fz = x*y- b_param*z
        return np.array([fx,fy,fz])
    
    a = float(start)
    b = float(end)
    N = int(step_count)
    r = initial.copy()
    h = (b-a)/N
    xpoints = []
    ypoints = []
    zpoints = []
    tpoints = np.arange(a,b,h)
    
    for i in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        zpoints.append(r[2])
        k1 = h*func(r,i) 
        k2 = h*func(r + (k1/2), i + (h/2))
        k3 = h*func(r + (k2/2), i + (h/2))
        k4 = h*func(r + k3, i + h)
        r += (k1 + (2*k2) + (2*k3) + k4)/6
    
    return xpoints 
    #plt.plot(xpoints, zpoints)
    #plt.title(f"IC: {initial}")
    #plt.grid()
    #plt.show()

    
def variant_gen(initial_condition, measures_needed = measures_count, N=5000):
    """Uncomment line 91 and then call this function with initial condition [1.0, 1.0, 1.0] to get Figure 2 in the report or initial condition [0.999, 1.0, 1.0] to get Figure 3 in the report."""
    
    refer_traj = [round(i, 3) for i in lorenz(0,50,N,np.array([1.0,1.0,1.0]))]
    var_traj = [round(i, 3) for i in lorenz(0,50,N,initial_condition)]

    def takeSecond(elem):
        return elem[1]

    original = m21.converter.parse('bwv846.mxl')

    ####Creating the notes list and setting proper offset to it
    notes_part1 = []
    for i in original.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure)[0:measures_needed]:
        for j in i.getElementsByClass(m21.note.Note):
            notes_part1.append(j)
    for i in notes_part1:
        i.offset = i.getOffsetInHierarchy(original)

    ####Mapping the notes to the reference trajectory and creating a copy of that list
    refer_notes_part1 = list(zip(refer_traj, notes_part1))
    cp_refer_notes_part1 = refer_notes_part1.copy()

    ####Shuffling the notes and mapping it to the new trajectory
    shuffled_notes_part1 = []
    for i in var_traj:
        for j in cp_refer_notes_part1:
            if((j[0] > i and abs(j[0] - i) > 10**(-2)) or abs(j[0]-i) <= 10**(-3)):
                shuffled_notes_part1.append(j[1])
                cp_refer_notes_part1.remove(j)
                break
            else:
                continue
    offsets_part1 = [shuffled_notes_part1[i].offset for i in range(len(shuffled_notes_part1))]
    sorted_offsets_part1 = sorted(offsets_part1)
    for i in range(len(shuffled_notes_part1)):
        shuffled_notes_part1[i].offset = sorted_offsets_part1[i]

    var_notes_part1 = list(zip(var_traj, shuffled_notes_part1))

    ####Finishing the creation of part 1 of the variation
    part1 = m21.stream.Part(shuffled_notes_part1)

    ####Creating the variation
    variant = m21.stream.Stream(part1)
    #variant.show('musicxml')
    return refer_notes_part1, var_notes_part1


refer01 = variant_gen(np.array([1.0,1.0,1.0]), measures_count)[1]

def result1():
    """Call this function to get Figure 4 in the report."""
    
    var1= variant_gen(np.array([.999,1.0,1.0]), measures_count)[1]
    plt.plot([i for i in range(len(refer01))], [refer01[i][1].pitch.frequency for i in range(len(refer01))], 'r', label = 'Reference trajectory')
    plt.hold
    plt.plot([i for i in range(len(var1))], [var1[i][1].pitch.frequency for i in range(len(var1))], 'b', label = 'Variant trajectory')
    plt.ylabel("Pitch frequency")
    plt.xlabel("Pitch index")
    plt.grid()
    plt.legend(loc = 'upper right')
    plt.show()
    plt.title("Result1: Not all the pitches have changed. The variant still sounds a bit like the reference.")


def result2():
    """Call this function to get Figure 5 in the report"""
    
    non_variants_count_list = []
    for i in np.arange(-100,101,1):
        var2 = variant_gen(np.array([i,1.0,1.0]), measures_count)[1]
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