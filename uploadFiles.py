import requests
import os



path = ('path for folders')

for folder in os.listdir(path):
    print("FILES IN FOLDER: ",folder)
    print("==============================")
    urls='http://127.0.0.1:8000/uploadFolder'
    r=requests.post(urls, data =  {"folder":folder, "sex":folder[1]})
    print(r.status_code)
    print(folder[1])
    for image in os.listdir(path+folder):
        index = int(image[7:9])
        
        #if folder == "WM_219":
            
        print(image)
        f = open(path+folder+'/'+image, 'rb')
        urls='http://127.0.0.1:8000/uploadMass'
        r=requests.post(urls, files= {'imageFile':f}, data =  {"folder":folder, "filename":image, "index":index})
        print(r.status_code)


#f = open(path, 'rb')
#urls='http://127.0.0.1:8000/uploadMass'
#r=requests.post(urls, files= {'emp_image':f}, data =  {"name":"testname"})
#print(r.status_code)
