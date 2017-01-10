import gspread
import bt_check
from oauth2client.service_account import ServiceAccountCredentials

LOCATION = "Gym"

# load up the attendance sheet
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/17DpK516LjWdcCsMMlm5w5A6HUawn5TS0eeIj7zWiVyk')
worksheet = sh.get_worksheet(0)

# grab the list of BlueTooth addresses
# this sloppy approach doesn't scale past 79 students
bt_cell_list = worksheet.range('C2:C80')
bt = bt_check.Btcheck()

for cell in bt_cell_list:
    if bt.check_bluetooth(cell.value):
        worksheet.update_cell(cell.row, 4, LOCATION)



