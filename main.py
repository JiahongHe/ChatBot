from func_utils import *
import time



def __main__():
    print('hi, I am your new friend, please try to talk to me!')
    while True:
        msg = get_audio()
        give_response(msg)
        time.sleep(5)


__main__()