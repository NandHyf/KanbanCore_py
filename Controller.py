import kbc_alt 
import Stateful
import datetime


class kbc_controller():
    def get_help():
        pass
    
    def rewrite_config():
        pass


    # [todo 3]
    def InUTC(timeZone:int=0):
        dt_now_UTC0 = str(datetime.datetime.now(datetime.timezone.utc))
        return(dt_now_UTC0)
    

    # [todo 2]
    # 前端只检查输入数量正确, 内容正确统一代回后端检查
    def InputHandler():
        pass


    def TransitCommand():
        # do while or for (1)
        while(1):
            app_commands = input(currentPath + "/: ", ).split(" ")
            # Input exception check
            
            # [todo 1]
            # Controller.InputCheck(app_commands)


    # [todo 4]
    def GenDB():# Stateful里面还有一个一样的方法
        pass
        # 1. 先检查是否已经存在DB? y/n?
        # 2. 连接性检查（是否要切换到新建的DB）y/n?


    # [todo 4]
    def start():
        pass

        # 2. Valid DB
        # startState = Stateful.Translator(['/', app_config["dbPath"], app_config["dbType"]])
        # print(startState)
        # kbc_controller.TransitCommand()


# For ChatGLM3-6B
class LLM():
    def call():
        pass

    def respond():
        pass


if __name__ == "__main__":
    kbc_controller.start()   