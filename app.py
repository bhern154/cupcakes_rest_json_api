"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# ----------- FRONTEND WEBPAGE -----------

@app.route("/")
def home():
    """Render HMTL home page."""
    return render_template("index.html")

# ----------- BACKEND API -----------

def serialize_cupcake(cupcake):
    """Serialize a cupcake SQLAlchemy obj to a dictionary."""

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }

@app.route("/api/cupcakes")
def get_all_cupcakes():
    """Get data about all cupcakes. Respond with JSON from each cupcake instance.
    Example -> {cupcakes: [{id, flavor, size, rating, image}, ...]}"""

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(item) for item in cupcakes]

    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes/<cupcake_id>")
def get_cupcake(cupcake_id):
    """Get data about one cupcake. Respond with a JSON of the cupcake instance
    Example -> {cupcake: {id, flavor, size, rating, image}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = serialize_cupcake(cupcake)

    return jsonify(cupcake = serialized)

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create a cupcake from form data & return it
    Example -> {cupcake: {id, flavor, size, rating, image}}"""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    if image == "":
        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating)
    else:
        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    # new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcake(new_cupcake)

    return (jsonify(cupcake = serialized), 201)

@app.route("/api/cupcakes/<cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Partially update a cupcake from form data & return it
    Example -> {cupcake: {id, flavor, size, rating,image}}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    serialized = serialize_cupcake(cupcake)

    return jsonify(cupcake = serialized)

@app.route("/api/cupcakes/<cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Partially update a cupcake from form data & return it
    Returns -> {message: "Deleted"}"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message = "Deleted")
