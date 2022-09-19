from tkinter import TRUE
from flask import Flask

#object of flask class
app=Flask(__name__)

#defining route for show
@app.route("/")
def show():
    return "riyansh"


#running the API
if __name__ == "__main__":
    app.run(debug=True)

    