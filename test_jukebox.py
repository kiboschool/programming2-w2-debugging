import unittest

from gradescope_utils.autograder_utils.decorators import weight
from jukebox import Jukebox

songs = ["Kuna Kuna", "Herawa Ni", "Inauma", "Vaida", "Sasa Hivi", "McMca", "Dai Dai", "Woman", "Mbona", "Toto", "Kanairo dating", "Wanjapi"] 

class TestJukebox(unittest.TestCase):

    @weight(1)
    # Make sure that all variables are set correctly 
    def test_jukebox_constructor(self):
        player = Jukebox(songs)
        assert player.is_playing == False
        assert player.current_song == 0
        assert player.songs == songs

    @weight(1)
    # Make sure that playing a new jukebox shows the first song
    def test_play(self):
        player = Jukebox(songs)
        player.play()
        assert player.current_state() == "Playing: Kuna Kuna"

    @weight(1)
    # Make sure that pausing a jukebox shows Paused as the current state
    def test_pause(self):
        player = Jukebox(songs)
        player.play()
        player.pause()
        assert player.current_state() == "Paused"

    @weight(0.5)
    # Make sure that calling next moves us to the next song
    def test_next(self):
        player = Jukebox(songs)
        player.play()
        player.next()
        assert player.current_state() == "Playing: Herawa Ni"

    @weight(0.5)
    # Make sure that calling previous moves us back to the previous song
    def test_previous(self):
        player = Jukebox(songs)
        player.play()
        player.next()
        player.previous()
        assert player.current_state() == "Playing: Kuna Kuna"

    @weight(1)
    # Make sure that calling previous when on the first song moves us to the last song
    def test_previous_wrap(self):
        player = Jukebox(songs)
        player.play()
        for i in range(len(songs)):
            player.previous()
        player.previous()
        assert player.current_state() == "Playing: Wanjapi"

    @weight(1)
    # Make sure that calling next when on the last song moves us to the previous song
    def test_next_wrap(self):
        player = Jukebox(songs)
        player.play()
        for i in range(len(songs)):
            player.next()
        player.next()
        assert player.current_state() == "Playing: Herawa Ni"

    @weight(2)
    # Make sure that sharing the list of songs returns a brand new list:
    def test_share_songs_returns_new_list(self):
        player = Jukebox(songs)
        new_list_of_songs = player.copy_song_list()
        assert new_list_of_songs == player.songs
        assert id(new_list_of_songs) != id(player.songs)

if __name__ == "__main__":
    unittest.main()
