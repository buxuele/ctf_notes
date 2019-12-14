#!/usr/bin/python3
# Time: 2019/07/09 5:55 PM
# About: 

from starlette.applications import Starlette
from starlette.responses import PlainTextResponse, Response
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
import uvicorn

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory="static"))


@app.route('/')
async def homepage(request):
    return PlainTextResponse("hello, world")


@app.route('/user/me')
async def user_me(request):
    username = "buxuele"
    return PlainTextResponse("hello, %s!" % username)


@app.route('/user/{username}')
async def user(request):
    username = request.path_params['username']
    return PlainTextResponse("hello, %s!" % username)


@app.websocket_route('/ws')
async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text("hello, websocket")
    await websocket.close()


@app.on_event("startup")
def startup():
    print("ready to go")


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)






