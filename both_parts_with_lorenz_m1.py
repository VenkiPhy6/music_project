import music21 as m21
import fourth_rk_lorenz as lorenz
import numpy as np

##########################
refer_traj = lorenz.Lorenz(0,50,5000,np.array([1.0,1.0,1.0]))
var1_traj = lorenz.Lorenz(0,50,5000,np.array([.999,1.0,1.0]))

######################

full_part1 = m21.converter.parse('bwv846.mxl')
og_notes_part1 = [full_part1.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)[i] for i in range(len(full_part1.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)))]

full1_part1 = m21.converter.parse('bwv846.mxl')
cp_notes_part1 = [full1_part1.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)[i] for i in range(len(full1_part1.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)))]
cp_offset_list_part1 = [cp_notes_part1[i].offset for i in range(len(cp_notes_part1))]
refer_zip_part1 = list(zip(refer_traj, cp_offset_list_part1))

var1_offset_list_part1 = []
for i in var1_traj:
    for j in range(len(refer_zip_part1)):
        if((refer_zip_part1[j][0] - i) >= 10**-3):
            var1_offset_list_part1.append(refer_zip_part1[j][1])
            break
        else:
            continue

for i in range(len(cp_notes_part1)):
    cp_notes_part1[i].offset = var1_offset_list_part1[i]

og_part1 = m21.stream.Part(og_notes_part1, id='part1')
shuffled_part1 = m21.stream.Part(cp_notes_part1, id='part1')


####################################
full_part2 = m21.converter.parse('bwv846.mxl')
og_notes_part2 = []
bass = m21.clef.BassClef()
og_notes_part2.append(bass)
for i in full_part2.getElementsByClass(m21.stream.Part)[1][1].getElementsByClass(m21.stream.Voice):
    for j in range(len(i)):
        og_notes_part2.append(i[j])

full1_part2 = m21.converter.parse('bwv846.mxl')
cp_notes_part2 = []
for i in full1_part2.getElementsByClass(m21.stream.Part)[1][1].getElementsByClass(m21.stream.Voice):
    for j in range(len(i)):
        cp_notes_part2.append(i[j])
cp_offset_list_part2 = [cp_notes_part2[i].offset for i in range(len(cp_notes_part2))]
refer_zip_part2 = list(zip(refer_traj, cp_offset_list_part2))

var1_offset_list_part2 = []
for i in var1_traj:
    for j in range(len(refer_zip_part2)):
        if((refer_zip_part2[j][0] - i) >= 10**-3):
            var1_offset_list_part2.append(refer_zip_part2[j][1])
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

print("Reference:\n")
og_stream.show('text')
print("Shuffled:\n")
shuffled_stream.show('text')
