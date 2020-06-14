import praw
import pandas as pd
import csv
from textblob import TextBlob

#from praw.models import MoreComments


reddit=praw.Reddit(client_id='ThExMcDCYM_RCw',client_secret='rBHhVDV4AkGCB2bYkIRp9AiTH9Y',user_agent='MainPro')
fields=['Comment','PostID','Polarity','Subjectivity']

posts = []
p_id = []
subreddit = reddit.subreddit('all')

for post in subreddit.hot(limit=1000):

    posts.append([post.title, post.id, post.num_comments])
    p_id.append([post.id])
posts = pd.DataFrame(posts,columns=['title', 'id', 'num_comments'])

print(posts)

dict=[]

with open('pos_data.csv','w') as new_file:
    csv_writer=csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
    with open('neg_data.csv','w') as new_file:
        csv_writer1=csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
        with open('pos_textblob_data.csv','w') as next_file:
            csv_writer2=csv.writer(next_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
            with open('neg_textblob_data.csv','w') as next_file:
                csv_writer3=csv.writer(next_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
                for post in subreddit.hot(limit=500):
                    submission = reddit.submission(id=post.id)
                    submission.comments.replace_more(limit=0)
    # for top_comment in submission.comments:
    #     print(top_comment.body)

                    csv_writer.writerow(['Comment'])
                    csv_writer1.writerow(['Comment'])
                    csv_writer2.writerow(['PostID'])
                    csv_writer3.writerow(['PostID'])


                    for comment in submission.comments.list():
                        print(comment.body)
                        try:
                            analysis=TextBlob(comment.body)
                            if analysis.sentiment.polarity<-0.3 and analysis.sentiment.subjectivity>0.3:
                                csv_writer1.writerow([comment.body])
                                csv_writer3.writerow([post.id])
                            else:
                                csv_writer.writerow([comment.body])
                                csv_writer2.writerow([post.id])
                        except Exception as e:
                            continue