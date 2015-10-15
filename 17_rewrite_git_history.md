I always forget how to back date, so here we go ...

> This is dangerous and should be signed off by the omniscience, omnipotence Git him/herself. Rewriting history is evil, in other words.

```bash
$ git add <file_name>
$ export GIT_COMMITER_DATE="Sun Jun 15 14:00 2014 +0100"
$ export GIT_AUTHOR_DATE="Sun Jun 15 14:00 2014 +0100"
$ git commit -m "so bad"
$ git push
```

> `GIT_COMMITER_DATE` and `GIT_AUTHOR_DATE` are environment variables