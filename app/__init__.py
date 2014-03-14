from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
app.config["MONGODB_SETTINGS"] = {"DB": "sungapp_log"}
app.config["SECRET_KEY"] = "dmafksakrnl"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()

from app import views