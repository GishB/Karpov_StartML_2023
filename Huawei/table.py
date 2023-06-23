import pandasql as psql
import pandas as pd


def table(name_data: str = 'some_data.csv', query: str = 'SELECT STRFTIME("%Y.%m.%d", DATE) AS Day,\
                                                          AVG(EVENT_RESULT) AS A,\
                                                          1.65*sqrt(((AVG(EVENT_RESULT) - EVENT_RESULT)*(AVG(EVENT_RESULT) -                                                                 EVENT_RESULT))/COUNT(EVENT_RESULT)) AS INTERVAL\
                                                          from data\
                                                          GROUP BY Day\
                                                          ORDER BY Day ASC;') -> pd.DataFrame:
    """
        This function via pandasql helps user read data.

        Note:
            To read your data you need to specify query or by default you will get some result based on some_data.csv file.
        Args:
            name_data: file name should be in csv format
            query: your SQL query
        Return:
            psql.sqldf(query)
    """
    data = psql.pd.read_csv('some_data.csv')
    return psql.sqldf(query)


if __name__ == "__main__":
    print(table())
    print('this is the result!')
