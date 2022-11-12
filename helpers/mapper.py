'''
return an optimized object of the necessary video details
'''
def get_formats(videoObj):
    formats = [
        {
            'id':    f['format_id'],
            'note':  f['format_note'],
            'label': f['format'],
            'ext':   f['ext'],
            'size':  f['filesize'],
            'url':   f['url'],
            'is_audio': True if 'audio only' in f['format'] else False
        } for f in videoObj['formats']
    ]

    return {'title': videoObj['title'], 'formats': formats }