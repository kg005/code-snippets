import gspread
from gspread import WorksheetNotFound
import gspread_dataframe as gsdf
from oauth2client import file as oauth_file

SPREADSHEET_ID = '16cBwJanevYpaJJMA2RSn_XdIvbEDKtIqZtYGwjt0dXA'

def init_worksheet(SPREADSHEET_ID, ws_name):
    """
    Returns a google worksheet object
    :param SPREADSHEET_ID: google spreadsheet id
    :param ws_name: worksheet name
    :return: google worksheet object
    """

    creds = oauth_file.Storage(f"{os.environ['HOME']}/token.json").get()
    gc = gspread.authorize(creds)
    wb = gc.open_by_key(SPREADSHEET_ID)

    try:
        ws = wb.worksheet(ws_name)
    except WorksheetNotFound:
        ws = wb.add_worksheet(ws_name, rows=1, cols=1)
    return ws


def write_to_google_sheet(df, SPREADSHEET_ID, ws_name, include_index=False, row=1, col=1):
    """
    writes into a google sheet
    :param include_index: whether to include index in output sheet
    :param df: pandas DF to write into the spreadsheet
    :param SPREADSHEET_ID: google spreadsheet id
    :param ws_name: worksheet name
    :param row: output starting row
    :param col: output starting column
    """
    ws = init_worksheet(SPREADSHEET_ID, ws_name)
    gsdf.set_with_dataframe(ws, df, resize=True, include_index=include_index)


def read_google_sheet(SPREADSHEET_ID, ws_name):
    """
    read from a google spreadsheet into a pandas DF
    :param SPREADSHEET_ID: google spreadsheet id
    :param ws_name: worksheet name
    """
    ws = init_worksheet(SPREADSHEET_ID, ws_name)
    df = gsdf.get_as_dataframe(ws, evaluate_formulas=True)
    return df



# write to gsheet
dart.write_to_google_sheet(input_pandas_dataframe, SPREADSHEET_ID, 'clicks_browse_session_id_2619479_w_timestamps_1571688082646_&_1571688082645', 1 , 1)

# read from gsheet
output_pandas_dataframe = read_google_sheet(SPREADSHEET_ID, 'sheet_name')


# auth set up , run once in jupyter
from oauth2client import file as oauth_file, client, tools
import os

class Args():
    logging_level = 'ERROR'
    noauth_local_webserver = None
    auth_host_port = []

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

store = oauth_file.Storage(f"{os.environ['HOME']}/token.json")

flow = client.flow_from_clientsecrets(f"{os.environ['HOME']}/credentials.json", scope)
creds = tools.run_flow(flow, store, Args())

# set up before
# Google OAuth2 Authorization
# Go to console.developers.google.com
# Create some project
# Credentials > Create OAuth client ID > Other > Some name > Create > OK
# Click on created access key and download json to your home on cluster as credentials.json
# Run following code in notebook

# Notes
# 1. Google Sheets
# Sharing results in Google Sheets with others is one of the most convenient methods of sharing. This guide will help you to export your pandas data frame from your Jupyter notebook into a Google spreadsheet:


# First, you need to authorize yourself with Google API as is described in this snippet: https://git.int.jumpshot.com/snippets/36 . A few notes:

# You will not be able to select Other before you actually fill in a certain form (a link to that form will be at the same page). All you really need to fill in is a name.
# After downloading the .json file, rename it to credentials.json and upload it in JupyterLab to your home.
# Run the authorization code in a notebook and follow its instructions.

# This is a one time thing and once it's done you do not need to run the code again (but you can).



# Secondly, you need to actually export the pandas data frame into Google Sheets. The relevant code is in this snippet: https://git.int.jumpshot.com/snippets/27 . A few notes:

# You need to create the spreadsheet manually in your Google Drive beforehand.
# The code is missing command import os.
# There are 3 variables that need to be changed to have the right values:

# SPREADSHEET_ID (from your spreadsheet's url)
# ws_name (the name of the sheet you want to write your data frame in – if it does not exists it will be created)
# df (the pandas data frame to export)


# It may happen that your first try will cause an error: ... Permission denied. .... The error message contains an url. Visit the url and allow Google Sheets API.