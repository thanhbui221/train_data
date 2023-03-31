import requests
import os
from bs4 import BeautifulSoup
c = 0
with open(f"{os.getcwd()}/raw/hocvien_urls.txt", "r") as f:
    url_list = f.readlines()
    for url in url_list:
        res = requests.get(url=str(url))
        soup = BeautifulSoup(res.content,  "html.parser")
        p_tags = soup.find_all("p")
        filename = str(url).split("/")[-2]
        if not os.path.exists(f"{os.getcwd()}/clean"):
            os.makedirs(f"{os.getcwd()}/clean")
        out_file = os.path.join(f"{os.getcwd()}/clean", f"{filename}.txt")
        with open(out_file, "w") as f:
            f.writelines([p_tag.text for p_tag in p_tags])