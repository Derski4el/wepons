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
next_id = 4

@app.get("/")
def get_orders():
    return repo


@app.post("/")
def editor(data=Body()):
    global next_id
    id = data.get("id")
    if id is not None:
        for i,o in enumerate(repo):
            if o.id == id:
                name = data.get("name")
                damage = data.get("damage")
                durability = data.get("durability")

                bufer = Wepons(id,name,damage,durability)
                repo[id] = bufer
                return {"message": "Оружие обновлена"}, 201
                 
    name = data.get("name")
    damage = data.get("damage")
    durability = data.get("durability")
    bufer = Wepons(next_id,name,damage,durability)
    next_id += 1
    repo.append(bufer)

    return {"message": "Оружие добавлено"}, 201

@app.post("/")
def delete(data=Body()):
    id = data.get("id")
    if id is not None:
            for i,o in enumerate(repo):
                 if o.id == id:
                    del repo[id]
                    return {"message": "Оружие удалено"}, 201
    return {"message": "Ошибка, не верный id"}, 201