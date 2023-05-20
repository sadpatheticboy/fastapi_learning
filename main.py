from fastapi import FastAPI

app = FastAPI()
counter = 0


@app.get('/counter')
def counter_route():
    global counter
    counter += 1
    return {
        'message': counter
    }
