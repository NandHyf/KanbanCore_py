import sqlite3
import kbc_alt

# ----- Record_main(DB record as a class) -----
class RM():
    def __init__(self, type:str="", name:str="", dscrp:str="", creator:str="", createdTime:str="datetime('now')", relatedBoard:str="", relatedClass:str="", state:int=-10) -> None:
        self.id = "null"
        self.type = type
        self.name = name
        self.dscrp = dscrp
        self.creator = creator
        self.createdTime = createdTime
        self.relatedBoard = relatedBoard
        self.relatedClass = relatedClass
        self.state = state


    def select(self, selectColumn:str="name"):
        return "SELECT {sc} FROM compact_main WHERE type='{s.type}' AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}' AND state={s.state};".format(sc=selectColumn, s=self)
    

    def add(self):
        return "INSERT INTO compact_main VALUES({a.id}, '{a.type}', '{a.name}', '{a.dscrp}', '{a.creator}', '{a.createdTime}', '{a.relatedBoard}', '{a.relatedClass}', {a.state});".format(a=self)


    def delete(self): # 1. withstate:int=10? 2. withStatement >= or > or <?
        return "UPDATE compact_main SET state=-10 WHERE type='{d.type}' AND name='{d.name}' AND relatedBoard='{d.relatedBoard}' AND relatedClass='{d.relatedClass}' AND state={d.state};".format(d=self)


    def edit(self, editColumn:str="", editValue:str=""):
        return "UPDATE compact_main SET {ec}='{ev}' WHERE type='{e.type}' AND name='{e.name}' AND relatedBoard='{e.relatedBoard}' AND relatedClass='{e.relatedClass}' AND state={e.state};".format(ec=editColumn, ev=editValue, e=self)
    

    def edit_state(self, editValue:int=-10):
        return "UPDATE compact_main SET state={ev} WHERE type='{e.type}' AND name='{e.name}' AND relatedBoard='{e.relatedBoard}' AND relatedClass='{e.relatedClass}' AND state={e.state};".format(ev=editValue, e=self)


    def move(self, moveColumn:str="", moveValue:str=""):
        return "UPDATE compact_main SET {mc}='{mv}' WHERE type='{m.type}' AND name='{m.name}' AND relatedBoard='{m.relatedBoard}' AND relatedClass='{m.relatedClass}' AND state={m.state};".format(mc=moveColumn, mv=moveValue, m=self)


    def back(self, selectColumn:str="name"):
        return "SELECT {sc} FROM compact_main WHERE type='{s.type}' AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}' AND state={s.state};".format(sc=selectColumn, s=self)


    def export(self, selectColumn:str="name"):
        return "SELECT {sc} FROM compact_main WHERE type='{s.type}' AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}' AND state={s.state};".format(sc=selectColumn, s=self)
    

    def get_style():
        pass


# ----- Record_log_action(DB record as a class) -----
class RLA():
    pass


# ----- DB as a class -----
class DB():
    def __init__(self) -> None:
        pass


    def dbExist():
        pass


    def reGenerate():
        pass


def direct():
    pass


# ----- Operating Cursor -----
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


# ----- Execute Methods -----
def execute(dbPath):
    def dec(origin_func):
        pass

    con = sqlite3.connect(dbPath)
    cur = con.cursor()

    cur.execute(commands)
    con.commit()

    # if fetchall == input, return 0?
    if fetchall == True:
        re = cur.fetchall()
        return re
    
    cur.close()
    con.close()
    def dec():
        pass


@execute(oc["dp"])
def exec_one(dbPath:str, commands:list, fetchall:bool=False):
    pass


@execute(oc["dp"])
def exec_many():
    pass


def recordExist(dbPath:str, tableName:str, capitalize:bool=False, itemName:str="", returnBool:bool=True):
    # [todo 4] 这里面.capitalize()后面需要根据config.toml里面的内容判断
    # 可能也不用, 因为KBCLEV的表名和本身并无关系
    if capitalize == True:
        tableName = tableName.capitalize()

    sqls = "SELECT name FROM {table} WHERE name='{name}';".format(table=tableName, name=itemName)
    ie = exec_one(dbPath, sqls)

    if ie != [] and returnBool == False:
        return ie
    
    elif ie != [] and returnBool == True:
        return True

    elif ie == []:
        return False
    
    else:
        # kbc_alt.Err(errCode)
        print("err <Code>: unexpected error in existence check")


# ----- Master process -----
def master():
    pass