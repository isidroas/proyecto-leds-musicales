#!/usr/bin/env python3

import mido 
import sys
mid = mido.MidiFile('sultans.mid')
#print(mid.tracks)
sel = sys.argv[1]
sel=int(sel)
#mid.tracks = [mid.tracks[sel]]
#mid.save('sultans_2.mid')

track = mid.tracks[sel]
test = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11 ]]
#track = []
tabla=[]
for msg in track:
	if msg.type == 'note_on':
		print(msg)
		tabla.append([msg.note, msg.time])
		
print(tabla)

import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(tabla)
