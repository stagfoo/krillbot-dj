from pydub import AudioSegment

# DRUM
drumSample = AudioSegment.from_mp3("lib/75bmp_drum.mp3");
last_5_seconds = drumSample[-5000:]
first_5_seconds = drumSample[5000]
drumSampleLoop = drumSample.append(last_5_seconds, crossfade=1500)
awesome = drumSampleLoop * 2

# drumSample = AudioSegment.from_mp3("lib/75bmp_drum.mp3");
# last_5_seconds = drumSample[-5000:]
# first_5_seconds = drumSample[5000]
# drumSampleLoop = drumSample.append(last_5_seconds, crossfade=1500)
# awesome = drumSampleLoop * 2


# sound1.overlay(sound2, loop=true)

awesome.export("mashup.mp3", format="mp3")
