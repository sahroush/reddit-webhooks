from discord_webhook import DiscordWebhook, DiscordEmbed
import time , requests  , random
subreddits = ["https://www.reddit.com/r/hentai/"];
seen = [[] , [] , []]
def start():
    global seen
    try:
        ch = open("cache.txt" , "r+");
        content = ch.readlines();
        for i in content:
            seen+=[i[:len(i)-1]]
        ch.close()
    except:
        ch = open("cache.txt" , "w+");
        ch.close()
def send(ur , ttl , x):
    global seen
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/724571331198320671/ibTQ6I91fbfSrdRS6mK2KDFRbbQRkwlG7uslG5H0R-o7OMurCSApFAEhSNQzGjChrDsL')
    embed = DiscordEmbed(title=ttl, description='', color=242424)
    embed.set_image(url=ur)
    webhook.add_embed(embed)
    webhook.execute()
    seen[x] += [ur];
    if (len(seen[x]) > 1000):
        seen[x] = seen[x][500:]
    #end()
def makeUrl(afterID, subreddit):
        return subreddit.split('/.json')[0] + "/.json?after={}".format(afterID)
def fetch(x , y = 0):
    url = makeUrl('', subreddits[x])
    subJson = requests.get(url, headers={'User-Agent': 'MyRedditScraper'}).json()
    post = subJson['data']['children']
    if(y > len(post)):
        return
    imageUrl = (post[y%len(post)]['data']['url'])
    imageTitle = (post[y%len(post)]['data']['title'])
    if(imageUrl in seen[x] or not('jpg' in imageUrl or 'webm' in imageUrl or 'mp4' in imageUrl or 'gif' in imageUrl or 'gifv' in imageUrl or 'png' in imageUrl)):
        fetch(x , y + 1)
    else :
        send(imageUrl , imageTitle , x)
def run():
    while(1):
        #end()
        fetch(0);
def end():
    global seen
    ch = open("cache.txt" , "w+");
    for i in seen:
        ch.write(i + '\n')
    ch.close()
#start()
run()
