import requests
import os



path = ('path for folders')

for folder in os.listdir(path):
    print("FILES IN FOLDER: ",folder)
    print("==============================")
    for image in os.listdir(path+folder):
        print(image)


#f = open(path, 'rb')
#urls='http://127.0.0.1:8000/uploadMass'
#r=requests.post(urls, files= {'emp_image':f}, data =  {"name":"testname"})
#print(r.status_code)