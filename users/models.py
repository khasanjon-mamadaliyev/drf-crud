from django.db.models import CharField, Model


class Member(Model):
    name = CharField('name', max_length=150, blank=True, null=True)
