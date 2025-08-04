import json
import os
from typing import Dict, List, Optional
from app.config import DB_FILE

def leer_json()->Dict:
    try:
        with open(DB_FILE, "r", encoding="utf-8") as cf:
            return json.load(cf)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def escribir_json(data : Dict)->Dict:
    with open(DB_FILE, "w", encoding="utf-8") as cf:
        json.dump(data, cf, indent=4)

def actualizar_json(data : Dict, path: Optional[List[str]] = None) -> None:
    currentData = leer_json()

    if not path:
        currentData.update(data)
    else:
        current = currentData
        for key in path[:-1]:
            current = current.setdefault(key, {})
        if path:
            current.setdefault(path[-1], {}).update(data)
    
    escribir_json(currentData)

def deleteJson(path: List[str])->bool:
    data = leer_json()
    if not data:
        return False
    
    current = data
    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]
    
    if path and path[-1] in current:
        del current[path[-1]]
        escribir_json(data)
        return True
    return False

def initializeJson(initialStructure:Dict)->None:
    if not os.path.isfile(DB_FILE):
        escribir_json(initialStructure)
    else:
        currentData = leer_json()
        for key, value in initialStructure.items():
            if key not in currentData:
                currentData[key] = value
        escribir_json(currentData)