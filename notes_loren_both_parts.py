import music21 as m21
import numpy as np
import fourth_rk_lorenz as lorenz

#########################

initial_condition = np.array([.999,1.0,1.0])

refer_traj = lorenz.Lorenz(0,50,5000,np.array([1.0,1.0,1.0]))
var_traj = lorenz.Lorenz(0,50,5000,initial_condition)

def takeSecond(elem):
    return elem[1]

original = m21.converter.parse('bwv846.mxl')

#########################

#Creating the notes list and setting proper offset to it
notes_part1 = []
for i in original.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure)[0:11]:
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
        if((j[0] > i and abs(j[0] - i) >= 10**(-3)) or abs(j[0]-i) <= 10**(-6)):
            shuffled_notes_part1.append(j[1])
            cp_refer_notes_part1.remove(j)
            break
        else:
            continue
offsets_part1 = [shuffled_notes_part1[i].offset for i in range(len(shuffled_notes_part1))]
sorted_offsets_part1 = sorted(offsets_part1)
for i in range(len(shuffled_notes_part1)):
    shuffled_notes_part1[i].offset = sorted_offsets_part1[i]

m2_var_notes_part1 = list(zip(var_traj, sorted_offsets_part1))

#Finishing the creation of part 1 of the variation
part1 = m21.stream.Part(shuffled_notes_part1)

#########################

#Creating the notes list and setting proper offset to it
notes_part2 = []
notes_offset_part2 = []
for i in original.getElementsByClass(m21.stream.Part)[1].getElementsByClass(m21.stream.Measure)[0:11]:
    for j in i.getElementsByClass(m21.stream.Voice):
        for k in j.getElementsByClass(m21.note.Note):
            notes_part2.append(k)
for i in notes_part2:
    i.offset = i.getOffsetInHierarchy(original)
    notes_offset_part2.append(i.offset)
    
#Notes here are sorted by voice. Instead we need to sort it by offsets.
notes_offset = zip(notes_part2, notes_offset_part2)
sorted_note_offset = sorted(notes_offset, key=takeSecond) #takeSecond was defined at the start
notes_part2 = list(list(zip(*sorted_note_offset))[0])

#Mapping the notes to the reference trajectory and creating a copy of that list
refer_notes_part2 = list(zip(refer_traj, notes_part2))
cp_refer_notes_part2 = refer_notes_part2.copy()

#Shuffling the notes and mapping it to the new trajectory
shuffled_notes_part2 = []
for i in var_traj:
    for j in cp_refer_notes_part2:
        if((j[0] > i and abs(j[0] - i) >= 10**(-3)) or abs(j[0]-i) <= 10**(-6)):
            shuffled_notes_part2.append(j[1])
            cp_refer_notes_part2.remove(j)
            break
        else:
            continue
offsets_part2 = [shuffled_notes_part2[i].offset for i in range(len(shuffled_notes_part2))]
sorted_offsets_part2 = sorted(offsets_part2)
for i in range(len(shuffled_notes_part2)):
    shuffled_notes_part2[i].offset = sorted_offsets_part2[i]
m2_var_notes_part2 = list(zip(var_traj, sorted_offsets_part2))

#Finishing the creation of part 2 of the variation
shuffled_notes_part2.insert(0, m21.clef.BassClef()) #Explicitly mentioning Bass Cleff
part2 = m21.stream.Part(shuffled_notes_part2)
part2 = part2

#########################

#Creating the variant
variant = m21.stream.Stream([part1, part2])
#for i in [0,1,2,3,4,7]:
 #   variant.insert(0.0, original[i])
variant.show('musicxml')

#Analysis
#print("Method 2, Part2, Offsets:", offsets_part2)