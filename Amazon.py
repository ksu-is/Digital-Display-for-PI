#The amazon code below comes from the aws site
#requires a user key and password key in a config file provided by in amazon cli

#import Amazon libraries
import boto3
import botocore

#Import OS Library
import os
import sys

#Find platform that is running
system = sys.platform
print(system)

#Pull update file from cloud
BUCKET_NAME = 'strikerfc' # replace with your bucket name
KEY = 'testupgrade.txt' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'upgrade.txt')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

#Open new and old files and compare to determine if upgrade is needed
new_upgrade = open("upgrade.txt","r")
print(new_upgrade.read(8))

old_upgrade = open("oldupgrade.txt","r")
print(old_upgrade.read())

if new_upgrade != old_upgrade:
    os.rename("newvideo.mp4","oldvideo.mp4")
    BUCKET_NAME = 'strikerfc' # replace with your bucket name
    KEY = 'StrikerTest.mp4' # replace with your object key

    s3 = boto3.resource('s3')

    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, 'newvideo.mp4')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
else:
    print("No update")

new_upgrade.close()
old_upgrade.close()
#Replace old update txt with new and delete old video
os.remove("oldupgrade.txt")
os.remove("oldvideo.mp4")
os.rename("upgrade.txt","oldupgrade.txt")

if system.startswith("win"):
    def play_movie(path):
        from os import startfile
        startfile(path)
else:
    print("Nothing")

play_movie(r"C:/Users/cwena/OneDrive/Documents/GitHub/Raspberry-Pi-digital-sign/newvideo.mp4")