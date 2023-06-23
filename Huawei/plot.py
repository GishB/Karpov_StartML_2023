import seaborn as sns
from matplotlib import pyplot as plt

import table

def plot(name_file: str = "some_file.csv", query: str = None, name_plot: str = "plot.png") -> plt.figure():
    '''
        This function helps to plot your SQL query
        
        Note: 
            To read your data you need to specify query or by default you will get some result based on some_data.csv file.
        Args:
            name_file: file name to work with (should be in csv format)
            name_plot: file name for your plot
            query: your SQL query (not working)
        Return:
            fig.savefig("plot.png")
    '''
    
    data = table.table(name_data=name_file)
    
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(data['Day'],data['A'])
    ax.fill_between(data['Day'], (data['A']-data['INTERVAL']),\
                    (data['A']+data['INTERVAL']), color='b', alpha=.1)
    sns.lineplot(data=data, x="Day", y="A")
    ax.set(ylim=(0, 1))
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    fig.savefig("plot.png") 
    
if __name__ == "__main__":
    plot()
    print('plot.png has been saved')