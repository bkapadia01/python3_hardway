class Song(object):
    def __init__(self, lyrics):
        self.singing = lyrics
    
    def sing_song(self):
        for line in self.singing:
            print(line)


happy_bday = Song(["happy bdayto you",
                   "i dont want to get sued",
                   "so i'll stop here"])

bulls_parade = Song(["they rally aorund the family",
                     "with pockets full of shells"])

happy_bday.sing_song()
bulls_parade.sing_song()
print("-" * 20)
# ------ # ----- #
## adv. of above is that you can call the song by calling the sing_song function, below you'll have to write the song each time
class Song(object):
    def __init__(self, lyrics):
        for line in lyrics:
            print(line)


happy_bday = Song(["happy bday to you",
                   "happy bday to you",
                   "how old are you"])

bulls_parade = Song(["before i lose my mind ",
                     "lose my mind again"])

