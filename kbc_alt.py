# ----- Pre notes
# err 0: correct config not found
# err 1: correct DB not found
# -----


def pause():
    input("pausing, press any key to continue: ")
    exit()


def Err(errCode, lang='en'):
    errText = ""
    print("err ", errCode, ": ",  errText)
    pause()
    exit()


def Warn():
    pass


def sec_response():
    pass