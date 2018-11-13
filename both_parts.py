import music21 as m21
import random
#random.seed(15)

full_part1 = m21.converter.parse('bwv846.mxl')
og_notes_part1 = [full_part1.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)[i] for i in range(len(full_part1.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)))]

full1_part1 = m21.converter.parse('bwv846.mxl')
cp_notes_part1 = [full1_part1.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)[i] for i in range(len(full1_part1.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)))]
offset_list_part1 = [cp_notes_part1[i].offset for i in range(len(cp_notes_part1))]

#******************
random.shuffle(offset_list_part1)
#******************

for i in range(len(cp_notes_part1)):
    cp_notes_part1[i].offset = offset_list_part1[i]

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
offset_list_part2 = [cp_notes_part2[i].offset for i in range(len(cp_notes_part2))]

#****************
random.shuffle(offset_list_part2)
#****************

for i in range(len(cp_notes_part2)):
    cp_notes_part2[i].offset = offset_list_part2[i]
cp_notes_part2.insert(0, bass)

og_part2 = m21.stream.Stream(og_notes_part2)
shuffled_part2 = m21.stream.Stream(cp_notes_part2)


##################################
og_stream = m21.stream.Stream([og_part1, og_part2])
shuffled_stream = m21.stream.Stream([shuffled_part1, shuffled_part2])

og_stream.show('musicxml')
shuffled_stream.show('musicxml')