import json

import boto3 as boto3
import requests
import os
from PIL import Image

bucket = os.getenv("aws_bucket", default=None),
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("aws_access_key", default=None),
    aws_secret_access_key=os.getenv("aws_access_key", default=None)
)

with open("input/image.json", "r") as file:

    for line in file:
        body = json.loads(line)

        # download image
        response = requests.get(body['url'])
        open("img/"+body['name'], "wb").write(response.content)

        # thumbnail
        # image = Image.open('img/rappi.png')
        # image.thumbnail((250, 250))
        # image.save('img/rappi_250x250.png')

        # upload to S3
        with open("img/"+body['name'], "rb") as img:
            s3.upload_fileobj(img, bucket, "thumbnail/" + body['name'], ExtraArgs={'ACL': 'public-read'})
            print(img.name)
