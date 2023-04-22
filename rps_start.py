from fastapi import FastAPI
import inventory as i
import service as s

app = FastAPI()


@app.get("/{count_win}")
def startgame(count_win:int):
    return s.startgame(count_win)
    
@app.get("/rps/{rps}")
def compet(rps):
    return s.compet(rps)