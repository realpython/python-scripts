from subprocess import check_output, call


file_name = str(input('Enter the file name: '))
commit = check_output(["git", "rev-list", "-n", "1", "HEAD", "--", file_name])
print(str(commit).rstrip())
call(["git", "checkout", str(commit).rstrip()+"~1", file_name])


"""
After entering a filename, this script searches your Git history for that file.
If the file exists, then it will restore it.
"""
