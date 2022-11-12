from fastapi import FastAPI
from helpers import extractor

app = FastAPI()


'''
GET /{video_id}/formats
'''
@app.get('/{video_id}/formats')
def get_url(video_id: str):
    data = extractor.get_info(video_id)
    return {
        'status': True,
        'meta': { 'video_id': video_id },
        'data': data
    }