import music21 as m21
import random
#random.seed(15)

full = m21.converter.parse('bwv846.mxl')
og_notes = [full.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)[i] for i in range(len(full.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)))]

full1 = m21.converter.parse('bwv846.mxl')
cp_notes = [full1.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)[i] for i in range(len(full1.getElementsByClass(m21.stream.Part)[0][1].getElementsByClass(m21.note.Note)))]
offset_list = [cp_notes[i].offset for i in range(len(cp_notes))]
random.shuffle(offset_list)

for i in range(len(cp_notes)):
    cp_notes[i].offset = offset_list[i]

og_stream = m21.stream.Stream(og_notes)
shuffled_stream = m21.stream.Stream(cp_notes)

og_stream.show('musicxml')
shuffled_stream.show('musicxml')