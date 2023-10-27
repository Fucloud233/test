import sys

# sys.path.append(".")
# from utils.reader import Reader

sys.path.append("./utils")
from reader import Reader

Reader.load_line("text.txt")