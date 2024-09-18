from fastapi import Depends, FastAPI



"""
Enroll Middlewares
--- 

Enroll Middleware to Root applicaiton

"""
def enroll_middlewares(app:FastAPI):
    middleware_attacher = app.middleware("http")
