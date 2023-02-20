from server import app
from flask import flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os
import cv2 as cv
from uuid import uuid1

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
clt = KMeans(n_clusters=5)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def show_img_compar(img_1, img_2):
    img_id = uuid1()
    f, ax = plt.subplots(1, 2, figsize=(7,7))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis('off') 
    ax[1].axis('off')
    f.tight_layout()
    plt.savefig(f"static/palettes/{img_id}")
    
    return img_id

def generate_image_pallete(clusters):
    width = 500
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width / clusters.cluster_centers_.shape[0]
    for idx, centers in enumerate(clusters.cluster_centers_): 
        palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
    return palette
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed below')
        
        dim = (500, 300)
        img = cv.imread(f'./static/uploads/{filename}')
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

        clt_1 = clt.fit(img.reshape(-1, 3))
        palette = show_img_compar(img, generate_image_pallete(clt_1))
        
        return render_template('upload.html', filename=f'{palette}.png')
    else:
        flash('Allowed image types are ==> png, jpg, jpeg')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='palettes/' + filename), code=301)

if __name__ == "__main__":
    app.run(debug=True)