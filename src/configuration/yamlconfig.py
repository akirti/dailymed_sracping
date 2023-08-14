import yaml
import os

class YamlReader:
    def __init__(self,path=None,fileName=None):
        self.fileName=fileName
        self.path =path if path is not None else os.getcwd()
        print(self.path)

    '''
        Load Yaml config file.
    '''
    def load_config(self,path=None,fileName=None):
        path =path if path is not None else self.path
        full_path = path + "/" + fileName
        data = None
        with open(full_path, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
            print("Read successful")
        print(data)
        return data

if __name__ == '__main__':
    yr = YamlReader("../../",'application.yaml')
    yr.load_config(None,'application.yaml')
