from pathlib import Path

def get_files(folder):
    return list(Path(folder).glob("*")) 