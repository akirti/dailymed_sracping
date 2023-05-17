import yaml

class YamlReader:
    def __init__(self,path=None,fileName=None):
        self.fileName=fileName
        self.path=path
with open("tutswiki.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")
print(data)