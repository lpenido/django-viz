from django.db import models

# Create your models here.
class Record(models.Model):

    # recorded_date, pin, type_desc, doc_num, first_grantor, first_grantee, first_prior_doc_num
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    count = models.IntegerField()

    def to_dict(self):
        return {
            "name": self.name,
            "data": self.date,
            "count": self.count
        }
