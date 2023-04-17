print("URL shortener Project in Python")
import pyshorteners as ps

# to use bitly service you should need to API from the bitly website First
#BITLY_API_KEY = "Your API Key Here"
#shortener = ps.Shortener(api_key=BITLY_API_KEY)
shortener = ps.Shortener()
longURL = "https://fmbp.aiou.edu.pk/application/index.php"
tinyShortURL = shortener.tinyurl.short(longURL)
#bitlyShortURL = shortener.bitly.short("https://fmbp.aiou.edu.pk/application/index.php")

print(f"Long URL\n {longURL}")
print(f"Short URL\n {tinyShortURL}")
#print(bitlyShortURL)


