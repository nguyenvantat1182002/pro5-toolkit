from api import FacebookAPI


cookie = 'sb=8xUVZf51mk6jVQz5PSyTRtzF; datr=8xUVZZD3BDkbIyKCGI23ZiGI; locale=en_US; c_user=100092241635457; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABaQAhaYybSWDBMFFoKij6iRwi0A%22%2C%222%22%3A%22GSwVQBxMAAAWChai2KjRDBYAABV-HEwAABYAFqLYqNEMFgAAFigA%22%2C%2295%22%3A%22HCwAABZAFtjYwlATBRaCoo-okcItAA%22%7D%2C%22d%22%3A%22acbad8d7-42b4-4c9b-b9d9-388b4a4afeb7%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22r1q2sj%22%7D; xs=17%3AHUSy4D8v1n16Vw%3A2%3A1695880713%3A-1%3A7461%3A%3AAcX6Rygjz1pA641duvuwyrfHAau9NE1V49RnBpkDow; usida=eyJ2ZXIiOjEsImlkIjoiQXMxb29id2QwZjhmaCIsInRpbWUiOjE2OTU4ODgwNzN9; wd=1920x963; fr=01h04FE1DVCGbeu9X.AWUZPL5mPi6TSm1OBIgzn7J21_o.BlFTLE.-o.AAA.0.0.BlFTRO.AWVi_BZ2ZjM; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNy4wLjAuMCBTYWZhcmkvNTM3LjM2; _uafec=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F117.0.0.0%20Safari%2F537.36; '
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'

api = FacebookAPI(cookie, user_agent)

pages = api.get_pages()

with open('output.txt', 'a', encoding='utf-8') as file:
    for item in pages:
        id, name = item
        file.write(f'{id}|{name}\n')

print(len(pages))