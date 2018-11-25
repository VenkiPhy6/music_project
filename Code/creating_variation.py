def variant_gen(initial_condition, measures_needed = 11, N=5000):
    import music21 as m21
    import numpy as np
    import creating_lorenz as lorenz

    #########################

    refer_traj = [round(i, 3) for i in lorenz.Lorenz(0,50,N,np.array([1.0,1.0,1.0]))]
    var_traj = [round(i, 3) for i in lorenz.Lorenz(0,50,N,initial_condition)]

    def takeSecond(elem):
        return elem[1]

    original = m21.converter.parse('bwv846.mxl')

    #########################

    #Creating the notes list and setting proper offset to it
    notes_part1 = []
    for i in original.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure)[0:measures_needed]:
        for j in i.getElementsByClass(m21.note.Note):
            notes_part1.append(j)
    for i in notes_part1:
        i.offset = i.getOffsetInHierarchy(original)

    #Mapping the notes to the reference trajectory and creating a copy of that list
    refer_notes_part1 = list(zip(refer_traj, notes_part1))
    cp_refer_notes_part1 = refer_notes_part1.copy()

    #Shuffling the notes and mapping it to the new trajectory
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

    #Finishing the creation of part 1 of the variation
    part1 = m21.stream.Part(shuffled_notes_part1)
    #########################

    #Creating the variant
    variant = m21.stream.Stream(part1)
    #variant.show('musicxml')
    return refer_notes_part1, var_notes_part1