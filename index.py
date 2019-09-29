from pydub import AudioSegment
from random import sample
from datetime import date
timeline = 60000*2;
trackbar = AudioSegment.silent(duration=60000*2)

drums = [
  'lib/drums/1.mp3',
  'lib/drums/2.wav',
  # 'lib/drums/3.wav',
  'lib/drums/4.wav',
  'lib/drums/5.wav',
  'lib/drums/6.wav',
  'lib/drums/7.wav',
  # 'lib/drums/8.wav',
  'lib/drums/9.wav',
  'lib/drums/10.wav',
]

piano = [
  'lib/piano/1.wav',
  'lib/piano/2.wav',
  # 'lib/piano/3.wav',
  'lib/piano/4.wav',
]

pad = [
  # 'lib/pad/1.wav',
  'lib/pad/2.wav',
  'lib/pad/3.wav',
  'lib/pad/4.wav',
  'lib/pad/5.wav',
  'lib/pad/6.wav',
  'lib/pad/8.wav',
  'lib/pad/9.wav',
  'lib/pad/10.wav',
]

synth = [
  'lib/synth/1.wav',
  'lib/synth/2.wav',
  'lib/synth/3.wav',
  'lib/synth/4.wav',
  'lib/synth/5.wav',
  'lib/synth/6.wav',
  'lib/synth/8.wav',
  'lib/synth/9.wav',
  'lib/synth/10.wav', # good
]

bass = [
  'lib/bass/1.wav',
  'lib/bass/2.wav',
  # 'lib/bass/3.wav',
  # 'lib/bass/4.wav',
  'lib/bass/5.wav',
  'lib/bass/6.wav',
  'lib/bass/8.wav',
  'lib/bass/9.wav',
  'lib/bass/10.wav',
]

noise = [
  'lib/noise/1.wav',

]

drumTrack = sample(drums,1)[0]


def trackMaker(f):
  sample = AudioSegment.from_file(f);
  last_5_seconds = sample[-1000:]
  first_5_seconds = sample[1000]
  sampleLoop = sample.fade_in(300)
  sampleLoop = sample.fade_out(300)
  return sampleLoop

def startLoop():
  tracks = [
    drumTrack,
    sample(pad,1)[0], # don't loop ever time
    sample(noise,1)[0],
    sample(bass,1)[0],
  ]
  print("start loop")
  print(tracks)
  syth = sample(synth,1)[0]
  trackbar = AudioSegment.silent(duration=timeline)
  for track in tracks:
      trackbar = trackbar.overlay(trackMaker(track), loop=True)
  trackbar = trackbar * 1
  trackbar = trackbar.fade_in(5000)
  return trackbar


def midLoop():
  tracks = [
    drumTrack,
    sample(pad,1)[0], # don't loop ever time
    sample(noise,1)[0],
    sample(bass,1)[0],
  ]
  print("middle loop")
  print(tracks)
  syth = sample(synth,1)[0]
  trackbar = AudioSegment.silent(duration=timeline)
  # trackbar = trackbar.overlay( trackbar.overlay(trackMaker(syth), position=timeline/4))
  # trackbar = trackbar.overlay( trackbar.overlay(trackMaker(syth), position=timeline/2))
  # trackbar = trackbar.overlay( trackbar.overlay(trackMaker(syth), position=timeline/4-timeline))
  for track in tracks:
      trackbar = trackbar.overlay(trackMaker(track), loop=True)
  trackbar = trackbar * 1
  return trackbar

def endLoop():
  tracks = [
    drumTrack,
    sample(pad,1)[0], # don't loop ever time
    sample(noise,1)[0],
    sample(bass,1)[0],
  ]
  print("end loop")
  print(tracks)
  syth = sample(synth,1)[0]
  trackbar = AudioSegment.silent(duration=timeline)
  for track in tracks:
      trackbar = trackbar.overlay(trackMaker(track), loop=True)
  trackbar = trackbar * 1
  trackbar = trackbar.fade_out(5000)
  return trackbar

trackbar = startLoop()
trackbar = trackbar.append(midLoop())
trackbar = trackbar.append(midLoop())
trackbar = trackbar.append(endLoop())


trackbar.export("mashup.mp3", format="mp3")
