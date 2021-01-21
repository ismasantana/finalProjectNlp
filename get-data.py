#https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
import praw
import sys

def uprintT(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

reddit = praw.Reddit(
     client_id="0nzFl2jzvYnLTQ",
     client_secret="JWfAyFGDn6qKC5NI4hzuFhf80kKQ2A",
     user_agent="script:nlp:Ismasantana",
     username="Ismasantana",
    password="nlpproject"
     
)
#Random_Acts_Of_Amazon, depression,news, depression_help, ForeverAlone
forum = "ForeverAlone" 
subreddit = reddit.subreddit(forum)

for submission in subreddit.hot(limit=100000):
    f =  open("comments_" + forum + ".txt", 'a', encoding='utf-8') 
    #print(submission.title)  # Output: the submission's title
    #print(submission.score)  # Output: the submission's score
    #print(submission.id)     # Output: the submission's ID 
    f.write('[${URL}] ' + submission.url + '\n')    # Output: the URL the submission points to
    f.write(submission.selftext.replace("\n", " ").strip() + '\n')
    submission.comments.replace_more(limit=None)        
    comments = submission.comments.list()
    
    for comment in comments:
        #try:
        f.write(comment.body.replace("\n", " ").strip() + "\n")
        #except:
        #    print("Erro!\n");