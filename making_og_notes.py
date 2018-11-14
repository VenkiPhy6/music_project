import music21 as m21

full = m21.converter.parse('bwv846.mxl').stripTies(retainContainers=True)

#############
og_notes_part1 = []
for i in full.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure):
    for j in i.getElementsByClass(m21.note.Note):
        og_notes_part1.append(j)

for i in og_notes_part1:
    i.offset = i.getOffsetInHierarchy(full)

og_part1 = m21.stream.Part(og_notes_part1, id='part1')

#############
bass = m21.clef.BassClef()
og_notes_part2 = []
for i in full.getElementsByClass(m21.stream.Part)[1].getElementsByClass(m21.stream.Measure):
    for j in i.getElementsByClass(m21.stream.Voice):
        for k in j.getElementsByClass(m21.note.Note):
            og_notes_part2.append(k)

#offsets = [] #
#for i in range(len(og_notes_part2)): #
#    print(og_notes_part2[i], og_notes_part2[i].offset) #
#    offsets.append(og_notes_part2[i].offset) #
#print(set(offsets)) #

for i in [2,3,4,5]:
    print(og_notes_part2[i].tie)

for i in og_notes_part2:
    i.offset = i.getOffsetInHierarchy(full)

#og_notes_part2.insert(0, bass)
og_part2 = m21.stream.Part(og_notes_part2)

############
og_stream = m21.stream.Stream([og_part1, og_part2])
og_stream.show('musicxml')