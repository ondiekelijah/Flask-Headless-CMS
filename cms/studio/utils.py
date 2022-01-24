import secrets
import os
import urllib, re
from PIL import Image
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    abort,
    send_from_directory,
)
from flask import current_app

# image upload handler

def upload_img(post_img):

    random_hex = secrets.token_hex(8)
    
    _, f_ext = os.path.splitext(post_img.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, "static/images/uploads", picture_filename
    )
    post_img.save(picture_path)
    return picture_filename
