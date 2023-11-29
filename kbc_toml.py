import tomlkit


# ----- Toml Methods -----
def GetTomlDoc(tomlName:str):
    try:
        with open(tomlName, "rb") as t:
            doc = tomlkit.load(t)

            if doc == {}:
                input("error 0: could not found correct config file") 
                exit()

            return doc
        
    except FileNotFoundError:
        input("error 0: could not found correct config file") 
        # sec_respond?
        exit()
    

def MatchTomlKey(tomlName:str, key:str, table:str="none") -> str:
    doc = GetTomlDoc(tomlName)

    if table == "none":
        return str(doc.item(key))
    
    elif table != "none":
        d = doc.unwrap()
        return str(d[table][key])


# no differernt between ↑ MatchTomlKey() ↑ except receives and returns in list
def MatchTomlKeys(tomlName:str, keys:list, table:str="none") -> list:
    doc = GetTomlDoc(tomlName)

    if table == "none":
        # rl == 'r'eturn 'l'ist
        rl = []

        for key in keys:
            try:
                rl.append(doc.item(key))
            except:
                pass

        return rl
    

    elif table != "none":
        rl = []
        d = doc.unwrap()

        for key in keys:
            try:
                rl.append(d[table][key])
            except:
                pass

        return rl
    

def MatchTomlTable(tomlName:str, tableName:str, returnType:str="list"):
    d = GetTomlDoc(tomlName).unwrap()

    if returnType == "list":
        return list(d.get(tableName).values())
    
    elif returnType == "dict":
        return d