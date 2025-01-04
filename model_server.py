# %%
import pickle
from enum import Enum

from fastapi import FastAPI

with open("model/trained_model.pkl", "rb") as file:
    model = pickle.load(file)


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Required query parameters, needy has no default value hence is required
# http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be 
# predefined, you can use a standard Python Enum.
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# Using an option directly from Starlette you can declare a path parameter containing a path using
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as 
# "query" parameters.

# The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.
# For example, in the URL:
# http://127.0.0.1:8000/items/?skip=0&limit=10
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
# As they are part of the URL, they are "naturally" strings.
# But when you declare them with Python types (in the example above, as int), they are converted to that type and validated 
# against it.

#You can also declare bool types, and they will be converted:
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
# http://127.0.0.1:8000/items/foo?short=1 or http://127.0.0.1:8000/items/foo?short=true or http://127.0.0.1:8000/items/foo?short=on
# many others included, check documentation

# You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item