"""Testing."""
import threading


def do_this():
    """Testing."""
    global x, lock
    while (x < 300):
        x += 1
        print('the thread 1 value of x -{}'.format(x))


def do_this_next():
    """Testing."""
    global x
    while (x < 600):
        x += 1
        print('the thraed 2 value of x -{}'.format(x))


def main():
    """Testing."""
    global x, lock
    x = 0
    lock = threading.Lock()
    our_thread = threading.Thread(name='our thread', target=do_this)
    our_thread.start()
    # our_thread.join()
    our_next_thread = threading.Thread(
        name='our_next_thread', target=do_this_next)
    our_next_thread.start()

if __name__ == '__main__':
    main()
