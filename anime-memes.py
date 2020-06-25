from discord_webhook import DiscordWebhook, DiscordEmbed
import time , requests  , random
subreddits = ["https://www.reddit.com/r/Animemes/" , "https://www.reddit.com/r/wholesomeanimemes/" , "https://www.reddit.com/r/anime_irl/"];seen=[]
def start():
    global seen
    ch = open("cache.txt" , "w+");
    ch.close()
    ch = open("cache.txt" , "r+");
    content = ch.readlines();
    ch.close()
    for i in content:
        seen+=[i[:len(i)-1]]
def send(ur , ttl):
    global seen
    webhook = DiscordWebhook(url='webhook's url')  #edit this line
    embed = DiscordEmbed(title=ttl, description='', color=242424)
    embed.set_image(url=ur)
    webhook.add_embed(embed)
    webhook.execute()
    seen += [ur];
    end()
    time.sleep(1800)
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
def run(x = 100 , y = 100 , z = 100):
    while(x + y + z):
        end()
        if(x):
            x-=1;
            fetch(0);
        if(y):
            y-=1
            fetch(1)
        if(z):
            z-=1;
            fetch(2);
def end():
    global seen
    ch = open("cache.txt" , "w+");
    for i in seen:
        ch.write(i + '\n')
    ch.close()
start()
run()
