I always forget this ...

To recursively remove all those pesky *.pyc* files from a git repo, run this command:

```bash
$ find . -name "*.pyc" -exec git rm -f {} \;
```

Then make sure to add a *.gitignore* in the root of the repo and add the line: `*.pyc`