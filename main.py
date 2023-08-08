from jukebox import Jukebox

songs = ["Kuna Kuna", "Herawa Ni", "Inauma", "Vaida", "Sasa Hivi", "McMca", "Dai Dai", "Woman", "Mbona", "Toto", "Kanairo dating", "Wanjapi"] 

# Demo of Jukebox methods
player = Jukebox(songs)
print(player.current_state())
player.play()
print(player.current_state())
player.next()
player.next()
print(player.current_state())
player.pause()
print(player.current_state())
player.next()
player.play()
for i in range(10):
    print(player.current_state())
    player.next()
player.previous()
print(player.current_state())
player.previous()
print(player.current_state())
for i in range(4):
    player.previous()
    print(player.current_state())
