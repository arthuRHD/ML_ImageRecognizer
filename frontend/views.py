from django.shortcuts import render, redirect
from .forms import UploadDocumentForm
from .models import Image
from .ml.lib.config import (img_height, img_width, export_dir, classnames, tested_picture_path)
import tensorflow as tf
from io import BytesIO
import numpy as np
import os

def upload_doc(request):
    form = UploadDocumentForm()
    logs = Image.objects.all()
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.get('file')
            dummy_file_path = os.path.join(os.path.dirname(__file__), "tmp/dummy.jpeg")
            with open(dummy_file_path, "wb+") as dummy_file:
                dummy_file.write(file.read())
            img = tf.keras.preprocessing.image.load_img(                
                dummy_file_path, target_size=(img_height, img_width)
            )
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0)

            model = tf.keras.models.load_model(export_dir)
            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0])

            classname_predicted = classnames[np.argmax(score)]
            resultat = f"Cette image appartient à la catégorie {classname_predicted} ({100 * np.max(score)})"            
            Image.objects.create(
                file=file,
                size=file.size,
                accuracy=round(100 * np.max(score), 2),
                class_name=classname_predicted
            ).save()
            os.remove(dummy_file_path)
            
    return render(request, 'upload_image.html', locals())

def clear_row(request):
    if request.method == 'GET':
        img = Image.objects.get(file=request.GET['log_row'])
        img.delete()
    return redirect("/upload")