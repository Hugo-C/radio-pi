import vlc

from settings import URL, VOLUME

if __name__ == '__main__':
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(URL)
    player.set_media(media)

    player.audio_set_volume(VOLUME)
    player.play()
    input("press enter to quit")
    player.stop()
