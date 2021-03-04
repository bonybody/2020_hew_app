from flask import Blueprint, request, jsonify
from flask_jwt import JWT, jwt_required, current_identity, current_app
import logging
import json
from api.models import User, Auth
from api.database.database import db
from api.plugin.aws_s3 import item_image_bucket
import io

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/', methods=['get'])
@jwt_required()
def get():
    print(current_identity)
    user = User.getUserInfo(current_identity.id)
    user_dict = user.__dict__
    user_dict.pop('_sa_instance_state')

    return jsonify(user_dict)


@bp.route('/', methods=['post'])
def post():
    user_data = json.loads(request.form['params'])
    image = ''
    current_app.logger.debug(request.files)

    for key in request.files:
        image = request.files[key]
        current_app.logger.debug(image)
        response = item_image_bucket.put_object(
            Body=io.BufferedReader(image).read(),
            Key=f's3/user-images/' + str(image.filename)
        )
        image = current_app.config['ITEM_IMAGE_BASE'] + response.key

    user = User(
        display_name=user_data['display_name'],
        image=image,
        name=user_data['name'],
        name_ruby=user_data['name_ruby'],
        birthday=user_data['birthday']
    )
    postUser = user.postRecord()
    auth = Auth(
        user_id=postUser.id,
        email=user_data['email'],
        password=user_data['password']
    )
    auth.postRecord()
    return jsonify({'state': True})
