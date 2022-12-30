import requests

url_tmple = "https://dd.b.pvp.net/latest/set%d/en_us/img/cards/%s"
img_name_tmple = "0%d%s%03d-full.png"
sets = 3
imgs = 100
dict = "art/"
regions = ["FR", "SI", "NX", "DE", "PZ", "IO", "BW", "MT"]

for reg in regions:
    for set_id in range(1, sets+1):
        for img in range(1, imgs+1):
            img_name = (img_name_tmple % (set_id, reg, img))
            url = (url_tmple % (set_id, img_name))
            print(url)
            r = requests.get(url, allow_redirects=True)
            open(dict + img_name, 'wb').write(r.content)
