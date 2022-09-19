from distutils.log import error
from flask import Flask,jsonify,request

#object of flask class
app=Flask(__name__)

#creating a dummy task using array of task 
tasks=[
    {
        'id':1,
        'title':u'buygrocery',
        'description':u'milk,cheese,pizza,fruit,bun',
        'done':False
    },
    {
         'id':2,
        'title':u'learnpython',
        'description':u'need to find a good python tutorial',
        'done':False
    }
]

#defining route for show
@app.route("/getdata")
def show():
    return jsonify({
        "data":tasks
    })


#defining route for add data
@app.route("//add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task = { 
        'id': tasks[-1]['id'] + 1, 
        'title': request.json['title'], 
        'description': request.json.get('description', ""), 
        'done': False 
        }    
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"taskaddedsuccessfully"
    })    
        
#running the API
if __name__ == "__main__":
    app.run(debug=True)

    