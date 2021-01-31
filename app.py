from flask import Flask 
app = Flask(__name__) 
   
@app.route('/') 
def hello_world(): 
    return 'Hello World... '
  
@app.route('/morning') 
def wish_me_good_morning(): 
    return 'Good morning... '
  
# main driver function 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8080)
