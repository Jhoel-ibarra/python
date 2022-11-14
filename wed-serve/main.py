import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,4]

@app.get("/contact")
def get_list():
    return {
        "name" : "platzi"
    }

@app.get("/html", response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>hola soy jhoel</title>
        </head>
        <body>
            <h1>holanda</h1>
        </body>
    </html>
    """



def run():
    store.get_categories()

if __name__ == "__main__":
    run()
