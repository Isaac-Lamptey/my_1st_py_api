from fastapi import FastAPI
from fastapi.params import Body

#get request to the root endpoint
app = FastAPI()
@app.get("/") # @ is a decorator, it defines the route for the GET request
async def read_root():
    return {"Hello": "World"}

#post request path operation to the root endpoint

@app.post('/createpost')
def createpost(payload: dict = Body(...)): # extracts the request body and assigns it to the payload variable
    print(payload)
    return {"message": "Post created successfully"}