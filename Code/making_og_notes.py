def og_notes(measures_needed):
    import music21 as m21
    full = m21.converter.parse('bwv846.mxl')

    #############
    og_notes_part1 = []
    for i in full.getElementsByClass(m21.stream.Part)[0].getElementsByClass(m21.stream.Measure)[0:measures_needed]:
        for j in i.getElementsByClass(m21.note.Note):
            og_notes_part1.append(j)

    for i in og_notes_part1:
        i.offset = i.getOffsetInHierarchy(full)

    og_part1 = m21.stream.Part(og_notes_part1, id='part1')

    ############
    og_stream = m21.stream.Stream(og_part1)
    og_stream.show('musicxml')