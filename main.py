import requests


def main():


    def get_lyrics(artist, title):
        url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('lyrics', 'Lyrics not found')
        else:
            return 'Error fetching lyrics'


    song_name = input("name of the song: ")
    artist_name = input("name of the artist: ")

    lyrics = get_lyrics(artist_name, song_name)

    lyrics_list = lyrics.split('\n')

    print(lyrics)



if __name__ == "__main__":
    main()



# if __name__ == "__main__":
#     artist = "Coldplay"
#     title = "Yellow"
#     lyrics = get_lyrics(artist, title)
#     print(lyrics)