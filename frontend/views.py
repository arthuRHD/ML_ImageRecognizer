from django.shortcuts import render
from .forms import UploadDocumentForm
from .models import Image

def upload_doc(request):
    form = UploadDocumentForm()
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'upload_image.html', locals())