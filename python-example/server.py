from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import json

app = Flask(__name__)
CORS(app)
posts = [
    {
      "message": "Hello world",
      "user": "David"
    },
    {
      "message": "Hello world2",
      "user": "Daniel"
    }
    ];

@app.route("/posts", methods = ['GET', 'POST'])
def handlePosts():
  mydb = mysql.connector.connect(
  host="0.0.0.0",
  user="ubuntu",
  password="",
  database="website"
  )


  if request.method == 'GET':
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM web")
    myresult = mycursor.fetchall()
    payload = []
    content = {}
    for result in myresult:
      content = {'message': result[1], 'user': result[0]}
      payload.append(content)
      content = {}
    print(jsonify(payload))
    return jsonify(payload)
  else:

    mycursor = mydb.cursor()
    sql = ("INSERT INTO web(name, message) VALUES (%s, %s)")
    data = request.get_json(force=True)
    val = (data["name"],data["message"])
    mycursor.execute(sql, val)

    mydb.commit()
    return "{\"status\": true}"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
