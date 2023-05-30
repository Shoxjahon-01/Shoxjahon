import requests
import json
def video_yuklash(link):
    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"
    video_id = link[-11:]
    querystring = {"videoId":video_id}

    headers = {
        "X-RapidAPI-Key": "7d02d25f3amsh428a3ea7e144132p1b23adjsn1878a89c049d",
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return (response.json()['videos']['items'][0]['url'])

