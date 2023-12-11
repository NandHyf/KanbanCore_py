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
        #             "/": 0, "..": 1,
        commandType = {"select": 2, "add": 3, "delete": 4, "edit":5, "move": 6}
        objType = {"board": 3, "class": 2, "event": 1}

        try:
            if ".." in c_list and "/" in c_list:
                kbc_alt.Err(0)
                return 0 

            elif c_list[0] == "/":
                print("command is 'back_home' ")
                c_list = [0]
                print(c_list)
                return 0
            
            elif c_list[0] == "..":
                print("command is 'back_previous' ")
                c_list[0] = 1
                print(c_list)
                return 0
            
            elif c_list[0] in commandType and c_list[1] in objType:
                print("Valid true")
                
                if c_list[1] == "board":

                    if "in" in c_list:
                        kbc_alt.Err(0)

                    elif "move" in c_list:
                        kbc_alt.Err(0)

                    c_list[0] = commandType[c_list[0]]
                    c_list[1] = 3


                elif c_list[1] == "class":
                    
                    if "move" in c_list:
                        kbc_alt.Err(0)

                    c_list[0] = commandType[c_list[0]]
                    c_list[1] = 2             


                elif c_list[1] == "event":
                    c_list[0] = commandType[c_list[0]]
                    c_list[1] = 1

                else:
                    kbc_alt.Err(0)
                
                print("command list: ", c_list)

            else:
                kbc_alt.Err(0)
            

        except IndexError:
            kbc_alt.Err(0)


        # 3. Executable check


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