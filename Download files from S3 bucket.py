# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:27:59 2020

@author: Harshal
"""
import datetime
import os
import boto3

'''You can configure the AWS access login credentials by uncommenting  the below code
or you can use the more secure way by using AWS CLI 
'''

#os.environ["BUCKET_NAME"] = "some_bucket"
#os.environ["AWS_ACCESS_KEY"] = "some_access_key"
#os.environ["AWS_SECRET_KEY"] = "some_secret"


DAY = datetime.datetime.today().strftime("%d")
MONTH = datetime.datetime.today().strftime("%m")
YEAR = datetime.datetime.today().strftime("%Y")
PATH = 'The path sould be same as the file structure in AWS S3 bucket'

def creat_folders():
    try:
        os.makedirs(path) #creating the required directories as per AWS S3 bucket.
    except WindowsError:
        pass

def download_all_objects_in_folder():
    creat_folders()
    try:        
        s3_resource = boto3.resource('s3')
        my_bucket = s3_resource.Bucket('<your_bucket_name>')
        for objects in my_bucket.objects.filter(Prefix=PATH): #specifying the folder path
            for var in objects.key.split('/'):
                 if var == '<any path values>'
                     continue
                 else:
                     my_bucket.download_file(objects.key, PATH+var)
    except Exception as e:
        print(e)
    
download_all_objects_in_folder()
