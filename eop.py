import scikits.audiolab as audiolab
from scikits.audiolab import Format, Sndfile
from scipy.io import wavfile
import time
import math
#iT = 10
#f = 15000
#fs = 16000
#x = scipy.cos((2*scipy.pi*f/fs)*scipy.arange(fs*T))
#audiolab.play(x, fs)

res = 2000 

drumfile = "amen2.wav"

format = Format('wav')
nbuff = 44100
f = Sndfile(drumfile, 'r', format, 2, nbuff)
input = Sndfile("flash_nointro.wav", 'r', format, 2, nbuff)
#f = Sndfile("drum.wav", format,)
print "Numframes: " + str(f.nframes)
max = -9999999999
avg = 0
for i in range(f.nframes):
    #print f.read_frames(1)
    frame = f.read_frames(1)
    if abs(frame[0][0]) > max:
        max = abs(frame[0][0])
    avg = avg + abs(frame[0][0]) 
avg = avg / f.nframes

print "Average: " + str(avg)
print "New max: " + str(max)

o_fmt = Format('wav', 'pcm16')
f = Sndfile(drumfile, 'r', format, 2, nbuff)
output = Sndfile("output.wav", 'w', format, f.channels, f.samplerate)



f = Sndfile(drumfile, 'r', format, 2, nbuff)
t_frame = f.read_frames(res) 
f = Sndfile(drumfile, 'r', format, 2, nbuff)
print "Mixing the gumbo.."
i=0
times = 20
while(i < ((f.nframes) * times)):

    if(i%f.nframes == 0):
        f = Sndfile(drumfile, 'r', format, 2, nbuff)

    if(i%10000 == 0):
        print str(i) + "/" + str(f.nframes * times) + " miksd!"
    d_frame = f.read_frames(res)

    i_frame = input.read_frames(res)
    if(abs(d_frame[0][0]) >= avg):
        t_frame[:][:] = i_frame[:][:]
    else:
        #t_frame[:][:] = d_frame[:][:]
        #t_frame[:][:] = d_frame[:][:]
        t_frame[:][:] = [0][0]

    output.write_frames(t_frame)
    i = i + res

output.close()
print "Okay, done!"
