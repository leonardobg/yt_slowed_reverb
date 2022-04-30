import subprocess
import yt_dlp
import re
import time
import argparse
from moviepy.video.io.VideoFileClip import AudioFileClip

def parser_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', type=str, help="Music URL")
    return parser.parse_args()

def download_video(url: str) -> str:
    url = url.split("&")
    url = url[0]
    video_info = yt_dlp.YoutubeDL().extract_info(url,download=False)
    filename = f"{video_info['title']}"
    filename = re.sub('[^0-9a-zA-Z]+', '_', filename)
    options={
    'format':'bestaudio/best',
    'keepvideo':False,
    'outtmpl':filename
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    return filename

def convert_to_mp3(filename: str) -> None:
    clip = AudioFileClip(filename)
    clip.write_audiofile(filename + ".mp3")
    clip.close()

def slow_and_reverb(filename: str) -> None:
    sox = f"sox {filename}.mp3 {filename}_slowed_reverb.mp3 reverb speed 0.8"
    print("Slowing and reverbering your song :)")
    subprocess.run(sox)

def main():
    try:
        args = parser_args()
        url = args.url
        filename = download_video(url)
        convert_to_mp3(filename)
        slow_and_reverb(filename)

        delete_files = f"del {filename} {filename}.mp3"
        
        print("Removing temp files")
        subprocess.run(delete_files,shell=True)
        time.sleep(0.5)
        print("Done!")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()