import requests
from bs4 import BeautifulSoup
base_url = 'https://www.yelp.com/search?cflt=restaurants&find_loc='
loc = 'New York,NY'
current_page = 0

while current_page < 101:
	print(current_page)
	url = base_url + loc + '&start='+ str(current_page)
	yelp_r = requests.get(url)
	yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
	businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
	file_path = 'yelp-{loc}-2.txt'.format(loc=loc)
	with open(file_path, 'a') as textfile:
		businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
		for biz in businesses:
			title = biz.findAll('a', {'class': 'biz-name'})[0].text
			print(title)
			try:
				address = biz.findAll('address')[0].text.lstrip()
			except:
				address = None
			print(address)
			try:
				phone = biz.findAll('span', {'class': 'biz-phone'})[0].text.lstrip()
			except:
				phone = None
			print(phone)
			print('\n')
			page_line = '{title}\n{address}\n{phone}\n\n'.format(
					title=title,
					address=address,
					phone=phone,
				)
			textfile.write(page_line)
	current_page += 10




	


"""



print(yelp_r.status_code) # prints 200




file_path = 'yelp-{loc}.txt'.format(loc=loc)
with open(file_path, 'a') as textfile:
	businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
	for biz in businesses:
		title = biz.findAll('a', {'class': 'biz-name'})[0].text
		print(title)
		address = biz.findAll('address')[0].text.lstrip()
		print(address)
		phone = biz.findAll('span', {'class': 'biz-phone'})[0].text.lstrip()
		print(phone)
		print('\n')
		page_line = '{title}\n{address}\n{phone}\n\n'.format(
				title=title,
				address=address,
				phone=phone,
			)
		textfile.write(page_line)




print(yelp_soup.findAll('li', {'class': 'regular-search-result'}))

print(yelp_soup.findAll('a', {'class': 'biz-name'}))
#print(yelp_soup.prettify())

for name in yelp_soup.findAll('a', {'class': 'biz-name'}):
	print(name.text)

for link in yelp_soup.findAll('a'):
	print(link)

"""