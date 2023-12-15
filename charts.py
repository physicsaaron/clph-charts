from google.colab import drive, auth
import gspread
from google.auth import default


def prepare():
  drive.mount('/content/drive')
  auth.authenticate_user()
  creds, _ = default()
  gc = gspread.authorize(creds)
  !mkdir -p "/content/drive/My Drive/000_Nothing_Here_To_See"
  sh = gc.create('O_o')
  wb = gc.open('O_o').sheet1
  cell_list = wb.range('A1:Z1000')
  for cell in cell_list:
      cell.value="O_o"
  wb.update_cells(cell_list)
  !mv "/content/drive/My Drive/O_o.gsheet" "/content/drive/My Drive/000_Nothing_Here_To_See"
