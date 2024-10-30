from fastapi import FastAPI, Body
app = FastAPI()

class Wepons:
    def __init__(self, id: int, name: str, damage: float, durability: int) -> None:
        self.id: int = id
        self.name: str = name
        self.damage: int = damage
        self.durability: int = durability
repo = [
    Wepons(0,"Алмазный меч",12.0,1200),
    Wepons(1,"Алмазный топор",15.0,1200),
    Wepons(2,"Железный меч",10.0,1000),
    Wepons(3,"Железный топор",12.0,1000),
]

@app.get("/")
def get_orders():
    return repo

@app.post("/")
def editor(data=Body()):
    id = data.get("id")
    for o in repo:
        if o.id == id:
            id = data.get("id")
            name = data.get("name")
            damage = data.get("damage")
            durability = data.get("durability")

            bufer = Wepons(id,name,damage,durability)
            repo[id] = bufer
            

            return {"message": "Оружие обновлена"}, 201
        
    id = data.get("id")
    name = data.get("name")
    damage = data.get("damage")
    durability = data.get("durability")

    bufer = Wepons(id,name,damage,durability)
    repo.append(bufer)

    return {"message": "Оружие добавлено"}, 201

@app.post("/del")
def editor(data=Body()):
    id = data.get("id")
    for o in repo:
        if o.id == id:
            id = data.get("id")
            name = data.get("name")
            damage = data.get("damage")
            durability = data.get("durability")

            bufer = Wepons(id,name,damage,durability)
            repo[id] = bufer
            

            return {"message": "Оружие обновлена"}, 201
    return {"message": "Не верный id"}, 201
