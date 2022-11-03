from django.http import HttpResponse


__all__ = [
    "wishlist_view"
]

def wishlist_view(request):
    if "authstring" in request.session:
        pass

    if "authstring" in request.GET:
        pass

    html = "<html><body>It is now.</body></html>"
    return HttpResponse(html)
