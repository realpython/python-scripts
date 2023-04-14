import os
import glob
import sys

if len(sys.argv) != 4:
    print("Incorrect usage, plz provide arguments like in an example: python script_name.py <folder_path> <file_type> <slicing>")
    sys.exit(1)

folder_path = sys.argv[1]
file_type = sys.argv[2]
slicing = int(sys.argv[3])

os.chdir(folder_path)
for file in glob.glob(f"*.{file_type}"):
    file_name = os.path.splitext(file)[0]
    extension = os.path.split(file)[1]
    new_file_name = f"{file_name[:-slicing]}{extension}"
    try:
      os.rename(file, new_file_name)
    except OSError as err:
      print(err)
    else:
      print(f"Renamed{file}to}{new_file_name}")
