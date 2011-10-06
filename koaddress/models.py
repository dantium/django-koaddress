from django.db import models

class Address(models.Model):
    code = models.CharField(max_length=8, db_index=True)
    city = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    
    def get_output(self):
        return "%s %s %s %s %s" % (self.code,self.city,self.town,self.area,self.block)
    
    def __unicode__(self):
        return "%s %s %s %s %s" % (self.code,self.city,self.town,self.area,self.block)