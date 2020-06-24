from discord_webhook import DiscordWebhook, DiscordEmbed
import time , requests , shutil , random
subreddits = ["https://www.reddit.com/r/Animemes/" , "https://www.reddit.com/r/wholesomeanimemes/" , "https://www.reddit.com/r/anime_irl/"];seen=[]
def send(ur , ttl):
    global seen
    webhook = DiscordWebhook(url='web hook url') #edit this line
    embed = DiscordEmbed(title=ttl, description='', color=242424)
    embed.set_image(url=ur)
    webhook.add_embed(embed)
    webhook.execute()
    seen += [ur];time.sleep(3)
def makeUrl(afterID, subreddit):
        return subreddit.split('/.json')[0] + "/.json?after={}".format(afterID)
def fetch(x , y = 0):
    url = makeUrl('', subreddits[x])
    subJson = requests.get(url, headers={'User-Agent': 'MyRedditScraper'}).json()
    post = subJson['data']['children']
    imageUrl = (post[y%len(post)]['data']['url'])
    imageTitle = (post[y%len(post)]['data']['title'])
    if(imageUrl in seen or not('jpg' in imageUrl or 'webm' in imageUrl or 'mp4' in imageUrl or 'gif' in imageUrl or 'gifv' in imageUrl or 'png' in imageUrl)):
        fetch(x , y + 1)
    else :
        send(imageUrl , imageTitle)
while(1):
    for i in range(3):
        fetch(i , random.randint(1 , 100000));
    if(len(seen) > 10000):
        seen = []
