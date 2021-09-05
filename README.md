# youtube_downloader

This project is about a small app hosted in AWS environment (see the diagram below ) , that allows a user to download a youtube video : the user provides the link of his youtube 
video and the app answers back with an email that contains a presigned url to download the video from an S3 bucket 

The first lambda function (lambda_youtube_download) downloads the video and uploads it to S3 bucket 

The second lambda function (lambda_presigned_url_provider) generates presigned url to download the video from S3 bucket and triggers the SNS service to send the url to the user inside
an email 



![youtube_downloader_diagram](https://user-images.githubusercontent.com/70094057/132139420-c42b239d-8f66-464b-90f1-dd0226b97b85.JPG)


