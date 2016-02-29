from slackbot.bot import Bot

from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re


def reply(message):
    from lxml import html
    import requests
    page = requests.get('http://smittenicecream.com/menu/')
    tree = html.fromstring(page.content)
    span_text_flavors = tree.xpath("//span[@class='name']/span/text()")
    flavors = '\n'.join(span_text_flavors)
    message.reply(flavors)


@respond_to('(.*)', re.IGNORECASE)
def hi(message, something):
    reply(message)


@listen_to('(.*)smitten')
def help(message, something):
    reply(message)


def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()