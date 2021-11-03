# Entry point for the application.
#from . import app    # For application discovery by the 'flask' command.
#from . import views  # For import side-effects of setting up routes.
import flask
app = flask.Flask(__name__)

if __name__ == "__main__":
    app.run(port=8080)