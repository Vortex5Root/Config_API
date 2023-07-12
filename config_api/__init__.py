import json

from os import walk

from pathlib import Path

class Config():

    main_dir : Path
    file_name_ : str

    config_ : dict

    def __init__(self,name):
        self.path = "./config/"
        self.file_name = name

    @property
    def path(self):
        if self.main_dir is not None:
            return self.main_dir

    @path.setter
    def path(self,value):
        if self.main_dir is not None:
            value = self.main_dir / value
        else:
            value = Path(value)
        if not self.main_dir.exists():
            self.main_dir.mkdir()
        self.main_dir = value
    
    @property
    def file_name(self):
        return self.file_name_
    
    @file_name.setter
    def file_name(self,value):
        check = self.path / "{}.json".format(value)
        if not check.exists():
            with open(check,"w") as file:
                file.write("{}")
                file.close()
        self.file_name_ = value

    def load(self,folder= ""):
        if folder != "":
            self.path = folder
        file = self.path / self.file_name
        with open(file,"r") as config:
            self.config = json.loads(config.read())
            config.close()

    def save(self,folder=""):
        if folder != "":
            self.path = folder
        file = self.path / self.file_name
        with open(file,"w") as config:
            config.write(json.dumps(config))
            config.close()        
        