import sqlite3
import kbc_alt


# ----- Record_main(DB record as a class) -----
class RM():
    def __init__(self, type:str="", name:str="", dscrp:str="", creator:str="", createdTime:str="datetime('now')", relatedBoard:str="", relatedClass:str="", statement:int=-10) -> None:
        self.id = "null"
        self.type = type
        self.name = name
        self.dscrp = dscrp
        self.creator = creator
        self.createdTime = createdTime
        self.relatedBoard = relatedBoard
        self.relatedClass = relatedClass
        self.statement = statement


    def select(self, selectColumn:str="name"):
        return "SELECT {sc} FROM compact_main WHERE type={s.type} AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}' AND state{s.statement};".format(sc=selectColumn, s=self)
    

    def add(self):
        return "INSERT INTO compact_main VALUES({a.id}, {a.type}, '{a.name}', '{a.dscrp}', '{a.creator}', '{a.createdTime}', '{a.relatedBoard}', '{a.relatedClass}', {a.statement});".format(a=self)


    def delete(self): 
        return "UPDATE compact_main SET state=-10 WHERE type={d.type} AND name='{d.name}' AND relatedBoard='{d.relatedBoard}' AND relatedClass='{d.relatedClass}' AND state{d.statement};".format(d=self)


    def edit(self, editColumn:str="", editValue:str=""):
        return "UPDATE compact_main SET {ec}='{ev}' WHERE type={e.type} AND name='{e.name}' AND relatedBoard='{e.relatedBoard}' AND relatedClass='{e.relatedClass}' AND state{e.statement};".format(ec=editColumn, ev=editValue, e=self)
    

    def move(self, moveColumn:str="", moveValue:str=""):
        return "UPDATE compact_main SET {mc}='{mv}' WHERE type={m.type} AND name='{m.name}' AND relatedBoard='{m.relatedBoard}' AND relatedClass='{m.relatedClass}' AND state{m.statement};".format(mc=moveColumn, mv=moveValue, m=self)


    def back(self, selectColumn:str="name"):
        return "SELECT {sc} FROM compact_main WHERE type={s.type} AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}' AND state{s.statement};".format(sc=selectColumn, s=self)


    def export(self, selectColumn:str="name"):
        return "SELECT {sc} FROM compact_main WHERE type={s.type} AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}' AND state{s.statement};".format(sc=selectColumn, s=self)
    

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


# ----- Operating Cursor -----
oc = {
    "dt":"", # DBType
    "dp":"", # DBPath

    "cp":[], # CurrentPath
    "pp":[], # PreviousPath

    "steps":[],

    "tp":[], # TargetPath
    "tp_in":[], # ~ after command parameter "in"(&& before command parameter "to")
    "tp_to":[], # ~ after command parameter "to"
    "tp_attr":[] # ~ like "-name" in "edit -name oldName to newName"
}
# some thoughts:
# class oc():
#   def read_oc(), def move_oc()


# ----- Execute Methods -----
def exec(dbPath:str="", sqls:str="", fetchAll:bool=False):
    if dbPath != "" and sqls != "":
        try:
            con = sqlite3.connect(dbPath)
            cur = con.cursor()

            cur.execute(sqls)
            con.commit()

            if fetchAll == True:
                return cur.fetchall()

            con.close()

        except sqlite3.OperationalError:
            print(sqlite3.OperationalError.__name__)


def recordExist(dbPath:str, tableName:str, capitalize:bool=False, itemName:str="", returnBool:bool=True):
    if capitalize == True:
        tableName = tableName.capitalize()

    sqls = "SELECT name FROM {table} WHERE name='{name}';".format(table=tableName, name=itemName)
    ie = exec(sqls)

    if ie != [] and returnBool == False:
        return ie
    
    elif ie != [] and returnBool == True:
        return True

    elif ie == []:
        return False
    
    else:
        # kbc_alt.Err(errCode)
        print("err <Code>: unexpected error in existence check")


if __name__ == "__main__":
    pass