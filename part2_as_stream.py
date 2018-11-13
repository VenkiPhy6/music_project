import music21 as m21
import random
#random.seed(15)

full = m21.converter.parse('bwv846.mxl')
og_notes = []
bass = m21.clef.BassClef()
og_notes.append(bass)
for i in full.getElementsByClass(m21.stream.Part)[1][1].getElementsByClass(m21.stream.Voice):
    for j in range(len(i)):
        og_notes.append(i[j])


full1 = m21.converter.parse('bwv846.mxl')
cp_notes = []
for i in full1.getElementsByClass(m21.stream.Part)[1][1].getElementsByClass(m21.stream.Voice):
    for j in range(len(i)):
        cp_notes.append(i[j])
offset_list = [cp_notes[i].offset for i in range(len(cp_notes))]
random.shuffle(offset_list)

for i in range(len(cp_notes)):
    cp_notes[i].offset = offset_list[i]
cp_notes.insert(0, bass)

og_stream = m21.stream.Stream(og_notes)
shuffled_stream = m21.stream.Stream(cp_notes)

og_stream.show('musicxml')
shuffled_stream.show('musicxml')