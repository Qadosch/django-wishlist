from django.http import HttpResponse


__all__ = [
    "wishlist_view"
]

def wishlist_view(request):
    html = "<html><body>It is now.</body></html>"
    return HttpResponse(html)
