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
    def validCheck(c_list:list=[]):
        # c_list == 'c'ommand 'list'
        commandType = {"/": 0, "..": 1, "select": 1, "add": 1, "delete": 1, "edit": 1, "move": 1, "to": 1, "in": 1}
        objType = {"board": 3, "class": 2, "event": 1}

        # split multi commands


        # valid each
        try:

            counter = 0

            if counter > 5:
                kbc_alt.Err(0)
            

            # 指令总和大于或者小于某个数就说明后面还有不合规的语法

        except IndexError:
            kbc_alt.Err(0)


    def makeLog():
        pass


    def direct():
        sqls = input("direct sqls(ONE SQL STATEMENT ONLY): ")
        res = kbc_sqlite.exec(kbc_sqlite.oc['dp'], sqls, True)
        print("res: ", res)


    # [todo 4]
    def start():
        app_config = kbc_controller.get_app_config()["app_config"]

        kbc_sqlite.oc['dt'] = app_config['DBType']
        kbc_sqlite.oc['dp'] = app_config['DBPath']

        # if start_as_llmserver == True:
        
        kbc_sqlite.oc['cp'] = ['home']


        while(True):
            c_list = input("input command: ").split()
            kbc_controller.validCheck(c_list)



if __name__ == "__main__":
    kbc_controller.start()
    # kbc_alt.pause()