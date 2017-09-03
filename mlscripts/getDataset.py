import sys
from pathlib import Path

inputs = sys.argv

if not inputs[-1]=='nofile':
	fname = inputs[-1]

	dfile = Path("../datasets/"+fname)
	if my_file.is_file():
		print(fname)
	else:
		print("error")