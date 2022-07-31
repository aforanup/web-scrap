from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


url = "https://proshore.eu/resources/"

options = ChromeOptions()
options.headless = True

driver = Chrome(
    executable_path="./chromedriver/chromedriver",
    options=options,
)
driver.get(url)

count = 0
while driver.find_element(By.CLASS_NAME, "playground-title"):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Divs = driver.find_element(
        By.CLASS_NAME,
        "playground-title",
    )
    print(count)
    if count == 1000:
        print("end")
        break
    else:
        count += 1
        continue

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

blogs = soup.find("div", {"class": "playground-list"})
blog_images = blogs.find_all("div", {"class": "playground-image"})
all_read_time = blogs.find_all("div", {"class": "playground-read-time"})
all_title = blogs.find_all("h4", {"class": "playground-title"})
all_description = blogs.find_all("div", {"class": "playground-excerpt"})
author_images = blogs.find_all("div", {"class": "playground-author-image"})
author_names = blogs.find_all("div", {"class": "playground-author-name"})
author_designations = blogs.find_all("div", {"class": "playground-author-description"})


blog_data = []

count = 0
for blog_image in blog_images:
    img_src = blog_image.find("img").attrs["src"]
    blog_data.append({})
    blog_data[count].update({"blog_image": img_src})
    count += 1

count = 0
for read_time in all_read_time:
    blog_data[count].update({"read_time": read_time.text})
    count += 1

count = 0
for title in all_title:
    blog_data[count].update({"title": title.text})
    count += 1

count = 0
for description in all_description:
    blog_data[count].update({"description": description.text})
    count += 1

count = 0
for author_image in author_images:
    img_src = author_image.find("img").attrs["src"]
    blog_data[count].update({"author_image": img_src})
    count += 1

count = 0
for author_name in author_names:
    blog_data[count].update({"author_name": author_name.text})
    count += 1

count = 0
for author_designation in author_designations:
    blog_data[count].update({"author_designation": author_designation.text})
    count += 1

print(blog_data, len(blog_data))
with open("scrapped_data.json", "w") as f:
    f.write(json.dumps(blog_data))
