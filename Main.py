# -*- coding: utf-8 -*- 
import WikipediaScraper as ws
import RYMScraper as rs
import DataAccessor as ds
import App
import sys 

def execute_app(genre,url):

    app = App.App(genre)
    
    if (input("Reset counter? y/n: ") == 'y'):
        app.reset_counter()

    print("executing for: ",genre)
    print("executing for: ",url)

    app.execute(url)

def main(genre = None, url = None):  

    if not genre or not url:
        print("executing by command line")
        if len(sys.argv) != 3:
            print('invalid')
            return

        execute_app(sys.argv[1], sys.argv[2] )

        # app = App.App(str(sys.argv[1]))
        
        # if (input("Reset counter? y/n: ") == 'y'):
        #     app.reset_counter()

        # print("executing for: ",sys.argv[1])
        # print("executing for: ",sys.argv[2])

        # app.execute(str(sys.argv[2]))
    else:
        print("executing by args")
        execute_app(genre, url )

        

def test(): 
    # d = ds.DataAccessor("hard-rock" , "https://en.wikipedia.org/wiki/List_of_hard_rock_musicians_(N%E2%80%93Z)")
 
    app = App.App("experimental")
    app.add_artist("lingua-ignota") 

    # app.add_artist("https://www.albumoftheyear.org/artist/670-bjork/")

    # a = app.get_artists("https://en.wikipedia.org/wiki/List_of_hip_hop_groups")

    # print(a)

if __name__ == "__main__":   
    # test() 
    # main("dance-pop","https://en.wikipedia.org/wiki/List_of_dance-pop_artists")
    # main("pop","https://en.wikipedia.org/wiki/List_of_power_pop_artists_and_songs")
    # main("punk","https://en.wikipedia.org/wiki/List_of_post-punk_bands")
    # main("pop-punk","https://en.wikipedia.org/wiki/List_of_pop-punk_bands")
    # main("pop-punk","https://en.wikipedia.org/wiki/List_of_pop-punk_bands")
    main("dance-rock","https://en.wikipedia.org/wiki/List_of_dance-rock_artists")



# Main.py r-and-b https://en.wikipedia.org/wiki/List_of_R%26B_musicians
    # hip-hop
    # https://en.wikipedia.org/wiki/List_of_hip_hop_musicians

 