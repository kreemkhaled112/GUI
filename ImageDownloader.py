import requests 
from bs4 import BeautifulSoup
from time import sleep
headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '1.25',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Microsoft Edge";v="121.0.2277.128", "Chromium";v="121.0.6167.184"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'viewport-width': '974',
}
cookie = 'presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1695742680083%2C%22v%22%3A1%7D;fr=0p454w9w8Co4U2EQ4.AWVCLWYK5eEXQJ23xCyVdtOR_IM.BlEvqc.xH.AAA.0.0.BlEvrJ.AWUidgAOquE;xs=44%3AX2Hf1mc_b_eKSw%3A2%3A1695742635%3A-1%3A-1;datr=nPoSZZK_8lmHk2eWabsib-0v;c_user=61552005803530;locale=en_GB;wd=929x881;m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYOFsCOmkoTBRaUuIeX5v4bAA%22%2C%222%22%3A%22GSwVQBxMAAAWARag65fRDBYAABV-HEwAABYAFqDrl9EMFgAAFigA%22%2C%2295%22%3A%22HCwAABYEFq6y8YgOEwUWlLiHl-b-GwA%22%7D%2C%22d%22%3A%22760c62d4-cbce-4360-87fe-da8abc50bd47%22%2C%22s%22%3A%221%22%2C%22u%22%3A%22300853%22%7D;sb=nPoSZRtG1FVX1qJkNzBf1grK;ps_n=0;ps_l=0;m_page_voice=61552005803530'
cookies = {'cookie': cookie }
with open(f"id.txt", "r") as f:
        i = f.readlines()
        for id in i :
            id = id.strip()
            response = requests.get(f'https://mbasic.facebook.com/profile.php?id={id}', cookies=cookies, headers=headers)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    href = [tag.get('href') for tag in soup.find_all('a', href=lambda x: x and x.startswith('/photo.php?'))]
                    response = requests.get( f'https://mbasic.facebook.com/{href[1]}' , cookies=cookies, headers=headers)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    href = soup.select_one('img[src^="https://scontent.fcai20-3.fna.fbcdn.net"]').get('src')
                    response = requests.get(href)
                    if response.status_code == 200:
                        with open(f"pages_functions\Public\man_photo\{id}.jpg", "wb") as f:
                            f.write(response.content)
                        print(f"Done {id}")
                        sleep(5)
                except Exception as e: print(f"Failed {id} {e}") ; sleep(5)

