from flask import Flask, render_template
from controllers.leagues_controller import leagues_blueprint
from controllers.admin_controller import admin_blueprint
from controllers.matches_controller import matches_blueprint
from controllers.teams_controller import teams_blueprint

app = Flask(__name__)

app.register_blueprint(leagues_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(matches_blueprint)
app.register_blueprint(teams_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)