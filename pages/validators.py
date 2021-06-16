from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


def clean_picture(image):
    w, h = get_image_dimensions(image)
    if w != 270:
        raise ValidationError("Bu rasmni uzunligi %i piksel. Rasmni uzunligi 270px bo'lishi kerak.(270x360)" % w)
    if h != 360:
        raise ValidationError("Bu rasmni bo\'yi %i piksel rasmni bo'yi 360px bo'lishi kerak.(270x360)" % h)
