from flask import Flask, request, jsonify, send_from_directory
from flasgger import Swagger
import os
import xml.etree.ElementTree as ET

app = Flask(__name__)
swagger = Swagger(app)

UPLOAD_FOLDER = 'uploads'
XML_FILE = 'images.xml'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(XML_FILE):
    root = ET.Element("gallery")
    tree = ET.ElementTree(root)
    tree.write(XML_FILE)


# Читаем XML
def read_xml():
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    return root


# Добавление изображения в XML
def add_image_to_xml(category, filename):
    root = read_xml()
    category_element = None
    for cat in root.findall("category"):
        if cat.get("name") == category:
            category_element = cat
            break
    if not category_element:
        category_element = ET.SubElement(root, "category", name=category)

    ET.SubElement(category_element, "image", name=filename)
    tree = ET.ElementTree(root)
    tree.write(XML_FILE)


# Получить список изображений
@app.route('/images', methods=['GET'])
def get_images():
    root = read_xml()
    images_data = {}
    for category in root.findall("category"):
        name = category.get("name")
        images_data[name] = [img.get("name") for img in category.findall("image")]
    return jsonify(images_data)


# Загрузка изображения
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    category = request.form.get('category', 'default')

    filename = file.filename
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    add_image_to_xml(category, filename)
    return jsonify({"success": True, "filename": filename})


# Отдача изображения
@app.route('/uploads/<filename>')
def get_uploaded_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# Сохранение выбранного изображения
selected_image = {"filename": None}


@app.route('/select', methods=['POST'])
def select_image():
    global selected_image
    data = request.json
    selected_image["filename"] = data.get("filename")
    return jsonify({"success": True, "selected": selected_image["filename"]})


@app.route('/selected', methods=['GET'])
def get_selected_image():
    return jsonify(selected_image)


if __name__ == '__main__':
    app.run(debug=True)
