# Author: Tracy Vierra
# Date Created: 3/22/2022
# Date Modified: 3/22/2022

# Description:

# Usage:

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(len(res.text))
print(res.text[:500])
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
	    playFile.write(chunk)
playFile.close()

