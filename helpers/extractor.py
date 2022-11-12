import youtube_dl
from helpers.mapper import get_formats


'''
extract video download links
'''
def get_info(video_id):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    with ydl:
        data = ydl.extract_info('https://www.youtube.com/watch?v=%s' % (video_id), download=False)
        if data != None:
            return get_formats(data)
    return {}