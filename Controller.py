import Alt, Stateful
import datetime


class kbc_controller():
    def get_config():
        tomls = Stateful.MatchTomlTable("dev.toml", "app_config", "dict")
        global app_config
        app_config = tomls["app_config"]


    def get_help():
        pass
    
    def rewrite_config():
        pass


    # [todo 3]
    def InUTC(timeZone=0):
        dt_now_UTC0 = str(datetime.datetime.now(datetime.timezone.utc))
        return(dt_now_UTC0)
    

    # [todo 2]
    # 前端只检查输入数量正确, 内容正确统一代回后端检查
    def InputCheck(inputs):
        pass


    def TransitCommand():
        # do while or for (1)
        while(1):
            app_commands = input(currentPath + "/: ", ).split(" ")
            # Input exception check
            
            # [todo 1]
            # Controller.InputCheck(app_commands)
            if len(app_commands) < 5:
                # Add CurrentPath && DBType && Path
                app_commands.append(currentPath)
                app_commands.append(app_config["dbPath"])
                app_commands.append(app_config["dbType"])

                Stateful.Handler(app_commands)

            elif len(app_commands) >= 5:
                print("app_commands >5 error")


    # [todo 4]
    def GenDB():# Stateful里面还有一个一样的方法
        pass
        # 1. 先检查是否已经存在DB? y/n?
        # 2. 连接性检查（是否要切换到新建的DB）y/n?


    # [todo 4]
    def start():
        # 0. init
        
        # 1. get config
        kbc_controller.get_config()

        # 2.
        startState = Stateful.Handler(['/', app_config["dbPath"], app_config["dbType"]])
        print(startState)
        kbc_controller.TransitCommand()


class View:
    def ToDisplayTime(utcTime, TimeZone):
        displayTime = "displayTime translation not finished"
        return displayTime
    
    def Refresh():
        pass


# For ChatGLM3-6B
class LLM():
    def call():
        pass

    def respond():
        pass


if __name__ == "__main__":
    # Controller.start()
    kbc_controller.get_config()
    