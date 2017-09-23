import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

def add_weight( weight ):
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

    gc = gspread.authorize(credentials)

    w = gc.open("scale-weight").sheet1

    d = datetime.date.today()
    today = d.strftime("%m/%d/%y")

    formula = '=SUM(R[-6]C[-1]:R[0]C[-1])/COUNTA(R[-6]C[-1]:R[0]C[-1])'

    w.append_row([today, weight, formula])
