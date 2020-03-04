
"""blogScraper.py: Display the Google blog's headings at first and then if you want to deep dive into any of the blogs, you can do that - and best part is everything is on cmd - which made you incognito at first sight from your manager/colleague.."""

# -*- coding: utf-8 -*-
"""
@author: Sahil.Bali
@version = "1.0.0"
@maintainer = "Sahil Bali"
@email = "datamansahil@gmail.com"
"""

# using beautifulsoup library in "blogsscraper" conda environment.....

import requests
import re 
from bs4 import BeautifulSoup 
import time



URL = "https://ai.googleblog.com/"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib') 

main_headings = []
dates = []
links = []
authors = []
contents = []

def blog_headings():
	page = BeautifulSoup(requests.get(URL).text, "lxml")
	for headlines in page.find_all("h2"):
		#print(headlines.text.strip())
		main_headings.append(headlines.text.strip())


def blog_dates():
	special_divs = soup.find_all('div',{'class':'published'})
	for text in special_divs:
		download = text.find_all('span',{'class':'publishdate'})
		for text in download:
			#print (text.get_text())
			dates.append(text.get_text())


def blogs_links():
	special_divs = soup.find_all('h2',{'class':'title'})
	for text in special_divs:
		download = text.find_all('a')
		for text in download:
			hrefText = (text['href'])
			#print(hrefText)
			links.append(hrefText)


'''def blog_authors():
	special_divs = text.find_all('div',{'class':'post-content post-original'})
	for text in special_divs:
		downloads = text.find_all('span',{'class':'byline-author'})
		for text in downloads:
			print (text.get_text())
			authors.append(text.get_text())'''




def blog_contents():
	special_divs = soup.find_all('div',{'class':'post-body'})
	for text in special_divs:
		download = text.find_all('div',{'itemprop':'articleBody'})
		for text in download:
			#print (text.get_text())
			contents.append(text.get_text().split("</span>")[-1])



def scraped_detail():
	blog_headings()
	blog_dates()
	blogs_links()
	blog_contents()



def display_results(h,d,l,c):
	for i in range(len(d)):
		print("Blog No. "+str(i))
		print(h[i])
		print(d[i])
		#print(c[i])
		print(l[i])
		print(end = "----------------------------------------------------------------------------------------------------------------------------")
		print(end = "\n\n\n")



def read_content():
	for i in range(1000):
		ques = input("Want to read the content??")
		if ques == "yes" or ques == "Yes" or ques == "y" or ques == "Y" or ques == "yup" or ques == "yep" or ques == "yeh" or ques == "ye":
			try:
				print(f'You have total {len(contents)} blogs available')
				content_no = int(input("Enter the blog no. -  "))
				print(contents[content_no])
			except:
				print(" Unvalid content no., please enter the valid no.")

		else:
			print("Good Bye!")
			break




def main():
	start_time = time.time()
	scraped_detail()
	display_results(main_headings,dates,links,contents)
	print("--- %s seconds ---" % (time.time() - start_time))
	read_content()
	print("--- %s seconds ---" % (time.time() - start_time))




if __name__ == "__main__": 
	main() 