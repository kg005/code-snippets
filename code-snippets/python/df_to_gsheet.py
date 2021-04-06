import pandas as pd
import os
import gspread
from gspread import WorksheetNotFound
import gspread_dataframe as gsdf
from oauth2client import file as oauth_file, client

creds = oauth_file.Storage(f"{os.environ['HOME']}/token.json").get()
gc = gspread.authorize(creds)

SPREADSHEET_ID = '19ROrQ16imIK375sKZYhoQma8yE3wEr_YTSrlQfaqc38' # from spreadsheet url

worksheet_names = []
tables_list = []

for guid in example_guids:
    worksheet_names.append(guid)
    tables_list.append(examples_pd[examples_pd.guid == guid].sort_values('cts'))

i = 0
for ws_name in worksheet_names:
    wb = gc.open_by_key(SPREADSHEET_ID)                           
    try:
        ws = wb.worksheet(ws_name)
    except WorksheetNotFound:
        ws = wb.add_worksheet(ws_name, rows=1, cols=1)
    df = tables_list[i]
    gsdf.set_with_dataframe(ws, df, resize=True)
    i = i+1
i = 0