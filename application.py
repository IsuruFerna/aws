from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
  return 'hello world'

if __name__ == '__main__':
  application.run(debug=False)