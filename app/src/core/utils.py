import os
import random
import re
import string
import json
from decimal import Decimal

from django.utils.text import slugify


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", None)
    return ip


def get_filename(path, new_filename=None):  # /abc/filename.mp4
    current_filename = os.path.basename(path)
    if new_filename is not None:
        filename, file_extension = os.path.splitext(current_filename)
        escaped_new_filename_base = re.sub(
            '[^A-Za-z0-9\#]+',
            '-',
            new_filename)
        escaped_filename = escaped_new_filename_base + file_extension
        return escaped_filename
    return current_filename


def upload_product_file_loc(instance, filename):
    slug = instance.product.slug
    # id_ = 0
    id_ = instance.id
    if id_ is None:
        Klass = instance.__class__
        qs = Klass.objects.all().order_by('-pk')
        id_ = qs.first().id + 1
    if not slug:
        slug = unique_slug_generator(instance.product)
    location = "product/{slug}/{id}/".format(slug=slug, id=id_)
    return location + filename  # "path/to/filename.mp4"


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_upper_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_key_generator(instance):
    """
    This is for a Django project with an key field
    """
    size = random.randint(30, 45)
    key = random_string_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(key=key).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return key


def unique_customer_id_generator(instance):
    """
    This is for a Django project with an order_id field
    """
    customer_new_id = random_upper_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(customer_id=customer_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return customer_new_id


def unique_order_id_generator(instance):
    """
    This is for a Django project with an order_id field
    """
    order_new_id = random_upper_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return order_new_id


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)
