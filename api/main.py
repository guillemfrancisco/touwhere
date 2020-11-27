#!/usr/bin/env python
'''
Uber H3 RESTApi
'''

from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from api.endpoints.router import api_router


__author__ = 'Guillem Francisco'
__license__ = 'GNU GPL v3'
__version__ = '0.1'
__maintainer__ = 'Guillem Francisco'
__email__ = 'guillem.francisco@actuatech.ad'
__status__ = 'Development'


app = FastAPI(title="H3", openapi_url="/api/v0.1/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v0.1")


@app.get("/api/v0.1/")
async def redirection():
    return RedirectResponse(url="/docs")
