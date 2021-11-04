from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    abort,
    current_app,
    jsonify
)
from app import create_app,db
from models import Articles,articles_schema

# Create an application instance
app = create_app()

@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("main/index.html")
    
if __name__ == "__main__":
	app.run(debug=True)