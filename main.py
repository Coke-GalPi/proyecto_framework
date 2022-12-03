from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="./view")

@app.get("/")
def root(req: Request):
    return template.TemplateResponse("./index.html", {"Request":req})