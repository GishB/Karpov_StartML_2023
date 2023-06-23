import pandas as pd
import numpy as np

def generate_data(size: int = 1000, a: list = [0, 1],
                  p: list = [0.3, 0.7], data_start: str = '2023-04-04 00:00:00',
                  data_end: str = '2023-05-05 23:59:59',
                  name_csv: str = 'some_data.csv') -> pd.DataFrame:
    '''
        This function useful to generate random dataset between 2023.04.04 and 2023.05.05 with numpy and pandas.
    '''
    data = pd.DataFrame(pd.date_range(start=data_start,
                                             end=data_end, freq='S'), columns=['DATE'])\
                                            .sample(n=size)\
                                            .sort_values(by=['DATE'], ignore_index=True)
    data['EVENT_ID'] = np.arange(start=0+1, stop=size+1, step=1)
    data['EVENT_RESULT'] = np.random.choice(a=a, size=size, p=p)
    data.to_csv(name_csv, index=False)
    return data

if __name__ == "__main__":
    generate_data()
    print('some_data.csv has been generated')