class Song:
    song_lyrics=()
    def __init__(self, title="",author="",lyrics=()):
        self.__title=title
        self.__author=author
        self.__lyrics=lyrics
        #self.lines=lines
        print(f"New Song made {self.__title} by artist/group {self.__author}")

    def set_title(self, new_title):
        self.__title=new_title
        return self

    def set_author(self, new_author):
        self.__author=new_author
        return self

    def set_lyrics(self, new_lyrics):
        self.__lyrics=new_lyrics
        return self

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_lyrics(self):
        return self.__lyrics

    def sing(self, max_lines=-1):
        print(self.__title, self.__author,sep="-")
        if max_lines==-1:
            song_lyrics=self.__lyrics
        else:
            song_lyrics=self.__lyrics[:max_lines]
        for line in song_lyrics:
            print(line,sep="\n")
        return self

    def yell(self,max_lines=-1):
        print(self.__title, self.__author, sep="-")
        if max_lines == -1:
            song_lyrics = self.__lyrics
        else:
            song_lyrics = self.__lyrics[:max_lines]
        for line in song_lyrics:
            c = ""
            for item in line:
                c+=str(item).upper()
            print(c)
        return self

class Rap(Song):

    def break_it(self,max_lines=-1,drop="yeah"):
        print(self.get_title(), self.get_author(), sep="-")
        song_lyrics = self.get_lyrics()
        if max_lines != -1:
            song_lyrics = song_lyrics[:max_lines]
        for word in song_lyrics:
            my_list=word.split()
            new_list=""
            for i in my_list:
                new_list+=i+" " +drop.upper()+" "
            print(new_list)
        return self

ziemelmeita=Song("Ziemeļmeita","Jumprava",["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
# print(ziemelmeita)
# print(type(ziemelmeita))
print(ziemelmeita.sing(1).yell())
print(f"{'#'*50}")
print(ziemelmeita.sing(1).yell().sing().yell())

zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","Garu, tālu ceļu veicu"])
zrap.break_it(10, "yah")