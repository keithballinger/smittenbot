from lxml import html
import requests
page = requests.get('http://smittenicecream.com/menu/')

tree = html.fromstring(page.content)

flavors = tree.xpath("//span[@class='name']/span/text()")
message = '\n'.join(flavors)

print 'Flavors:', flavors

from slackclient import SlackClient

token = 'xoxb-23465111906-LUJJs8YHOSmpKgf6JU4dMLEC'
sc = SlackClient(token)

print sc.api_call("api.test")
print sc.api_call("channels.info", channel="1234567890")
print sc.api_call(
   "chat.postMessage", channel="#general", text=message,

   username='smittenbot', icon_emoji=':robot_face:'
)