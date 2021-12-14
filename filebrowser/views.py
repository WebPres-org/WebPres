
#/media/uploads/testfolder/testimage.jpg
#/media/uploads/blog/1/images/blogimage.jpg



def upload(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "inlude/upload.html")