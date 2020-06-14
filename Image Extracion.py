import praw
import pandas as pd
import csv
import shutil
import requests
import random
import os
from textblob import TextBlob

from praw.models import MoreComments


reddit=praw.Reddit(client_id='ThExMcDCYM_RCw',client_secret='rBHhVDV4AkGCB2bYkIRp9AiTH9Y',user_agent='MainPro')
fields=['Comment','PostID','Polarity','Subjectivity']

posts = []
p_id = []
p_url= []
subreddit = reddit.subreddit('all')

for post in subreddit.hot(limit=100):
    posts.append([post.title, post.id, post.num_comments, post.url])
    p_id.append([post.id])
    p_url.append([post.url])
posts = pd.DataFrame(posts,columns=['title', 'id', 'num_comments', 'URL'])

print(posts)

i=0

filenames=os.listdir("./train/")

for post in subreddit.hot(limit=100):
    #submission = reddit.submission(id=post.id)
    pid = post.id
    url = str(post.url)
    url=url[-3:]
    #print(url)
    print(i)
    try:
        if url == 'jpg' or url == 'png':
            response = requests.get(post.url) #, stream=True)
            #if response.status_code == 200:
            with open('./train/app_'+ str(pid) +'.png', 'wb') as f:
                #'cat.'+i+'.jpg'
                # r.raw.decode_content = True
            #shutil.copyfileobj(response.raw, f)
                f.write(response.content)
            #del response
            i=i+1
        else:
            continue
    except Exception as e:
            continue
