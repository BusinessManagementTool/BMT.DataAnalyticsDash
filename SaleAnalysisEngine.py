import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from SQLDataLoader import SalesSQLRepository


class SaleAnalysisEngine:
    def __init__(self):
        # Create an instance of ClassA within ClassB
        self.SalesSQLRepositoryInstance = SalesSQLRepository()

    def perMonthSaleData(self):
        sales = self.SalesSQLRepositoryInstance.fetchSales()
        # Sample data (replace this with your actual data)
        orderIds = [item[0] for item in sales]
        orderdates = [item[1] for item in sales]
        data = {
            'OrderID': orderIds,
            'OrderDate': orderdates
        }

        # Convert 'OrderDate' to datetime
        df = pd.DataFrame(data)
        df['OrderDate'] = pd.to_datetime(df['OrderDate'])

        # Calculate per-day sales
        daily_sales = df.groupby('OrderDate')['OrderID'].count()

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-', color='b')
        plt.title('Per-Day Sales')
        plt.xlabel('Date')
        plt.ylabel('Number of Orders')
        plt.grid(True)
        plt.show()

