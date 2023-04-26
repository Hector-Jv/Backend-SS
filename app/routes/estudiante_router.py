from flask import Blueprint, jsonify, request, redirect, url_for
from app import db


bp = Blueprint('estudiante_rutas', __name__)

@bp.route('/')
def listar_usuarios():
    return jsonify({'saludo': 'Hola Mundo'}), 201

