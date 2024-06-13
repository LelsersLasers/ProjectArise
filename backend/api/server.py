import flask
# import flask_cors

import json

import keras
import keras.models

import base64
import numpy as np
import cv2


MODEL_LOAD_PATH = "arise_fullsave"
REMOVE_JSON_PATH = "remove.json"
INPUT_SIZE = 256
LABELS = [
    "aegilops_triuncialis",
    "arundo_donax",
    "centaurea_calcitrapa",
    "centaurea_stoebe",
    "cortaderia_selloana",
    "cynara_cardunculus",
    "euphorbia_terracina",
    "hypericum_canariense",
    "lepidium_latifolium",
    "lythrum_salicaria",
    "volutaria_tubuliflora"
]


app = flask.Flask(__name__)

model = keras.models.load_model(MODEL_LOAD_PATH)

def create_response(value):
    response = flask.jsonify(value)
    return response

@app.route("/classify", methods=["POST"])
# @flask_cors.cross_origin()
def classify():
    image_bs64 = flask.request.json.get("image_b64", None)
    if image_bs64 is None:
        return create_response({"error": "No image_b64 provided"})

    np_arr = np.frombuffer(base64.b64decode(image_bs64), np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (INPUT_SIZE, INPUT_SIZE))
    image = image.astype(np.float32) / 255.0

    cnn_input = np.expand_dims(image, axis=0)

    np_prediction = model.predict(cnn_input)[0]
    prediction = map(lambda x: float(x), list(np_prediction))
    predictions_with_labels = list(map(
        lambda prediction_and_label: {
            "confidence": prediction_and_label[0],
            "label": prediction_and_label[1]
        },
        zip(prediction, LABELS))
    )
    predictions_with_labels.sort(reverse=True, key=lambda x: x["confidence"])
    best_predictions = predictions_with_labels[:5]

    return create_response(best_predictions)

@app.route("/remove/<label>", methods=["GET"])
# @flask_cors.cross_origin()
def remove(label):
    with open(REMOVE_JSON_PATH, "r") as f:
        remove_json = json.load(f)
    
    remove_instructions = remove_json.get(label, None)
    if remove_instructions is None:
        remove_instructions = remove_json.get("lipsum")

    return create_response(remove_instructions)

@app.route('/')
def home():
    return 'Project Arise Backend'