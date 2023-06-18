import vlc

from time import sleep
from settings import URL, VOLUME

if __name__ == '__main__':
    instance = vlc.Instance("--h264-fps=15")  # fix lag
    player = instance.media_player_new()
    media = instance.media_new(URL)
    player.set_media(media)

    player.audio_set_volume(VOLUME)
    player.play()

    playing = True  # Assume play is started or will start soon
    print(f"Playing {URL}")

    while playing:
        sleep(10)
        playing = player.is_playing()
