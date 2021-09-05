#importing the pytube package
import pytube
import json
import boto3
import os

def lambda_handler(event, context):
    #create a client for S3 access
    s3_client = boto3.client('s3' , region_name = "eu-west-3" ,
                  config=boto3.session.Config(s3={'addressing_style': 'path'}, signature_version='s3v4'))

    #creating a pytube object called youtube from the given URL (enter the url of the file you want to download)
    url = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    youtube = pytube.YouTube(url)

    #creating a name variable using the youtube object property "title"
    #for saving it later
    name = youtube.title.replace(" ","-").lower()

    #chossing the stream as youtube videos are available in different streams
    #e.g. different resolutions, etc.
    video = youtube.streams.first()

    #finally downloading the youtube video and saving it to specified path / name
    video.download(output_path="/tmp", filename=name)

    fname=os.listdir("/tmp")[0]
    response = s3_client.upload_file("/tmp/"+fname, "processed-youtube-videos", name+".mp4")
