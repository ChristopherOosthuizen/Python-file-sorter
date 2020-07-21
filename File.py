import os
import shutil


class File:
    def __init__(self,name):
        r = open(name)
        self.directory = r.readline().strip()
        self.folders = r.readline().strip().split(",")
        self.dict = {}
        line = r.readline().strip()
        while line != "":
            spliter = line.split("-")
            self.dict[spliter[0]] = spliter[1]
            line = r.readline().strip()

    # return the count of files in specified directory
    def get_count(self):
        return len(os.listdir(self.directory))

    # setup the code if its not present
    def setup(self):
        for s in self.folders:
            if not (s in os.listdir(self.directory)):
                os.mkdir(self.directory + "/" + s)
        self.sort()

    def sort(self):
        while self.unsorted():
            for s in os.listdir(self.directory):
                if not (s in self.folders):
                    self.move_file(s)

    def unsorted(self):
        return len(self.folders) != self.get_count()

    def move_file(self, name):
        f = os.path.splitext(name)
        if os.path.isdir(self.directory+"/"+name):
            location = self.dict["'dir'"]
        else:
            if f[1] in self.dict:
                location = self.dict[f[1]]
            else:
                location = self.dict["'other'"]
        location = self.directory+"/"+location
        shutil.move(self.directory+"/"+name, location)
