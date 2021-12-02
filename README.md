# Python script for downloading youtube videos with provided url

## Dependencies:
- pytube
- ffmpeg (if you want mp3)

## How to run:

```
python script.py url
python3 script.py url
```

## Options:

```
-h --help - to see the help options in the terminal
-v -video - download the as a video file not as an audio file
-p -playlist - use when the provided url is a playlist
-mp3 - If you want to convert the audio files to mp3 (needs ffmpeg to be installed on your os)