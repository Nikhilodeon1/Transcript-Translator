from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session, abort
import json
from youtube_transcript_api import YouTubeTranscriptApi
import requests
app = Flask(__name__)
app.secret_key = "|\|||<|-|||_"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def stuff():
    videoLink = request.form['video_link']
    #videoLink = 'https://www.youtube.com/watch?v=Ey_vGhau7ho'
    vLink = videoLink.split('watch?v=')
    dict1 = {
        "data": YouTubeTranscriptApi.get_transcript(vLink[1])
    }
    with open('vid.json', 'w') as file:
        json.dump(dict1, file)
    return render_template('results.html', list1=YouTubeTranscriptApi.get_transcript(vLink[1]), id=vLink[1])

@app.route('/translate', methods=['POST'])
def translate():
    language = request.form['language']
    videoLink = request.form['video_link']
    vLink = videoLink.split('watch?v=')
    headers = {
        "content-type": "application/x-www-form-urlencoded",
	    "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "cd00cc840emsh92d438f7f956fa0p194762jsnc96c3e80b846",
	    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    with open('vid.json') as file:
        file1 = json.load(file)
        payload = "q="
        for elm in file1['data']:
            var = elm['text'].replace(' ', '%20')
            payload += var + "=+="
        payload += "&target={}&source=en".format(language)
        response = requests.request("POST", url, data=payload, headers=headers)
        dict1 = response.text
        list5 = dict1.split('translatedText":"')
        list6 = list5[1].split('= ="}]}')
        list7 = list6[0].split("= =")
        return render_template('html.html', id=vLink[1], language=language, list1=list7, file=file1["data"])