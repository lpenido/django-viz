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

class ScavengerPin(models.Model):
    """
    
    """
    #  'Tax Sale Year', 'PIN', 'Classification', 'Township Name',
    #  'Sold at Sale', 'Tax Amount Offered', 'Penalty Amount Offered',
    #  'Total Tax and Penalty Amount Offered', 'Cost', 'Total Amount Paid',
    #  'Total Amount Forfeited', 'Winning Bid Percent', 'Buyer Name',
    #  'location_1'
    year = models.IntegerField()
    pin = models.CharField(max_length=100)
    classification = models.IntegerField()
    township = models.TextField()
    sold_at_sale = models.BooleanField()
    tax_amount_offered = models.FloatField()
    pen_amount_offered = models.FloatField()
    total_tax_pen = models.FloatField()
    cost = models.FloatField()
    total_amount_paid = models.FloatField()
    total_forfieted = models.FloatField()
    winning_bid_pct = models.FloatField()
    buyer_name = models.CharField(max_length=250)
    location_1 = models.TextField()