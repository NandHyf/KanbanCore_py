# ----- Pre notes
# err 0: correct config not found
# err 1: correct DB not found
# -----


def pause():
    input("pausing, press any key to continue: ")
    # exit()


def Err(errCode, sec_respond:bool=False):
    if errCode == 0:
        print("err 0: syntax error")

    elif errCode == 1:
        print("err 1: ")

    elif errCode == 2:
        pass

    pause()
    # exit()



def Warn():
    pass


def sec_response():
    pass