"""
FastAPI application exposing calculator functions as API endpoints.
"""
from fastapi import FastAPI, HTTPException

import calculator

app = FastAPI(title="Calculator API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/add")
def add(a: float, b: float):
    return {"result": calculator.add(a, b)}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": calculator.subtract(a, b)}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": calculator.multiply(a, b)}


@app.get("/divide")
def divide(a: float, b: float):
    try:
        return {"result": calculator.divide(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/divide_fl")
def divide_fl(a: float, b: float):
    try:
        return {"result": calculator.divide_fl(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/square")
def square(a: float):
    return {"result": calculator.square(a)}


@app.get("/cube")
def cube(a: float):
    return {"result": calculator.cube(a)}


@app.get("/power")
def power(a: float, b: float):
    return {"result": calculator.power(a, b)}


@app.get("/mod")
def mod(a: float, b: float):
    try:
        return {"result": calculator.mod(a, b)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/square_root")
def square_root(a: float):
    return {"result": calculator.square_root(a)}


@app.get("/itob")
def itob(a: int):
    try:
        return {"result": calculator.itob(a)}
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
