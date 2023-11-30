import kbc_alt 
import kbc_toml
import kbc_sqlite
import kbc_llm

import datetime


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


class kbc_controller():
    def get_app_config(returnDict:bool=True):
        tomls = kbc_toml.MatchTomlTable("dev.toml", "app_config", "dict")
        global app_config
        app_config = tomls["app_config"]

        if returnDict == True:
            return app_config
        

    def get_help():
        pass
    
    def rewrite_config():
        pass


    # [todo 3]
    def inUTC(timeZone:int=0):
        dt_now_UTC0 = str(datetime.datetime.now(datetime.timezone.utc))
        return(dt_now_UTC0)
    

    # [todo 2]
    # 前端只检查输入数量正确, 内容正确统一代回后端检查
    def inputHandler():
        pass


    def transitCommand():
        # do while or for (1)
        while(1):
            app_commands = input(currentPath + "/: ", ).split(" ")
            # Input exception check
            
            # [todo 1]
            # Controller.InputCheck(app_commands)

    
    def makeLog():
        pass


    # [todo 4]
    def start():
        pass

        # 2. Valid DB
        # startState = Stateful.Translator(['/', app_config["dbPath"], app_config["dbType"]])
        # print(startState)
        # kbc_controller.TransitCommand()


if __name__ == "__main__":
    kbc_controller.start()   