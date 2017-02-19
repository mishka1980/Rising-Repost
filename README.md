#Rising-Repost

Many of us have heard of the website reddit, and many of us use it on an everyday basis.

Although reddit is a great website, there is a lot of reposting that goes on, and this is exactly what our app takes advantage of. Although it is not an exploit of Reddit itself, it is most definitely an exploit of Reddit's social system.

First, we look at the "rising" page of the /r/all subreddit, which has the newest and most trending posts of reddit.

We then use an external API to see if any of the images have been posted before.

If so, our script takes the top comment of the previously posted image, and then comments it on the new, "rising" post.

The script is repeated every hour, and the account should gain lots of traction.

You will need the [Praw](https://github.com/praw-dev/praw) and [KarmaDecay-Api](https://github.com/ethanhjennings/karmadecay-api) modules.
