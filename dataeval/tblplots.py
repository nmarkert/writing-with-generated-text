import pandas as pd
from constants import INPUT_DIR, diverging_bar


def plot_table(tbl_name, save=False):
    df = pd.read_csv(INPUT_DIR + '/' + tbl_name + '.csv',  index_col='Version', sep=';')

    title = df.index[0]
    df = df.drop(title)

    diverging_bar(df, df.index, df.columns, title, save, tbl_name)


if __name__ == '__main__':
    for tbl in ['insp_helpfull', 'inspired', 'learning']:
        plot_table(tbl, True)
