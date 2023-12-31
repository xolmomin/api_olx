from django.db.models import Model, DateTimeField


class BaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True, editable=False)


class BaseMeta:
    ordering = ('-id',)