from fastapi import FastAPI
import requests
app = FastAPI()


app.get("/server-list")
def serverlist():
    return {
        "code": 200,
        "data": {
            "official": [{"name": "test official server","online": 0}],
            "unofficial": [{"name": "test unofficial server","online": 0}]

        }
        
    }



