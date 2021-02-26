from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello People</h1>"

@app.route("/login")
def login():
    return "<input type='text' placeholder='enter name'>"

if __name__=='__main__':
    app.run(host='0.0.0.0')

