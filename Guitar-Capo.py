# guitar capo
# the notes are  A A# B C C# D D# E F F# G G#
# if there is no capo they remains the same
# if capo is put on a fret the chords with similar structure would change
# for example if capo was put on 1st fret the chord A will become A#

def GuitarCapo (capo, chord):
    Notes = ['A', "A#", 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'] #list of notes
    if chord[0] in Notes: #checks whether or not the chord is in the list
        new_chord_index= int(int(Notes.index(chord))+ int(capo))%12
##        new_chord_index = int(new_chord_index)
##        new_chord_index =new_chord_index%12
        new_chord= Notes[new_chord_index]
        print(new_chord)


Capo= input ("which fret the capo is on? > " )
Chord= input (str("Please enter the base major chord: "))
Chord= Chord.upper()
GuitarCapo(Capo, Chord)
