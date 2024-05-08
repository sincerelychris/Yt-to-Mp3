import os
import certifi
import ssl
from pytube import YouTube
from moviepy.editor import *

def youtube_to_mp3(url, output_path='output.mp3'):
    # Set SSL context to use certifi's certificate
    ssl._create_default_https_context = ssl._create_unverified_context
    os.environ['SSL_CERT_FILE'] = certifi.where()

    # Download video from YouTube
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()

    # Download the video to a temporary mp4 file
    temp_video_path = stream.download(filename='temp_video.mp4')

    # Load the video file using moviepy
    video_clip = VideoFileClip(temp_video_path)

    # Extract audio from the video
    audio_clip = video_clip.audio

    # Write the audio to the output file
    audio_clip.write_audiofile(output_path)

    # Close the clips to free up resources
    video_clip.close()
    audio_clip.close()

    # Success message
    print(f"Downloaded and converted video to MP3 successfully. File saved as: {output_path}")

# Example usage (replace 'YOUR_VIDEO_URL' with the actual YouTube video URL)
youtube_to_mp3('https://www.youtube.com/watch?v=C-Nic1Q3ZaU')

