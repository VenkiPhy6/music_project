import music21 as m21
import fourth_rk_lorenz as lorenz
import numpy as np

initial_condition = np.array([.999,1.0,1.0])
##########################
refer_traj = lorenz.Lorenz(0,50,5000,np.array([1.0,1.0,1.0]))
var_traj = lorenz.Lorenz(0,50,5000,initial_condition)

def takeSecond(elem):
    return elem[1]

original = m21.converter.parse('bwv846.mxl')
######################

notes_part1 = []
for i in original.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure)[0:11]:
    for j in i.getElementsByClass(m21.note.Note):
        notes_part1.append(j)

notes_offset_part1 = []
for i in notes_part1:
    notes_offset_part1.append(i.getOffsetInHierarchy(original))
refer_part1 = list(zip(refer_traj, notes_offset_part1))
refer_part1_cp = refer_part1.copy()

var_offset_part1 = []
for i in var_traj:
    #print("varience :",i)
    for j in refer_part1_cp:
        #print("reference:",j[0])
        if((j[0] > i and abs(j[0] - i) >= 10**(-3)) or abs(j[0]-i) <= 10**(-6)):
            var_offset_part1.append(j[1])
            refer_part1_cp.remove(j)
            break
        else:
            continue

for i in range(len(notes_part1)):
    notes_part1[i].offset = var_offset_part1[i]

part1 = m21.stream.Part(notes_part1, id='part1')

#og_part1.show('musicxml')
#shuffled_part1.show('musicxml')

####################################

bass = m21.clef.BassClef()

notes_part2 = []
for i in original.getElementsByClass(m21.stream.Part)[1].getElementsByClass(m21.stream.Measure)[0:11]:
    for j in i.getElementsByClass(m21.stream.Voice):
        for k in j.getElementsByClass(m21.note.Note):
            notes_part2.append(k)

notes_offset_part2 = []
for i in notes_part2:
    notes_offset_part2.append(i.getOffsetInHierarchy(original))
note_offset_zip = zip(notes_part2, notes_offset_part2)
sorted_note_offset_zip = sorted(note_offset_zip, key=takeSecond)
cp_notes_part2 = list(list(zip(*sorted_note_offset_zip))[0])

refer_part2 = list(zip(refer_traj, sorted(notes_offset_part2)))
refer_part2_cp = refer_part2.copy()

var_offset_part2 = []
for i in var_traj:
    #print("varience :",i)
    for j in refer_part2_cp:
        #print("reference:",j[0])
        if((j[0] > i and abs(j[0] - i) >= 10**(-3)) or abs(j[0]-i) <= 10**(-6)):
            var_offset_part2.append(j[1])
            refer_part2_cp.remove(j)
            break
        else:
            continue

for i in range(len(cp_notes_part2)):
    cp_notes_part2[i].offset = var_offset_part2[i]
cp_notes_part2.insert(0, bass)

shuffled_part2 = m21.stream.Part(cp_notes_part2)

#og_part2.show('musicxml')
#shuffled_part2.show('musicxml')
##################################

shuffled_stream = m21.stream.Stream([part1, shuffled_part2])
shuffled_stream.show('musicxml')

#print("Method 1, Part2, Offsets:", var_offset_part2)

"""
masker_part1 = []
for i in range(len(notes_offset_part1)):
    masker_part1.append(notes_offset_part1[i] == var_offset_part1[i])

masker_part2 = []
for i in range(len(notes_offset_part2)):
    masker_part2.append(sorted(notes_offset_part2)[i] == var_offset_part2[i])

m1_var1_zip_part1 = list(zip(var_traj, var_offset_part1))
m1_var1_zip_part2 = list(zip(var_traj, var_offset_part2))
print("IC:", initial_condition)
print("Are there duplicates in part 1?", set([x for x in var_offset_part1[0:len(notes_offset_part1)] if var_offset_part1[0:len(notes_offset_part1)].count(x) > 1]))
print("Are there variations in part 1?", not(all([masker_part1[i] for i in range(len(masker_part1))])))
print(f"Number of non-variants in part 1 out of {len(notes_part1)} notes:", sum(masker_part1))
print("Are there duplicates in part 2?", set([x for x in var_offset_part2[0:len(notes_offset_part2)] if var_offset_part2[0:len(notes_offset_part2)].count(x) > 1]))
print("Are there variations in part 2?", not(all([masker_part2[i] for i in range(len(masker_part2))])))
print(f"Number of non-variants in part 2 out of {len(cp_notes_part2)-1} notes:", sum(masker_part2))
"""