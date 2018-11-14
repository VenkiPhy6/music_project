import music21 as m21
import fourth_rk_lorenz as lorenz
import numpy as np

initial_condition = np.array([.999,1.0,1.0])
##########################
refer_traj = lorenz.Lorenz(0,50,5000,np.array([1.0,1.0,1.0]))
var1_traj = lorenz.Lorenz(0,50,5000,initial_condition)

def takeSecond(elem):
    return elem[1]
######################
full_part1 = m21.converter.parse('bwv846.mxl')
og_notes_part1 = []
for i in full_part1.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure)[0:11]:
    for j in i.getElementsByClass(m21.note.Note):
        og_notes_part1.append(j)

for i in og_notes_part1:
    i.offset = i.getOffsetInHierarchy(full_part1)

full1_part1 = m21.converter.parse('bwv846.mxl')
cp_notes_part1 = []
for i in full1_part1.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure)[0:11]:
    for j in i.getElementsByClass(m21.note.Note):
        cp_notes_part1.append(j)

cp_offset_list_part1 = []
for i in cp_notes_part1:
    cp_offset_list_part1.append(i.getOffsetInHierarchy(full1_part1))
refer_zip_part1 = list(zip(refer_traj, cp_offset_list_part1))
refer_zip_part1_cp = refer_zip_part1.copy()

var1_offset_list_part1 = []
for i in var1_traj:
    #print("varience :",i)
    for j in refer_zip_part1_cp:
        #print("reference:",j[0])
        if((j[0] > i and abs(j[0] - i) > 10**(-3)) or abs(j[0]-i) <= 10**(-6)):
            var1_offset_list_part1.append(j[1])
            refer_zip_part1_cp.remove(j)
            break
        else:
            continue

for i in range(len(cp_notes_part1)):
    cp_notes_part1[i].offset = var1_offset_list_part1[i]

og_part1 = m21.stream.Part(og_notes_part1, id='part1')
shuffled_part1 = m21.stream.Part(cp_notes_part1, id='part1')

masker_part1 = []
for i in range(len(cp_offset_list_part1)):
    masker_part1.append(cp_offset_list_part1[i] == var1_offset_list_part1[i])
#og_part1.show('musicxml')
#shuffled_part1.show('musicxml')

####################################

bass = m21.clef.BassClef()

full_part2 = m21.converter.parse('bwv846.mxl')
og_notes_part2 = []

for i in full_part2.getElementsByClass(m21.stream.Part)[1].getElementsByClass(m21.stream.Measure)[0:11]:
    for j in i.getElementsByClass(m21.stream.Voice):
        for k in j.getElementsByClass(m21.note.Note):
            og_notes_part2.append(k)

for i in og_notes_part2:
    i.offset = i.getOffsetInHierarchy(full_part2)

og_notes_part2.insert(0, bass)

full1_part2 = m21.converter.parse('bwv846.mxl')
cp_notes_part2 = []
for i in full1_part2.getElementsByClass(m21.stream.Part)[1].getElementsByClass(m21.stream.Measure)[0:11]:
    for j in i.getElementsByClass(m21.stream.Voice):
        for k in j.getElementsByClass(m21.note.Note):
            cp_notes_part2.append(k)

cp_offset_list_part2 = []
for i in cp_notes_part2:
    cp_offset_list_part2.append(i.getOffsetInHierarchy(full1_part2))
note_offset_zip = zip(cp_notes_part2, cp_offset_list_part2)
sorted_note_offset_zip = sorted(note_offset_zip, key=takeSecond)
cp_notes_part2 = list(list(zip(*sorted_note_offset_zip))[0])

refer_zip_part2 = list(zip(refer_traj, sorted(cp_offset_list_part2)))
refer_zip_part2_cp = refer_zip_part2.copy()

var1_offset_list_part2 = []
for i in var1_traj:
    #print("varience :",i)
    for j in refer_zip_part2_cp:
        #print("reference:",j[0])
        if((j[0] > i and abs(j[0] - i) > 10**(-3)) or abs(j[0]-i) <= 10**(-6)):
            var1_offset_list_part2.append(j[1])
            refer_zip_part2_cp.remove(j)
            break
        else:
            continue

for i in range(len(cp_notes_part2)):
    cp_notes_part2[i].offset = var1_offset_list_part2[i]
cp_notes_part2.insert(0, bass)

og_part2 = m21.stream.Part(og_notes_part2)
shuffled_part2 = m21.stream.Part(cp_notes_part2)

masker_part2 = []
for i in range(len(cp_offset_list_part2)):
    masker_part2.append(sorted(cp_offset_list_part2)[i] == var1_offset_list_part2[i])
#og_part2.show('musicxml')
#shuffled_part2.show('musicxml')
##################################

og_stream = m21.stream.Stream([og_part1, og_part2])
shuffled_stream = m21.stream.Stream([shuffled_part1, shuffled_part2])

m1_var1_zip_part1 = list(zip(var1_traj, var1_offset_list_part1))
m1_var1_zip_part2 = list(zip(var1_traj, var1_offset_list_part2))
print("IC:", initial_condition)
print("Are there duplicates in part 1?", set([x for x in var1_offset_list_part1[0:len(cp_offset_list_part1)] if var1_offset_list_part1[0:len(cp_offset_list_part1)].count(x) > 1]))
print("Are there variations in part 1?", not(all([masker_part1[i] for i in range(len(masker_part1))])))
print(f"Number of non-variants in part 1 out of {len(cp_notes_part1)} notes:", sum(masker_part1))
print("Are there duplicates in part 2?", set([x for x in var1_offset_list_part2[0:len(cp_offset_list_part2)] if var1_offset_list_part2[0:len(cp_offset_list_part2)].count(x) > 1]))
print("Are there variations in part 2?", not(all([masker_part2[i] for i in range(len(masker_part2))])))
print(f"Number of non-variants in part 2 out of {len(cp_notes_part2)-1} notes:", sum(masker_part2))
#og_stream.show('musicxml')
shuffled_stream.show('musicxml')