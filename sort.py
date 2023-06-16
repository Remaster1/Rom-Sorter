import pathlib
import re
import shutil
from filetypes import file_signature
import os
class Sorter:

    _path: str 
    _patterns: dict
    _files: list 
    
    def __init__(self, path: str, patterns: dict) -> None:
        self._path = path
        self._patterns = patterns
        self._files = list(pathlib.Path(path).iterdir())
    
    def move_to_dir(self, file: pathlib.Path, name: str) -> None:
        game_folder = file.name.split('.')[0]
        roms_path = pathlib.Path(f'{self._path}/{name}/{game_folder}')
        if file.is_dir():
            return
        if not roms_path.is_dir():
            roms_path.mkdir(parents=True)
        try:
            shutil.move(file,roms_path)
        except shutil.Error:
            console = input(f"Rewrite file {file.name}? (y/n)")
            if console == "y" or "yes":
                os.remove(str(roms_path)+'/'+str(file.name))
                shutil.move(file,roms_path)
            else:
                print("Skipped")

    def read_signature(self, file: pathlib.Path) -> str:
        """Read file signature"""
        if re.search("\.cue",file.name) != None:
            return 
        with open(file,"rb") as file:
                while True:
                    data = file.read(36)
                    print(data)
                    for i in file_signature:
                        if bytes.hex(data) == i.lower():
                            return file_signature.get(i)
                        
    def sort_roms(self) -> None:
        """Sorting all roms by patterns"""
        for pattern in self._patterns:
            for file in self._files:
                if re.search(pattern=pattern,string=file.name) and (self._patterns.get(pattern) == "Undefined"):
                    pattern =  self.read_signature(file)
                    self.move_to_dir(file, pattern)
                    if re.search(pattern='\.cue',string=file.name.split(".")[0]+'.cue'):
                        file = pathlib.Path(self._path+"/"+file.name.split(".")[0]+'.cue')
                        self.move_to_dir(file,pattern)
                    continue
                elif re.search(pattern=pattern,string=file.name) != None:
                    self.move_to_dir(file, self._patterns.get(pattern))
                    
    
    
                
# TODO: Write Cue Reader    
class CueReader:
    _path: str
    def __init__(self, path) -> None:
        pass
            