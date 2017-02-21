import kdapi, praw
reddit = praw.Reddit(client_id='CLIENTID', client_secret='CLIENTSECRET',user_agent='Does.this.matter.lol',password="PASSWORD",username= "USERNAME")
for submission in reddit.subreddit('all').rising(limit=100):
    if ("redd.it" in submission.url or "imgur" in submission.url):
        prevhigh = 0
        highpost = 0
        for item in kdapi.check(submission.url):
            sub2 = reddit.submission(url=item.link)
            if (sub2 == submission):
                continue
            if (sub2.score > prevhigh):
                highpost = sub2
            prevhigh = sub2.score
        if (highpost != 0):
            submission.reply(highpost.comments[0].body)
