# from Controller import kbc_config
import kbc_alt
import kbc_toml
import kbc_sqlite


# ------ Basics ------
def get_app_config(returnDict:bool=True):
        tomls = kbc_toml.MatchTomlTable("dev.toml", "app_config", "dict")
        global app_config
        app_config = tomls["app_config"]

        if returnDict == True:
            return app_config


# ----- Core Function -----
def Translator():
    global oc
    oc = {
    "dt":str, # DBType
    "dp":str, # DBPath

    "cp":list, # CurrentPath
    "pp":list, # PreviousPath

    "next_move":str,

    "tp":list, # TargetPath
    "tp_in":list, # ~ after command parameter "in"(&& before command parameter "to")
    "tp_to":list, # ~ after command parameter "to"
    "tp_attr":str # ~ like "-name" in "edit -name oldName to newName"
    }
    # some thoughts:
    # class oc():
    #   def get_oc(), def move_oc()


if __name__ == "__main__":
    pass