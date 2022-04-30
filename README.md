
# yt_slowed_reverbered

Slow and reverb your songs using their youtube link  
Working only on Windows atm, Linux version coming soon™



## Prerequisites

Tested only on Python 3.9.6  
Install yt_dlp and moviepy

```
  pip install yt_dlp
  pip install moviepy
```
Install Sox  
Download it from here https://sourceforge.net/projects/sox/ and add it to your PATH  
Download these 2 DLL http://www.videohelp.com/download/sox-14.4.0-libmad-libmp3lame.zip and paste it on your Sox directory

## Usage

```
slow_reverb.py -u video url -o output file
if you dont use the -o parameter, it will save 
named as the video_title.mp3

Example:
slow_reverb.py -u 'https://www.youtube.com/watch?v=w8KQmps-Sog' -o uprising_slowed_reverb.mp3
slow_reverb.py -u 'https://www.youtube.com/watch?v=w8KQmps-Sog'

```


## TODO

- Add Linux support
- Add function to download songs from spotify
- Choose the directory of your output file
- Download entire playlists, slow and reverb them


