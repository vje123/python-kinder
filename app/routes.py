from flask import Blueprint, render_template, jsonify, request

bp = Blueprint('main', __name__)

shapes = ["Circle", "Square", "Triangle", "Rectangle", "Star"]
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/api/shapes')
def get_shapes():
    return jsonify(shapes)

@bp.route('/api/colors')
def get_colors():
    return jsonify(colors)

@bp.route('/api/select', methods=['POST'])
def select_shape_color():
    shape = request.args.get('shape')
    color = request.args.get('color')
    return jsonify({"selectedShape": shape, "selectedColor": color})