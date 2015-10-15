import subprocess
import sys


if len(sys.argv) == 3:
    tag = sys.argv[1]
    commit = sys.argv[2]
    command = 'git tag -a {0} {1} -m "{2}"'.format(tag, commit, tag)
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    subprocess.call(command, shell=True)
    subprocess.call('git push --tags', shell=True)
else:
    print('usage: tag.py TAG_NAME COMMIT')
    sys.exit(1)
