import vlc
url = 'http://radio.garden/api/ara/content/listen/KTSP4urQ/channel.mp3'

instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(url)
player.set_media(media)

player.audio_set_volume(25)
player.play()
input("press enter to quit")
player.stop()
