import kbc_alt 
import kbc_toml
import kbc_sqlite
import kbc_llm

import datetime

# class config def read(), reload()
class kbc_controller():
    def get_app_config(returnDict:bool=True):
        tomls = kbc_toml.MatchTomlTable("dev.toml", "app_config", "dict")

        if returnDict == True:
            return tomls
        

    def get_help():
        pass
    
    def rewrite_config():
        pass


    # [todo 4]
    def display_in_timezone(timezone:int=0):
        pass
    

    # [todo 2]
    def validCheck():
        pass


    def makeLog():
        pass


    def transitCommand():
        while(True):
            pass
            # Input exception check
            
            # [todo 1]
            # Controller.InputCheck(app_commands)


    def direct():
        sqls = input("direct sqls(ONE SQL STATEMENT ONLY): ")
        res = kbc_sqlite.exec_fetchall(kbc_sqlite.oc['dp'], sqls)
        print("res: ", res)


    # [todo 4]
    def start():
        app_config = kbc_controller.get_app_config()["app_config"]

        kbc_sqlite.oc['dt'] = app_config['DBType']
        kbc_sqlite.oc['dp'] = app_config['DBPath']

        # if start_as_llmserver == True:
        
        kbc_sqlite.oc['cp'] = ['home']


if __name__ == "__main__":
    kbc_controller.start()
    kbc_controller.direct()
    kbc_alt.pause()