
from .models import User
import re


def showData(id):
    log = 'MOSTRANDO DATOS'
    print('ENTRAMOS A SHOWDATA con id: ',id)
    return log
    # qs = User.objects.all().values_list('liked')
    # print(qs)
    # app_names_list = list(val[0] for val in qs)