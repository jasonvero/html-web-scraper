
# urllib grabs the page itself
from urllib.request import urlopen as uReq

# bs4 parses html text
from bs4 import BeautifulSoup as soup


# url
my_url = 'https://www.newegg.com/p/pl?d=graphics+cards'

# opening up connection, grabbing the page
uClient = uReq(my_url)

# offloads the content into a variable
page_html = uClient.read()

# with any web client, since this is an open internet connect, 
# we want to close the client once done with it
uClient.close()


# html parsing

page_soup = soup(page_html,  "html.parser")

# show's the header of the page
	# page_soup.h1

# traversing the html
# convert each graphics card and convert to CSV file

# grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})

# how many containers
	# len(containers)

# index 0

# had issues scraping with this index
	# containers[0]

# set synthax to html (ctrl + shift + p)
# jsbeauitifer 


# had issues scraping with this index
	# containers[6]

# this index finally worked
	# containers[12]

# for loop to find the brand of gpu
for container12 in containers:
	brand = container12.div.div.a.img["title"]
	if brand is not None:
		print("brand: " + brand)
	else: 
		print("no brand name")


	title_container = container12.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	if product_name is not None:
		print("product name: " + product_name)
	else:
		print("no product name")

# need to resume trouble shooting from here
python Beautiful_Soup_Web_Scraper_GPU_tutorial.py




	
	


