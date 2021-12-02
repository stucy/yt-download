from pytube import YouTube, Playlist
import argparse
import os
import subprocess

DOWNLOAD_FOLDER = './downloads/'

def download_single(args):
    # Create youtube obj
    yt = YouTube(args.Url)

    # Get stream depending on arguments
    stream = yt.streams.filter(only_video=True) if args.video else yt.streams.filter(only_audio=True)

    # Download video as audio/video file
    stream.first().download(DOWNLOAD_FOLDER)

    if(not args.video and args.mp3):
        mp4 = DOWNLOAD_FOLDER + "%s.mp4" % yt.title
        mp3 = DOWNLOAD_FOLDER + "%s.mp3" % yt.title
        ffmpeg = ('ffmpeg -nostdin -loglevel error -i "{mp4}" "{mp3}" '.format(mp4=mp4, mp3=mp3))
        try:
            subprocess.run(ffmpeg, shell=True)
        except:
            print('Error when converting file to mp3')
        else:
            os.remove(mp4)

    

def download_playlist(args):
    # Create playlist obj
    p = Playlist(args.Url)

    # Loop the videos in the playlist
    for video in p.videos:
        stream = video.streams.filter(only_video=True) if args.video else video.streams.filter(only_audio=True)

        stream.first().download(DOWNLOAD_FOLDER)

        if(not args.video and args.mp3):
            mp4 = DOWNLOAD_FOLDER + "'%s'.mp4" % video.title
            mp3 = DOWNLOAD_FOLDER + "'%s'.mp3" % video.title
            ffmpeg = ('ffmpeg -nostdin -loglevel error -i "{mp4}" "{mp3}" '.format(mp4=mp4, mp3=mp3))
            try:
                subprocess.run(ffmpeg, shell=True)
            except:
                print('\nError when converting file to mp3')
            else:
                os.remove(mp4)


# Check if folder exist if not create it
if(not os.path.isdir('./downloads')):
    os.mkdir('downloads')

# Create the parser
Parser = argparse.ArgumentParser(prog="yt-downloader",usage='%(prog)s [options] path',description='Download youtube videos from url. Default is audio (mp3).')

# Add the arguments
Parser.add_argument('Url', metavar='url', type=str, help='Youtube video/playlist url')
Parser.add_argument('-p', '--playlist', action='store_true', help='use when downloading a playlist')
Parser.add_argument('-v', '--video', action='store_true', help='use when you want to download as a video file and not as an audio file.')
Parser.add_argument('-mp3', action='store_true', help='use when you want to download to download as an mp3 file. (You need ffmpeg installed on you OS)')

# Execute the parse_args() method
args = Parser.parse_args()

try:
    if(args.playlist):
        download_playlist(args)
    else:
        download_single(args)
except:
    print('There was a problem with the download. Please check if the url you are giving as input is valid')
else:
    print('\nDownload finished')
    exit()

# Example urls
#https://www.youtube.com/watch?v=OK0jU-JuQHc&ab_channel=JaredHalley
#https://www.youtube.com/playlist?list=PLMD5fIlZdqAyCBkrtjyoSmukjA50Aq8pg
