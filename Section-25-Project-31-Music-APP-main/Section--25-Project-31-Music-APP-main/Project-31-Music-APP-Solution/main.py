from music import playlist
from ascii_art import logo

def print_playlist():
    for artist_index, t_song in enumerate(playlist,1):
        artist, songs = t_song
        for song_num,song in songs:
            print(f"{artist_index}:{song_num} {artist} - {song}")
print(logo)
while True:
    # Print Default list
    print_playlist()
    current_play = input("\nSelect a song to play using number:(1:1) ")
    print(f"\n{playlist[int(current_play[0])-1][0]} - {playlist[int(current_play[0])-1][1][int(current_play[2])-1][1]} playing now....")


    change = input("\nPress C to change song or any letter to quit APP: ")
    if change == "C":
        continue
    break

print("Good Bye!")



