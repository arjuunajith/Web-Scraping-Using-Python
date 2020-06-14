import praw
import pandas as pd
import csv
from textblob import TextBlob

from praw.models import MoreComments


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

with open('pos_data.csv','a') as new_file:
    csv_writer_pos=csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
    with open('neg_data.csv','a') as new_file:
        csv_writer_neg=csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
        with open('all_data.csv','a') as new_file:
            csv_writer_all=csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
            with open('negpost_id.csv','a') as new_file:
                csv_writer_id=csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
        # with open('pos_textblob_data.csv','w') as next_file:
        #     csv_writer2=csv.writer(next_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
        #     with open('neg_textblob_data.csv','w') as next_file:
        #         csv_writer3=csv.writer(next_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator = '\n')
                for post in subreddit.hot(limit=1000):
                    submission = reddit.submission(id=post.id)
                    submission.comments.replace_more(limit=0)
                # for top_comment in submission.comments:
                #     print(top_comment.body)

                    # csv_writer_all.writerow(['Comment'])
                    # csv_writer_pos.writerow(['Comment'])
                    # csv_writer_neg.writerow(['Comment'])

                    #csv_writer2.writerow(['PostID'])
                    #csv_writer3.writerow(['PostID'])
                    csv_writer_id.writerow([post.id])

                    print(post.id)
#                     t=0
#                     n=0
#                     p=0
#                     for comment in submission.comments.list():
#                         try:
#                             #print(comment.body)
#                             t=t+1
#                             #csv_writer_all.writerow([comment.body])
#                             analysis=TextBlob(comment.body)
#                             if analysis.sentiment.polarity<0 and analysis.sentiment.subjectivity>0.2:
#                                 #csv_writer_neg.writerow([comment.body])
#                                 n=n+1
#                                 #csv_writer3.writerow([post.id])
#                             else:
#                                 #csv_writer_pos.writerow([comment.body])
#                                 p=p+1
#                                 #csv_writer2.writerow([post.id])
#                         except Exception as e:
#                             continue
#
#                 print()
#                 print()
#                 print()
#                 print()
#                 print()
#                 print('Neg Ratio : ',n/t)
#                 print('Pos Ratio : ',p/t)
#                 if n/t>0.1:
#                     print('Post ID : ',post.id)
#                     csv_writer_id.writerow([post.id])
#
#
# print()
# print()
# print()
# print()
# print()

# print('Total Scraped Comments : ', p+n)
# print('Positive Scraped Comments : ', p)
# print('Negative Scraped Comments : ', n)
# print('Ratio of Negative to Positive : ',n/p)
