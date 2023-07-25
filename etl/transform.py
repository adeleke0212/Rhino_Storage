import pandas as pd


def join_transaction_df():
    trans1_df = pd.read_csv('Datasets/transaction1.csv')
    trans2_df = pd.read_csv('Datasets/transaction2.csv')
    transactions_df = pd.concat([trans1_df, trans2_df], ignore_index=True)
    # transactions_df.to_csv('Datasets/transactions.csv')
    return transactions_df


def convertdate(transactions_df):
    transactions_df['date'] = pd.to_datetime(transactions_df['date'])
    return transactions_df


def splitdate(transactions_df):
    transactions_df['year'] = pd.DatetimeIndex(transactions_df['date']).year
    transactions_df['month'] = pd.DatetimeIndex(transactions_df['date']).month
    transactions_df['day'] = pd.DatetimeIndex(transactions_df['date']).day
    transactions_df['day_of_week'] = pd.DatetimeIndex(
        transactions_df['date']).day_of_week
    return transactions_df


def saveDataframe(transactions_df):
    transactions_df.to_csv('Datasets/transactions_trans.csv')


transactions_df = join_transaction_df()
transactions_df = convertdate(transactions_df)
transactions_df = splitdate(transactions_df)
transactions_df = saveDataframe(transactions_df)

# def runTransformation():
#     transactions_df = join_transaction_df()
#     transactions_df = convertdate(transactions_df)
#     transactions_df = splitdate(transactions_df)
#     transactions_df = saveDataframe(transactions_df)
