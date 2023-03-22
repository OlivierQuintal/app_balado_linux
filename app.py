# premièrement installer pytube sur l'orfinateur avec pip install pytube


# importing packages
from pytube import YouTube
from flask import Flask 
from flask import render_template
from flask import request
import os

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/telecharger')
def telechargement():
    lien = request.args.get('lienMusique')
    yt = YouTube(lien)
  
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    

    # replace destination with the path where you want to save the downloaded file
    destination = "./musiques"
    
    # download the file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    # result of success
    print(yt.title + " has been successfully downloaded.")
    return render_template('index.html')




  
# url input from user
# yt = YouTube(input("Enter the URL of the video you want to download: \n>> "))


if __name__ == "__main__":
	app.run(debug=True)
