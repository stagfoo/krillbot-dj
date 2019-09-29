from pydub import AudioSegment

trackbar = AudioSegment.silent(duration=60000)

def trackMaker(f):
  sample = AudioSegment.from_file(f);
  last_5_seconds = sample[-5000:]
  first_5_seconds = sample[5000]
  sampleLoop = sample.fade_in(300)
  return sampleLoop

track1 = trackMaker('lib/lounge/Kit01 80bpm/Drums/Beats/BeatK01 80-02.wav')
track2 = trackMaker('lib/ChartanK01 80A-02.wav')
track3 = trackMaker('lib/Drums_DrumsMix_Love_Song_80.mp3')
track4 = trackMaker('lib/Drums_Vinyl_Love_Song_80.mp3')
track5 = trackMaker('lib/lounge/Kit01 80bpm/Electric Piano/Lines/ChePiK01 80A-04.wav')

trackbar1 = trackbar.overlay(track4, loop=True, gain_during_overlay=-50);
trackbar2 = trackbar1.overlay(track2, loop=True);
trackbar3 = trackbar2.overlay(track3, loop=True);
trackbar4 = trackbar3.overlay(track1, loop=True);
trackbar5 = trackbar4.overlay(track5, loop=True);

# sound1.overlay(sound2, loop=true)
finalTrack = trackbar5 * 5

finalTrack.export("mashup.mp3", format="mp3")
