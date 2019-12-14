#!/usr/bin/python3
# Time: 2019/07/09 5:45 PM
# About: high performance asyncio services


from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn

app = Starlette(debug=True)


@app.route('/')
async def homepage(request):
    return JSONResponse({"hello": "world"})

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)


# for better performance
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker --log-level warning example:app





























