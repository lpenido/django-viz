import os 

import pandas as pd

from .models import ScavengerPin

def load_data():
    scav = os.getenv("SCAV")
    df = pd.read_csv(scav)
    records = df.to_dict("records")
    
    print("Loading Data...")
    for i, rec in enumerate(records):
        print("Trying", i)
        #  'Tax Sale Year', 'PIN', 'Classification', 'Township Name',
        #  'Sold at Sale', 'Tax Amount Offered', 'Penalty Amount Offered',
        #  'Total Tax and Penalty Amount Offered', 'Cost', 'Total Amount Paid',
        #  'Total Amount Forfeited', 'Winning Bid Percent', 'Buyer Name',
        #  'location_1'
        try:
            sp = ScavengerPin(
                year = rec["Tax Sale Year"],
                pin = rec["PIN"],
                classification = rec["Classification"],
                township = rec["Township Name"],
                sold_at_sale = rec["Sold at Sale"],
                tax_amount_offered = rec["Tax Amount Offered"],
                pen_amount_offered = rec["Penalty Amount Offered"],
                total_tax_pen = rec["Total Tax and Penalty Amount Offered"],
                cost = rec["Cost"],
                total_amount_paid = rec["Total Amount Paid"],
                total_forfieted = rec["Total Amount Forfeited"],
                winning_bid_pct = rec["Winning Bid Percent"],
                buyer_name = rec["Buyer Name"],
                location_1 = rec["location_1"],
            )
            sp.save()
            
        except Error as e:
            print(e)
            breakpoint()

    print("Loaded Data.")

    



