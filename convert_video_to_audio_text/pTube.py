from rutube import Rutube
import os
from typing import Optional
import pdb

def save_vidio_of_utube(url: str, out_path: Optional[str] = None) -> str:


    rt = Rutube(url)

    # Get a list of videos
    # Each object is the same video but with different resolution
    #print(rt.playlist)  # [Nature 4k (272x480), Nature 4k (408x720), Nature 4k (608x1080)]

    # Get a list of available resolutions
    #print(rt.available_resolutions)  # [480, 720, 1080]

    # Download a video with specific resolution and save it to the current directory
    # rt.get_by_resolution(720).download()

    # Download a video with the best quality and save it to specific directory
    # Path may be absolute or relative
    # rt.get_best().download('downloads/saved-videos')
    #pdb.set_trace()
    # Получаем путь для сохранения указанный пользователем
    file_path = ''  # 'C:\\Users\\user\\Documents\GUI\\'
    if file_path:
        #video_path = rt.get_by_resolution(480)._build_file_path(file_path)
        video_path = rt.get_best()._build_file_path(file_path)
    else:
        #video_path= f"{os.getcwd()}\\{rt.get_by_resolution(480)._build_file_path()}"
        video_path = f"{os.getcwd()}\\{rt.get_best()._build_file_path()}"

    rt.get_best().download(file_path)
    #rt.get_by_resolution(480).download(file_path)

    return video_path
    # ***************************************************************
    # Проверка что загрузка завершена

    #rt.get_best()._build_file_path()
    # print("Текущая директория:", os.getcwd())
    # print()
