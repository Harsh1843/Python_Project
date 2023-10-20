from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
  #This function is the handler for the root URL("/")
  return "Hello World"
if __name__=="__main__":
  #Run the Flask application if the script is executed directly
  app.run()
