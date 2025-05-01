from moviepy import *
from .pTube import save_vidio_of_utube
from typing import Optional



def vidioConvert(url_vidio: str, out_audio: Optional[str] = None):

    video = VideoFileClip(save_vidio_of_utube(url_vidio))  # В кавычках указать путь к видео
    #pdb.set_trace()
    if out_audio is None:
        video.audio.write_audiofile("audio.mp3")  # В кавы чках указать название итогового аудиофайла
    else:
        video.audio.write_audiofile(out_audio)  # В кавы чках указать название итогового аудиофайла
