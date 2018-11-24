from django.shortcuts import render

#método para llamar los posts dentro de la vista
def post_list(request):
    return render(request, 'blog/post_list.html', {})