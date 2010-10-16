import scikits.audiolab as audiolab
from scikits.audiolab import Format, Sndfile
from scipy.io import wavfile
import time
import math

res = 5000

drumfile = "drugs.wav"

format = Format('wav')
nbuff = 44100
f = Sndfile(drumfile, 'r', format, 2, nbuff)
input = Sndfile("luv.wav", 'r', format, 2, nbuff)

o_fmt = Format('wav', 'pcm16')
f = Sndfile(drumfile, 'r', format, 2, nbuff)
output = Sndfile("945output.wav", 'w', format, f.channels, f.samplerate)


f = Sndfile(drumfile, 'r', format, 2, nbuff)
t_frame = f.read_frames(res) 
f = Sndfile(drumfile, 'r', format, 2, nbuff)
print "Mixing the gumbo.."
i=0
while(i < ((f.nframes))):

    if(i%f.nframes == 0):
        f = Sndfile(drumfile, 'r', format, 2, nbuff)

    if(i%10000 == 0):
        print str(i) + "/" + str(f.nframes) + " miksd!"
    d_frame = f.read_frames(res)

    i_frame = input.read_frames(res)
    if(abs(i_frame[0][0]) >= abs(d_frame[0][0])):
        t_frame[:][:] = i_frame[:][:]
    else:
        t_frame[:][:] = d_frame[:][:]
        #t_frame[:][:] = [0][0]

    output.write_frames(t_frame)
    i = i + res

output.close()
print "Okay, done!"
