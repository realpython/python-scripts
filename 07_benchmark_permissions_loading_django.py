import os
import time
import numpy

# temp file for benchmarking


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()

        result = method(*args, **kw)
        te = time.time()
        all_times.append(te - ts)

        print(all_times)
        print(numpy.mean(all_times))
        return result

    return timed


def create_new_db():
    os.system("mysqladmin -u root drop DATABASE_NAME -f")
    os.system("mysqladmin -u root create DATABASE_NAME -f")
    os.system("./manage.py syncdb")
    os.system("./manage.py migrate")


@timeit
def load_new_perms():
    os.system("./manage.py LOAD_PERMS_COMMAND")


if __name__ == "__main__":
    n = 0
    all_times = list()
    while n < 10:
        create_new_db()
        load_new_perms()
        n += 1
