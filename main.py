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


    def detect_language(text):
        url = "https://libretranslate.com/detect"
        payload = {"q": text}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()[0].get('language', 'Language not detected')
        else:
            return 'Error detecting language'


    song_name = input("name of the song: ")
    artist_name = input("name of the artist: ")

    lyrics = get_lyrics(artist_name, song_name)

    lyrics_list = lyrics.split('\n')

    language_of_song = detect_language(lyrics)

    print(lyrics)




if __name__ == "__main__":
    main()

