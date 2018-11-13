import music21 as m21
import fourth_rk_lorenz as lorenz
import numpy as np

##########################
refer_traj = lorenz.Lorenz(0,50,5000,np.array([1.0,1.0,1.0]))
var1_traj = lorenz.Lorenz(0,50,5000,np.array([.999,1.0,1.0]))

######################

full_part1 = m21.converter.parse('bwv846.mxl')
og_notes_part1 = []
for i in full_part1.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure):
    for j in i.getElementsByClass(m21.note.Note):
        og_notes_part1.append(j)

for i in og_notes_part1:
    i.offset = i.getOffsetInHierarchy(full_part1)

full1_part1 = m21.converter.parse('bwv846.mxl')
cp_notes_part1 = []
for i in full1_part1.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure):
    for j in i.getElementsByClass(m21.note.Note):
        cp_notes_part1.append(j)

cp_offset_list_part1 = []
for i in cp_notes_part1:
    cp_offset_list_part1.append(i.getOffsetInHierarchy(full1_part1))
refer_zip_part1 = list(zip(refer_traj, cp_offset_list_part1))
refer_zip_part1_cp = refer_zip_part1.copy()

var1_offset_list_part1 = []
for i in var1_traj:
    for j in refer_zip_part1_cp:
        if((j[0] - i) >= 10**-3):
            var1_offset_list_part1.append(j[1])
            refer_zip_part1_cp.remove(j)
            break
        else:
            continue

for i in range(len(var1_offset_list_part1)):
    cp_notes_part1[i].offset = var1_offset_list_part1[i]

og_part1 = m21.stream.Part(og_notes_part1, id='part1')
shuffled_part1 = m21.stream.Part(cp_notes_part1, id='part1')


####################################

bass = m21.clef.BassClef()

full_part2 = m21.converter.parse('bwv846.mxl')
og_notes_part2 = []

for i in full_part2.getElementsByClass(m21.stream.Part)[1].getElementsByClass(m21.stream.Measure):
    for j in i.getElementsByClass(m21.stream.Voice):
        for k in range(len(j)):
            og_notes_part2.append(j[k])

for i in og_notes_part2:
    i.offset = i.getOffsetInHierarchy(full_part2)
og_notes_part2.insert(0, bass)

full1_part2 = m21.converter.parse('bwv846.mxl')
cp_notes_part2 = []
for i in full1_part2.getElementsByClass(m21.stream.Part)[1].getElementsByClass(m21.stream.Measure):
    for j in i.getElementsByClass(m21.stream.Voice):
        for k in range(len(j)):
            cp_notes_part2.append(j[k])

cp_offset_list_part2 = []
for i in cp_notes_part2:
    cp_offset_list_part2.append(i.getOffsetInHierarchy(full1_part2))
refer_zip_part2 = list(zip(refer_traj, cp_offset_list_part2))
refer_zip_part2_cp = refer_zip_part2.copy()

var1_offset_list_part2 = []
for i in var1_traj:
    for j in refer_zip_part2_cp:
        if((j[0] - i) >= 10**-3):
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

##################################

og_stream = m21.stream.Stream([og_part1, og_part2])
shuffled_stream = m21.stream.Stream([shuffled_part1, shuffled_part2])

og_stream.show('musicxml')
shuffled_stream.show('musicxml')