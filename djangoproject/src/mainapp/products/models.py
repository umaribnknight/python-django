from django.db import models

TYPE_CHOICES = (
   ('appetizers', 'appetizers')
   ('entrees', 'entrees'),
   ('treats', 'treats'),
   ('drinks', 'drinks'),
)




class djangoClasses  (models.Model):
   type = models.CharField(max_length=60)
   name = models.Charfield(max_length=60, default="", blank=True, null=False)
   description = models.Textfield(max_length=300, default="", blank=True)
   price = models.DecimalField(default=0.00, maxdigits = 10000,decimal_places=2)
   image = models.Charfield(max_length=255, default='',blank=True,

   objects = models.Manager()

   def __str__(self):
       return self.name
