from Logger import LoggerFactory


class Reports:
    def __init__(self,df):
        self.df=df
        self.logger = LoggerFactory.create_logger('console')

    def current_report(self):
        self.df.to_csv('../Reports/Active_report.csv')
        msg ='An actual report has been successfully created'
        self.logger.info(msg)
        print('A current report has been successfully created')

    def products_to_expire_report(self):
        out_of_stock= self.df[self.df["Quantity"]<10]
        out_of_stock.to_csv('../Reports/Report_products_to_expire.csv')
        msg ='A products to expire report has been successfully created'
        self.logger.info(msg)
        print('A products to expire report has been successfully created')

    def assets_balance_report(self):
        self.df['Balance'] = self.df['Quantity']*self.df['Price']
        balance_assets = self.df.groupby(['Type'])['Balance'].sum('Balance').reset_index()
        balance_assets.to_csv('../Reports/assets_balance_report.csv')
        msg ='An assets balance report has been successfully created'
        self.logger.info(msg)
        print('An assets balance report has been successfully created')