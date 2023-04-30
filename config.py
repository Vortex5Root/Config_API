import json

from os import walk

from pathlib import Path

def msg_fix(msg):
    return msg.replace('    ','')

class config():

    def __init__(self):
        self.path = Path('./configs/')
        if not self.path.exists():
            self.path.mkdir()

        #print(self.configs)
        self.woking_path = ''

    @property
    def configs(self):
        return self.list_configs()

    def add_config(self,data,config,dir = ''):
        if dir == '': dir = self.woking_path
        msg = ''

        chp= self.check_working_path(dir)
        if not chp:
            (self.path / dir).mkdir()
            msg += msg_fix(f"\
                    [Config] new path «{(self.path / dir).as_posix()}» created\
                    ")

        json_object = ''
        try:
            json_object = json.dumps(data)
        except:
            return msg_fix(f"\
                    [Config-Error] no dump json variable \
                    [Config-Error] data: {data}\
                    ")

        new_config = open((self.path / dir/ config).as_posix()+'.json','w')
        new_config.write(json_object)

        msg += msg_fix(f"\
                [Config] new file {config}.json in path\
                ")
        return msg

    def remove_config(self,config,dir = ''):
        if dir == '': dir = self.woking_path
        file = (self.path / dir / config+'.json')
        if file.exists():
            file.rm()
            return msg_fix(f"\
                    [Config] file «{(self.path / dir).as_posix()+config+'.json'}» removed\
                    ")
        return msg_fix(f"\
                [Config-Error] file «{(self.path / dir).as_posix()+config+'.json'}» not existend\
                ")

    def get_config(self,config,dir = ''):
        if dir == '': dir = self.woking_path
        chp= self.check_working_path(dir)
        if not chp:
            return self.not_exists_path(dir)
        try:
            return json.loads(open((self.path / dir).as_posix()+'/'+config+'.json', "r").read())
        except:
            return msg_fix(f"\
                    [Config] file: {(self.path / dir).as_posix()}/{config}.json \
                    [Config-Error] unexistents \
                    ")

    def not_exists_path(self,dir):
        return msg_fix(f"\
            [Config-Error] Path '{(self.path / dir).as_posix()}' not found\
            ")

    def check_working_path(self,dir):
        if not (self.path / dir).exists():
            return False
        return True

    def list_configs(self):
        configs = []
        for (dirpath, dirnames, filenames) in walk('./configs'):
            for i in filenames:
                if str(i).split('.')[1].lower() == 'json':
                    configs.append([dirpath,str(i)])
        return configs

cfg = config()
