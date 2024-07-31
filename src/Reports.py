class Reports:
    def __init__(self,df):
        self.df=df

    def report_actual(self):
        self.df.to_csv('../Reports/Active_report.csv')

    def report_products_to_expire(self):
        out_of_stock= self.df[self.df["Quantity"]<10]
        out_of_stock.to_csv('../Reports/Report_products_to_expire.csv')

