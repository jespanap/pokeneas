from flask import Blueprint, jsonify, render_template, request
from .s3_client import get_s3_client
import random, socket

pokenea_bp = Blueprint("pokenea", __name__)
BUCKET_NAME = "s3-bucketjd"
BASE_URL = f"https://{BUCKET_NAME}.s3.amazonaws.com/"

pokeneas = [
    {
        "id": 1,
        "nombre": "Arequipeachu",
        "altura": "0.6 m",
        "habilidad": "Dulce pegajoso",
        "imagen": f"{BASE_URL}Arequipeachu.jpg",
        "frase": "El sabor de la vida está en compartir el arequipe.",
    },
    {
        "id": 2,
        "nombre": "Bandejator",
        "altura": "1.2 m",
        "habilidad": "Frijol furioso",
        "imagen": f"{BASE_URL}Bandejator.jpg",
        "frase": "La fuerza viene de un buen almuerzo paisa.",
    },
    {
        "id": 3,
        "nombre": "Rappidrill",
        "altura": "0,4 m",
        "habilidad": "Bolsa naranja",
        "imagen": f"{BASE_URL}Rappidrill.jpg",
        "frase": "Si despues de una hora no llega se comio tu comida.",
    },
    {
        "id": 4,
        "nombre": "Traquetons",
        "altura": "1.6 m",
        "habilidad": "Cuchilla oxidada",
        "imagen": f"{BASE_URL}Traquetons.jpg",
        "frase": "No lo mires directamente a los ojos.",
    },
    {
        "id": 5,
        "nombre": "Cableon",
        "altura": "2.5 m",
        "habilidad": "Fila interminable",
        "imagen": f"{BASE_URL}Cableon.jpg",
        "frase": "No vayas a hora pico.",
    },
    {
        "id": 6,
        "nombre": "Choleons",
        "altura": "0.2 m",
        "habilidad": "Mata-calor",
        "imagen": f"{BASE_URL}Choleons.jpg",
        "frase": "Sueles verlo en epocas de calor.",
    },
    {
        "id": 7,
        "nombre": "Chuzeuns",
        "altura": "0.5 m",
        "habilidad": "Puya electrica",
        "imagen": f"{BASE_URL}Chuzeons.jpg",
        "frase": "Le gusta buscar nuevas carnes para su fuente de poder.",
    },
    {
        "id": 8,
        "nombre": "Marimonda",
        "altura": "1.3 m",
        "habilidad": "Disfraz carnavalero",
        "imagen": f"{BASE_URL}Marimonda.jpg",
        "frase": "Solo son visibles en febrero.",
    },
    {
        "id": 9,
        "nombre": "Mojarranser",
        "altura": "0,3 m",
        "habilidad": "Estafa extranjeros",
        "imagen": f"{BASE_URL}Mojarranser.jpg",
        "frase": "De repente su valor se multiplica por 25",
    },
    {
        "id": 10,
        "nombre": "Reguenton",
        "altura": "1.5 m",
        "habilidad": "No pega una",
        "imagen": f"{BASE_URL}MR.rime.jpg",
        "frase": "El nuevo coco de la palmera(No suena ni en su casa).",
    },
]

@pokenea_bp.route("/pokenea_json")
def get_pokenea_json():
    pokenea = random.choice(pokeneas)
    container_id = socket.gethostname()
    data = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": container_id,
    }
    return jsonify(data)


@pokenea_bp.route("/pokenea_img")
def get_pokenea_img():
    pokenea = random.choice(pokeneas)
    container_id = socket.gethostname()
    return render_template("pokenea.html", pokenea=pokenea, contenedor=container_id)

@pokenea_bp.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No se envió ningún archivo"}), 400

    file = request.files["file"]
    s3 = get_s3_client()

    try:
        s3.upload_fileobj(file, BUCKET_NAME, file.filename, ExtraArgs={"ACL": "public-read"})
        url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{file.filename}"
        return jsonify({"url": url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
