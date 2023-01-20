# Import pandas library
import pandas as pd
import environment as envProp
import matplotlib.pyplot as plt


def break_down_code(response_api)-> pd.DataFrame:
    '''this function converts the raw data into pandas dataframe'''
    data=response_api.json()
    n_data=data.split("\n")
    print(type(n_data))
    li=[]
    for line in n_data:
        li.append(line.split("\t"))

    # Create the pandas DataFrame
    df = pd.DataFrame(li, columns = ['Timestamp', 'Values'])
    # df2=df.dropna(axis=1)
    df2 = df[df.Timestamp != '']
    # print dataframe.
    filename="csv_out.csv"
    return(df2 )
    # write_csv(df)

def write_csv(df,filename):
    df.to_csv(envProp.csv_output_path+"/"+filename)

    # print(li[:5])
    # print(n_data[:5])


def grouping_df(df):
    # df['new_date']=df["Timestamp"]
    # print(df.dtypes)
    df['new_date']=pd.to_datetime(df['Timestamp'])
    df['only_date']=df['new_date'].dt.date
    print(df)
    print("-----------------------------------------")
    df3=df.groupby(['only_date'])['only_date'].count()
    return(df3)
    # write_csv(df3,"grouped.csv")

    # print(df.dtypes)


def plot_graph(df):
    # Initialize the lists for X and Y
    data = pd.read_csv('/Users/sathishkumar/Desktop/Acciopy_02/project_api/outs/grouped.csv')

    df = pd.DataFrame(data)
    print(df)
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])
    print(X)
    print(Y)
    # Plot the data using bar() method
    plt.bar(X, Y, color='g')
    plt.title("Entries over adsl")
    plt.xlabel("Dates")
    plt.ylabel("No of Entries")

    # Show the plot
    plt.show()




"26-Aug-2021 19:36:07\t[['block1', 'block2'], ['block2', 'block3'], ['block3', 'block4'], ['block3', 'block5'], ['block3', 'block6'], ['block4', 'block6'], ['block5', 'block6'], ['block2', 'block6'], ['block7', 'block6']]", 
"26-Aug-2021 19:36:52\t[['A', 'B'], ['C', 'D']]", 
"26-Aug-2021 19:36:52\t[['A', 'B'], ['C', 'D']]", 
"26-Aug-2021 19:37:36\t[['A', 'B'], ['C', 'D']]", 
"26-Aug-2021 19:38:37\t[['dag_tal_gbl_feeds_stg_mrch_markdown_dly_1', 'dag_tal_ETL381D_mrch_markdown_dly_1'], ['dag_tal_ETL381D_mrch_markdown_dly_1', 'dag_tal_ETL382D_mrch_markdown_dly_1'], ['dag_tal_ETL382D_mrch_markdown_dly_1', 'dag_tal_ETL383D_mrch_markdown_dly_1'], ['dag_tal_ETL382D_mrch_markdown_dly_1', 'dag_tal_ETL380W_mrch_markdown_wkly_1'], ['dag_tal_ETL382D_mrch_markdown_dly_1', 'dag_tal_ETL383M_mrch_markdown_mnthly_1'], ['dag_tal_ETL383D_mrch_markdown_dly_1', 'dag_tal_ETL383M_mrch_markdown_mnthly_1'], ['dag_tal_ETL380W_mrch_markdown_wkly_1', 'dag_tal_ETL383M_mrch_markdown_mnthly_1'], ['dag_tal_ETL381D_mrch_markdown_dly_1', 'dag_tal_ETL383M_mrch_markdown_mnthly_1'], ['dag_tal_ETL380D_mrch_markdown_dly_1', 'dag_tal_ETL383M_mrch_markdown_mnthly_1']]"


[['26-Aug-2021 19:36:07', "[['block1', 'block2'], ['block2', 'block3'], ['block3', 'block4'], ['block3', 'block5'], ['block3', 'block6'], ['block4', 'block6'], ['block5', 'block6'], ['block2', 'block6'], ['block7', 'block6']]"], 
['26-Aug-2021 19:36:52', "[['A', 'B'], ['C', 'D']]"], 
['26-Aug-2021 19:36:52', "[['A', 'B'], ['C', 'D']]"], 
['26-Aug-2021 19:37:36', "[['A', 'B'], ['C', 'D']]"], ['26-Aug-2021 19:38:37', "[['dag_tal_gbl_feeds_stg_mrch_markdown_dly_1', 'dag_tal_ETL381D_mrch_markdown_dly_1'], ['dag_tal_ETL381D_mrch_markdown_dly_1', 'dag_tal_ETL382D_mrch_markdown_dly_1'], ['dag_tal_ETL382D_mrch_markdown_dly_1', 'dag_tal_ETL383D_mrch_markdown_dly_1'], ['dag_tal_ETL382D_mrch_markdown_dly_1', 'dag_tal_ETL380W_mrch_markdown_wkly_1'], ['dag_tal_ETL382D_mrch_markdown_dly_1', 'dag_tal_ETL383M_mrch_markdown_mnthly_1'], ['dag_tal_ETL383D_mrch_markdown_dly_1', 'dag_tal_ETL383M_mrch_markdown_mnthly_1'], ['dag_tal_ETL380W_mrch_markdown_wkly_1', 'dag_tal_ETL383M_mrch_markdown_mnthly_1'], ['dag_tal_ETL381D_mrch_markdown_dly_1', 'dag_tal_ETL383M_mrch_markdown_mnthly_1'], ['dag_tal_ETL380D_mrch_markdown_dly_1', 'dag_tal_ETL383M_mrch_markdown_mnthly_1']]"]]

