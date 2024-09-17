from music import playlist


def print_playlist():
    for b_index, band in enumerate(playlist, 1):
        name, songs = band
        for song_num, song in songs:
            print(f"{b_index}:{song_num} {name} - {song}")

def print_song(p_bnumber, p_snumber):
    try:
        band_name = playlist[p_bnumber-1][0]
        song_name = playlist[p_bnumber-1][1][p_snumber-1][1]
    except IndexError:
        print("This song does not exist in playlist.")
    else:
        print(f"\n{band_name} - {song_name} playing now...")

while True:
    print_playlist()
    current_play = input("\nSelect a song to play using number:(1:1) ")
    try:
        band_number = int(current_play[0])
        song_number = int(current_play[2])
    except ValueError:
        print("The format is not correct, it should be like (1:1)")
    else:
        print_song(band_number, song_number)
    change = input("\nPress C to change the song or any key to quit APP: ")
    if change == "C":
        continue
    break
print("Good Bye! ")