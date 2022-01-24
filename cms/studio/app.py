from flask import (
    Flask,
    render_template,
)
from .main import create_app

# Create an application instance
app = create_app()

@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("main/index.html")
    

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')