
"""blogScraper.py: Display the Google blog's headings at first and then if you want to deep dive into any of the blogs, you can do that - and best part is everything is on cmd - which made you incognito at first sight from your manager/colleague.."""
# self: is nothing but it is treated as instance of an object - https://www.youtube.com/watch?v=M1BAlDufqao

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



class Google_blogs:

	def __init__(self):
	 	self.URL = "https://ai.googleblog.com/"
	 	self.r = None
	 	self.soup = None
	 	self.main_headings = list()
	 	self.dates = list()
	 	self.links = list()
	 	self.authors =list()
	 	self.contents = list()


	def beautiful_soup(self):
		self.r = requests.get(self.URL)
		self.soup = BeautifulSoup(self.r.content, 'html5lib')


	def blog_headings(self):
		page = BeautifulSoup(requests.get(self.URL).text, "lxml")
		for headlines in page.find_all("h2"):
			#print(headlines.text.strip())
			self.main_headings.append(headlines.text.strip())


	def blog_dates(self):
		special_divs = self.soup.find_all('div',{'class':'published'})
		for text in special_divs:
			download = text.find_all('span',{'class':'publishdate'})
			for text in download:
				#print (text.get_text())
				self.dates.append(text.get_text())


	def blogs_links(self):
		special_divs = self.soup.find_all('h2',{'class':'title'})
		for text in special_divs:
			download = text.find_all('a')
			for text in download:
				hrefText = (text['href'])
				#print(hrefText)
				self.links.append(hrefText)



	def blog_contents(self):
		special_divs = self.soup.find_all('div',{'class':'post-body'})
		for text in special_divs:
			download = text.find_all('div',{'itemprop':'articleBody'})
			for text in download:
				#print (text.get_text())
				self.contents.append(text.get_text().split("</span>")[-1])



	def scraped_detail(self):
		self.beautiful_soup()
		self.blog_headings()
		self.blog_dates()
		self.blogs_links()
		self.blog_contents()



	def display_results(self):
		for i in range(len(self.dates)):
			print("Blog No. "+str(i))
			print(self.main_headings[i])
			print(self.dates[i])
			#print(contents[i])
			print(self.links[i])
			print(end = "----------------------------------------------------------------------------------------------------------------------------")
			print(end = "\n\n\n")



	def read_content(self):
		for i in range(1000):
			ques = input("Want to read the content??")
			if ques == "yes" or ques == "Yes" or ques == "y" or ques == "Y" or ques == "yup" or ques == "yep" or ques == "yeh" or ques == "ye":
				try:
					print(f'You have total {len(self.contents)} blogs available')
					content_no = int(input("Enter the blog no. -  "))
					print(self.contents[content_no])
				except:
					print(" Unvalid content no., please enter the valid no.")

			else:
				print("Good Bye!")
				break




def main():
	start_time = time.time()
	obj = Google_blogs()
	obj.scraped_detail()
	obj.display_results()
	print("--- %s seconds ---" % (time.time() - start_time))
	obj.read_content()
	print("--- %s seconds ---" % (time.time() - start_time))




if __name__ == "__main__": 
	main() 