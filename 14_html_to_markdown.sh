# Convert all html files in a single directory to markdown
#
# 1. Install pandoc
# 2. Run the script
 
 
 
FILES=*.html
for f in $FILES
do
  # extension="${f##*.}"
  filename="${f%.*}"
  echo "Converting $f to $filename.md"
  `pandoc $f -t markdown -o ../mds/$filename.md`
  # uncomment this line to delete the source file.
  # rm $f
done