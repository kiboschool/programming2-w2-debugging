class Jukebox:
    def __init__(shelf, songs):
        self.songs = songs
        self.current_song = 0
        self.is_playing = False

    def play(self):
        self.is_playing = True

    def pause(self):
        self.is_playing == False

    def next(self):
        self.current_song += 1

    def previous(self):
        self.current_song -= 1

    def current_state(self):
        if self.is_playing:
            return "Playing: " + self.songs[self.current_song]
        else:
            return "Paused"

    def copy_song_list(self):
        return self.songs