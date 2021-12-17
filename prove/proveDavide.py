from cleanedFunction import cleaned
from googletrans import Translator

#x = 'RT @fausername1: @fakeusername2 just bought 30.6 BTC from https://fakeesceafafa.com &amp; I am hating the crash\n Hope it recovers so... '


x = "@matteosalvinimi @mariogiordano5 Cosa hai fatto per evitargli la Censura? Nulla come per evitare a noi il #supergreenpass. Scompari #Lega"
x = cleaned(x)

translator = Translator()
x = translator.translate(x, dest='en', src='it').text
print(x)
print(cleaned(x))


