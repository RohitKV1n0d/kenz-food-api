import requests, json
import pyimgur
#remove file 
import os
from app import app

UPLOAD_FOLDER = 'static/img/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CLIENT_ID = "2d3158d36137249"
# PATH = "C:/Users/USER/Desktop/Hash IT/kenz-food-api/kenz-food-api/kenz-api/static/img/uploads/Group_84logo.PNG"
img_filename ="hash-text-removebg-preview.png"
im = pyimgur.Imgur(CLIENT_ID)
basedir = os.path.abspath(os.path.dirname(__file__))
uploaded_image = im.upload_image(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename), title="Uploaded with PyImgur")
os.remove(os.path.join(basedir, app.config['UPLOAD_FOLDER'], img_filename))

print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.size)
print(uploaded_image.type)



