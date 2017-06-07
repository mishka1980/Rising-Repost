import kdapi, praw
reddit = praw.Reddit(client_id='asdasd',
                     client_secret='asdasd',
                     user_agent='Does.this.matter.lol',
                     password="asdasd",
                     username= "asdasd")
for submission in reddit.subreddit('all').top('hour',limit=1000):
    if ("redd.it" in submission.url or "imgur" in submission.url):
        print("ID: "+submission.id)
        prevhigh = 0
        highpost = 0
        try:
            for item in kdapi.check(submission.url):
                sub2 = reddit.submission(url=item.link)
                if (sub2 == submission):
                    continue
                sub2score = 0
                try:
                    sub2score = sub2.score
                    if (sub2.score > prevhigh):
                        highpost = sub2
                        prevhigh = sub2.score
                except Exception:
                    pass
                    print(" - ERROR GETTING VOTES OF "+sub2.id)
            if (highpost != 0):
                print(" - HIGH POST: "+highpost.id)
                print("    - SCORE: "+str(highpost.score))
                try:
                    print("    - COMMENT: "+highpost.comments[0].body)
                except Exception:
                    pass
                    print("    - ERROR GETTING COMMMENT")
                try:
                    submission.reply(highpost.comments[0].body)
                    print("    - COMMENT POSTED")
                except Exception:
                    pass
                    print("    - ERROR POSTING COMMENT (banned?)")
            else:
                print(" - NO REPOSTS")
        except Exception:
            print(" - ERROR COMMUNICATING WITH KDAPI")
