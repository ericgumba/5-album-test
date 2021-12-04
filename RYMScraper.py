from typing import Text
import requests
from bs4 import BeautifulSoup
import re
from requests.api import head
def get_num_ratings(html):
	ratings = html.find_all('div', class_="ratingText")[1].text
	ratings = ratings.replace("(","")
	ratings = ratings.replace(")","")
	ratings = ratings.replace(",","")
	return int(ratings)

def get_rating(html):
	return  html.find("div" ,class_="rating").text
def create_album(html):
	return html

class RYMScraper:

	def get_link_data(url):
		artist_obj = {}
		artist_obj["albums"] = []
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
		}  
		try:

			response = requests.get(
				url=url, headers=headers
			) 

			soup = BeautifulSoup(response.content, 'html.parser')

			artist_name = soup.find('h1', class_="artistHeadline").text
			print("ARTISTE", artist_name)
			artist_obj["name"] = artist_name
			albums = create_album(soup.find_all("div", {"data-type" : "lp"}))
		except:
			print("Failed to get artist data")
			return None


		number_of_acclaimed_albums = 0
		total_score = 0
		for album in albums:
			album_obj = {}
			# title_elements = col_element.find_all("a") 
			
			print("=======================================") 
			title = album.find("div" ,class_="albumTitle")
			album_obj["title"] = title.text
			ratings = album.find_all("div" ,class_="ratingRow")
			print(title.text)
			try:
				num_of_ratings = get_num_ratings(ratings[1])

				critic_rating = get_rating(ratings[0])
				user_rating = get_rating(ratings[1])
				album_obj["rating"] = user_rating
				print("critic rating: " + critic_rating)
				print("user rating: " + user_rating)
				print("num of ratings: ", num_of_ratings)
				if int(user_rating) >= 80 and int(num_of_ratings) > 50:
					artist_obj["albums"].append(album_obj)
					number_of_acclaimed_albums += 1 
					total_score += int(user_rating)
			except:
				print("couldnt get rating") 
		print("number of critically acclaimed albums " + str(number_of_acclaimed_albums)) 
		artist_obj["acclaimed_albums_count"] = number_of_acclaimed_albums
		# critical acclaim

		return artist_obj


	def get_artist_data(artist_name):
		if "albumoftheyear" in artist_name:
			return RYMScraper.get_link_data(artist_name)
		print(artist_name)

		artist_obj = {}
		artist_obj["albums"] = []
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
		}  
		artist_url = artist_name.replace("-","%20")

		try:
			response = requests.get(
				url="https://www.albumoftheyear.org/search/artists/?q=" + artist_url, headers=headers
			) 
			soup = BeautifulSoup(response.content, 'html.parser')
			
			# print(soup)
			
			title = soup.find('a', href = re.compile (r'.*artist.*' + artist_name + '.*'))
			# print(title)
			artist= re.findall(r"/artist.*"+artist_name+"/", str(title))[0]
			# print(artist)
			response = requests.get(
				url="https://www.albumoftheyear.org/" + artist , headers=headers
			) 

			soup = BeautifulSoup(response.content, 'html.parser')

			artist_name = soup.find('h1', class_="artistHeadline").text
			print("ARTISTE", artist_name)
			artist_obj["name"] = artist_name
			albums = create_album(soup.find_all("div", {"data-type" : "lp"}))
		except:
			print("Failed to get artist data")
			return None


		number_of_acclaimed_albums = 0
		total_score = 0
		for album in albums:
			album_obj = {}
			# title_elements = col_element.find_all("a") 
			
			print("=======================================") 
			title = album.find("div" ,class_="albumTitle")
			album_obj["title"] = title.text
			ratings = album.find_all("div" ,class_="ratingRow")
			print(title.text)
			try:
				num_of_ratings = get_num_ratings(ratings[1])

				critic_rating = get_rating(ratings[0])
				user_rating = get_rating(ratings[1])
				album_obj["rating"] = user_rating
				print("critic rating: " + critic_rating)
				print("user rating: " + user_rating)
				print("num of ratings: ", num_of_ratings)
				if int(user_rating) >= 80 and int(num_of_ratings) > 50:
					artist_obj["albums"].append(album_obj)
					number_of_acclaimed_albums += 1 
					total_score += int(user_rating)
			except:
				print("couldnt get rating") 
				try:
					num_of_ratings = get_num_ratings(ratings[0])
					user_rating = get_rating(ratings[0])

					album_obj["rating"] = user_rating 
					if int(user_rating) >= 80 and int(num_of_ratings) > 50:
						artist_obj["albums"].append(album_obj)
						number_of_acclaimed_albums += 1 
						total_score += int(user_rating)
				except:
					print("really couldnt get ratings")
				
		print("number of critically acclaimed albums " + str(number_of_acclaimed_albums)) 
		artist_obj["acclaimed_albums_count"] = number_of_acclaimed_albums
		# critical acclaim

		return artist_obj
	
if __name__ == "__main__":
	a = RYMScraper.get_artist_data("nujabes")
	print(a)