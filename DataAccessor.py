
import requests
import json

class DataAccessor:
    def get_checkpoint(self):
        f = open("checkpoint", "r") 
        return int(f.readline())
    


    def update_checkpoint(self,checkpoint):
        print("updating checkpoint")
        f = open('checkpoint', "w") 
        f.write(str(checkpoint))

    def get_artist_data(self):
        print("getting artist data")
        url ='https://gq9ukp1155.execute-api.us-west-2.amazonaws.com/dev/artist'
        a = requests.get('https://gq9ukp1155.execute-api.us-west-2.amazonaws.com/dev/artist')
        print(a)


    def update_artist_data(self, artist):
        print("updating artist data")
        print(artist)
        url = 'https://gq9ukp1155.execute-api.us-west-2.amazonaws.com/dev/artist'
        requests.post(url, data=json.dumps(artist)) 

    def update_failed_artist_list(self, artist_name): 
        try:
            f = open('FailedArtists', "a") 
            f.write(str(artist_name) + "\n")
        except:
            print("failed to write to Failed Artist list")

if __name__ == '__main__':

    print("getting artist data")
    url ='https://gq9ukp1155.execute-api.us-west-2.amazonaws.com/dev/artist'
    a = requests.get('https://gq9ukp1155.execute-api.us-west-2.amazonaws.com/dev/artist')
    print(a)