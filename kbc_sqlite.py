import sqlite3


# ----- Sqlite Methods -----
def exec_one(dbPath:str, commands:list, fetchall:bool=False):
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

    return 0


def isExist(dbPath:str, tableName:str, capitalize:bool=False, itemName:str="", returnBool:bool=True):
    # [todo 4] 这里面.capitalize()后面需要根据config.toml里面的内容判断
    # 可能也不用, 因为KBCLEV的表名和本身并无关系
    if capitalize == True:
        tableName = tableName.capitalize()

    sqls = "SELECT name FROM {table} WHERE name='{name}'".format(table=tableName, name=itemName)
    ie = Exec_one(dbPath, sqls)

    if ie != [] and returnBool == False:
        return ie
    
    elif ie != [] and returnBool == True:
        return True

    elif ie == []:
        return False
    
    else:
        # Alt.Err(errCode)
        print("err <Code>: unexpected error in existence check")


# ----- Record_main(DB record as a class) -----
class RM():
    def __init__(self, type:str="", name:str="", dscrp:str="", creator:str="", relatedBoard:str="", relatedClass:str="", state:int=-10) -> None:
        self.id = "null"
        self.type = type
        self.name = name
        self.dscrp = dscrp
        self.creator = creator
        self.createdTime = "datetime('now')"
        self.relatedBoard = relatedBoard
        self.relatedClass = relatedClass
        self.state = state

    
    def select(self, selectColumn:str="name"):
        sqls = "SELECT {sc} FROM compact_main WHERE type='{s.type}' AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}' AND state={s.state};".format(sc=selectColumn, s=self)                                              
        
        return sqls
    

    def add(self):
        sqls = "INSERT INTO compact_main VALUES({a.id}, '{a.type}', '{a.name}', '{a.dscrp}', '{a.creator}', '{a.createdTime}', '{a.relatedBoard}', '{a.relatedClass}', {a.state});".format(a=self)

        return sqls


    def delete(self): # 1. withstate:int=10? 2. withStatement >= or > or <?
        sqls = "UPDATE compact_main SET state=-10 WHERE type='{d.type}' AND name='{d.name}' AND relatedBoard='{d.relatedBoard}' AND relatedClass='{d.relatedClass}' AND state=10;".format(d=self)

        return sqls


    def edit(self, editColumn:str="", editValue:str=""):
        sqls = "UPDATE compact_main SET {ec}='{ev}' WHERE type='{e.type}' AND name='{e.name}' AND relatedBoard='{e.relatedBoard}' AND relatedClass='{e.relatedClass}' AND state={e.state};".format(ec=editColumn, ev=editValue, e=self)

        return sqls
    

    def edit_state(self, editColumn:str="", editValue:int=-10):
        sqls = "UPDATE compact_main SET {ec}='{ev}' WHERE type='{e.type}' AND name='{e.name}' AND relatedBoard='{e.relatedBoard}' AND relatedClass='{e.relatedClass}' AND state={e.state};".format(ec=editColumn, ev=editValue, e=self)

        return sqls


    def move(self, moveColumn:str="", moveValue:str=""):
        sqls = "UPDATE compact_main SET {mc}='{mv}' WHERE type='{m.type}' AND name='{m.name}' AND relatedBoard='{m.relatedBoard}' AND relatedClass='{m.relatedClass}' AND state=10;".format(mc=moveColumn, mv=moveValue, m=self)
        
        return sqls


    def back(self, selectColumn:str="name"):
        sqls = "SELECT {sc} FROM compact_main WHERE type='{s.type}' AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}' AND state={s.state};".format(sc=selectColumn, s=self)                                              
        
        return sqls


    def export(self, selectColumn:str="name"):
        sqls = "SELECT {sc} FROM compact_main WHERE type='{s.type}' AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}' AND state={s.state};".format(sc=selectColumn, s=self)                                              
        
        return sqls


# ----- Record_log_action(DB record as a class) -----
class RLA():
    pass


# ----- Auto generate DB from config.toml -----
def genDB():
    # model IE?
    # over write?
    # exec
    pass

