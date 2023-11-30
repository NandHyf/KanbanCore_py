# ----- Pre notes
# err 0: correct config not found
# err 1: correct DB not found
# -----


def pause():
    input("pausing, press any key to continue: ")


def Err(errCode, lang='en'):
    errText = ""
    input("err ", errCode, ": ",  errText)
    exit()


def Warn():
    pass


def sec_response():
    pass