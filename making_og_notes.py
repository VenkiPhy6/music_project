import music21 as m21
import fourth_rk_lorenz as lorenz
import numpy as np

########
full_part1 = m21.converter.parse('bwv846.mxl')
og_notes_part1 = []
for i in full_part1.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure):
    for j in i.getElementsByClass(m21.note.Note):
        og_notes_part1.append(j)

for i in og_notes_part1:
    i.offset = i.getOffsetInHierarchy(full_part1)

og_part1 = m21.stream.Part(og_notes_part1, id='part1').makeMeasures()
########

bass = m21.clef.BassClef()

full_part2 = m21.converter.parse('bwv846.mxl')
og_notes_part2 = []

for i in full_part2.getElementsByClass(m21.stream.Part)[1].getElementsByClass(m21.stream.Measure):
    for j in i.getElementsByClass(m21.stream.Voice):
        for k in range(len(j)):
            og_notes_part2.append(j[k])

for i in og_notes_part2:
    i.offset = i.getOffsetInHierarchy(full_part2)
