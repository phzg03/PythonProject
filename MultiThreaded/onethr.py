from time import sleep, ctime
import _thread
import threading


loops = [4, 2]
def loop0():
    print("start loop0 at " + ctime())
    sleep(4)
    print("end loop0 at " + ctime())


def loop1():
    print("start loop1 at " + ctime())
    sleep(2)
    print("end loop1 at " + ctime())


def loop(nloop, nesc, lock):
    print("start loop " + nloop + " at " + ctime())
    sleep(nesc)
    print("loop " + nloop + " done " + ctime())
    lock.release()

def main():
    # print("starting at " + ctime())
    # _thread.start_new_thread(loop0, ())
    # _thread.start_new_thread(loop1, ())
    # sleep(6)
    # print("all done at " + ctime())
    print("start at " + ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop,(str(i), loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass

    print("all done at " + ctime())


if __name__ == '__main__':
    main()