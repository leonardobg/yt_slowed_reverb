import subprocess
import yt_dlp
import re
import time
import argparse
from moviepy.video.io.VideoFileClip import AudioFileClip

def parser_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', type=str, help="Music URL")
    parser.add_argument('-o','--output', type=str, help="Output file name")
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

def slow_and_reverb(filename: str, output: str) -> None:
    sox = f"sox -S {filename}.mp3 {output} reverb speed 0.8"
    print("Slowing and reverbering your song :)")
    subprocess.run(sox)

def main():
    try:
        args = parser_args()
        url = args.url
        filename = download_video(url)
        output = args.output or f"{filename}.slowed&reverb.mp3"
        delete_files = f"del {filename} {filename}.mp3"
        convert_to_mp3(filename)
        time.sleep(1)
        subprocess.run("cls",shell=True)
        slow_and_reverb(filename,output)
        time.sleep(1)
        subprocess.run("cls",shell=True)
        
        print("Removing temp files")
        subprocess.run(delete_files,shell=True)
        time.sleep(0.5)
        print("Done! Enjoy your song")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
