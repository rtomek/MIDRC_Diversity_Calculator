import pandas as pd


def excelparse(filename, sheet_name):
    """
    Parse a spreadsheet using the filename and sheet name specified and return a pandas dataframe

    :param string filename: filename to open
    :param string sheet_name: sheet name to parse
    :return: pandas dataframe
    """

    # This opens the file and creates a list of sheet names, along with necessary readers
    # TODO: this should probably be separate in case wse want multiple sheets
    xls = pd.ExcelFile(filename)

    # This reads all Excel sheets, probably not worth it
    # df_map = pd.read_excel(xls)

    # This reads in the specified worksheet
    df = pd.read_excel(xls, sheet_name)

    # Find the columns that are percentages of the total distribution
    pct_cols = [col for col in df.columns if '(%)' in col]

    return df[['date'] + pct_cols]
