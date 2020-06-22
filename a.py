from discord_webhook import DiscordWebhook, DiscordEmbed
import time , requests , shutil
subreddit = "https://www.reddit.com/r/subreddit/"#edit this line
webhook = DiscordWebhook(url='discord webhook url')#edit this line
def send(ur):
    embed = DiscordEmbed(title='', description='', color=242424)
    embed.set_image(url=ur)
    webhook.add_embed(embed)
    response = webhook.execute()
def makeUrl(afterID, subreddit):
        newUrl = subreddit.split('/.json')[0] + "/.json?after={}".format(afterID)
        return newUrl
def splitUrl(imageUrl):
        if 'jpg' or 'webm' or 'mp4' or 'gif' or 'gifv' or 'png' in imageUrl:
            return imageUrl.split('/')[-1]
def fetch():
    subJson = ''
    if subJson:
        url = makeUrl(subJson['data']['after'], subreddit)
    else:
        url = makeUrl('', subreddit)
    subJson = requests.get(url, headers={'User-Agent': 'MyRedditScraper'}).json()
    post = subJson['data']['children']
    imageUrl = (post[0]['data']['url'])
    send(imageUrl)
while(1):
    fetch()
    time.sleep(3600)
