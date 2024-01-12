import argparse
from pathlib import Path
import shutil

def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    parser.add_argument("-s", "--source", type = Path,required= True, help = "Папка з файлами")
    parser.add_argument("-o", "--source", type = Path, default = Path('output'), help = "Папка для копіювання")
    
    return parser.nparse_args()

def recursive_copy(source: Path, output: Path):
    for el in source.iterdir():
        if el.is_dir():
            recursive_copy(el, output)
        else:
            folder = el.name[:1]
            output = output / folder
            output.mkdir(exist_ok=True, parents = True)
            shutil.copy(el, output)



def main():
    args = parse_argv()
    print(args)
    
if __name__ == "__main__":
    main()