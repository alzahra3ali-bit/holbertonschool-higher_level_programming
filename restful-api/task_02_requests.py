#!/usr/bin/python3
import requests
import csv
def fetch_and_print_posts():
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: ", req.status_code)
    if (status_code == 200):
      postes = req.json()
      for post in postes:
        print(post['title'])
def fetch_and_save_posts():
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    postes = req.json()
    fpost = []
    for post in postes:
        temp = { 
            id':post['id']',
            title':post['title']',
            body':post['body']']
        }
        fpost.append(temp)
with open('posts.csv','w',newline='',encoding='utf-8') as f:
    header = ['id','title','body']
    writer = csv.DictWriter(f, fildename=headers)
    writer.writeheader()
    writer.writerows(fpost)
