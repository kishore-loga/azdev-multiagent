from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

@app.get("/api/greet")
async def greet(name: Optional[str] = Query(default="World")):
    try:
        return {"message": f"Hello, {name}!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class Numbers(BaseModel):
    numbers: List[float]

@app.post("/api/sum")
async def sum_numbers(data: Numbers):
    try:
        total = sum(data.numbers)
        return {"sum": total}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)