import csv
import os, os.path, codecs
from django.conf import settings
from django.core.management.base import BaseCommand

from koaddress.models import Address

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../"))

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        Address.objects.all().delete()
        count = 0
        datafile = os.path.join(data_dir, 'data/korea_address.csv')
        datafile = codecs.open(datafile.decode('Korean'), mode="rb",)
        c = csv.reader(datafile)
        for row in c:
            Address.objects.create(code=row[0].decode('Korean'), city=row[1].decode('Korean'), town=row[2].decode('Korean'), area=row[3].decode('Korean'), block=row[4].decode('Korean'), )
            count += 1 
        del c
        print "Imported %d" % count