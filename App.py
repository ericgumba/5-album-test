import WikipediaScraper as ws
import RYMScraper as rs
import DataAccessor as ds

import time
class App:
    def __init__(self, genre):
        self.genre = genre
        self.data_accessor = ds.DataAccessor()
        self.rym_scraper = rs.RYMScraper
        self.wiki_scraper = ws.WikipediaScraper
    
    def reset_counter(self):
        self.data_accessor.update_checkpoint(0)

    def get_artists(self, link):
        return self.wiki_scraper.get_artist_list(link)

    def add_artist(self,artist_name):
        artist = self.rym_scraper.get_artist_data(artist_name)
        print(artist)
        print("================")
        if artist and artist['acclaimed_albums_count'] > 0:
            artist['genre'] = self.genre
            self.data_accessor.update_artist_data(artist)
        else:
            self.data_accessor.update_failed_artist_list(artist_name)

    def execute(self, url): 
        print("executing")
         
        artist_list = self.wiki_scraper.get_artist_list(url)
        checkpoint = self.data_accessor.get_checkpoint()
        print("ARTIST LIST: ", artist_list)

        for i in range(checkpoint, len(artist_list)): 
            print("Getting data for: ", artist_list[i])
            checkpoint += 1
            self.add_artist(artist_list[i])
            self.data_accessor.update_checkpoint(checkpoint) 
            time.sleep(10)