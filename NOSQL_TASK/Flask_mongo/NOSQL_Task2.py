from flask import Flask , render_template_string, request
from pymongo import MongoClient
import os 
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()  # load .env
client = MongoClient(os.getenv("connection_string"))
db = client["SourabhDB"]
collection = db["Collection1"]

@app.route("/", methods=['GET', 'POST'])
def index():
    form_html = """
<!doctype html>
<html>
  <head><meta charset="utf-8"><title>User Form</title></head>
  <body>
    <h1>Add User</h1>
    <form method="post">
      <label>Name: <input type="text" name="name" required></label><br>
      <label>Email: <input type="email" name="email" required></label><br>
      <button type="submit">Submit</button>
    </form>
  </body>
</html>
"""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        user_data ={
            "name": name,
            "email": email
        }

        collection.insert_one(user_data)
        client.close()
        return render_template_string("<p>Data inserted successfully</p><p><a href='/'>Back</a></p>")
    
    return render_template_string(form_html)

if __name__ == "__main__":
    app.run(debug = True)