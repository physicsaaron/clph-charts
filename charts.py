from google.colab import drive, auth
import gspread
from google.auth import default
import requests
import os
import shutil
import time

def prepare():
  try:
    drive.mount('/content/drive')
  except:
    error=True
  auth.authenticate_user()
  creds, _ = default()
  gc = gspread.authorize(creds)
  gcloud_token = !gcloud auth print-access-token
  gcloud_tokeninfo = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=' + gcloud_token[0]).json()
  userEmail = gcloud_tokeninfo['email']
  try:
    os.mkdir("/content/drive/My Drive/000_Nothing_Here_To_See")
  except:
    error=True
  sh = gc.create('O_o')
  time.sleep(1)
  wb = gc.open('O_o').sheet1
  cell_list = wb.range('A1:Z1000')
  for cell in cell_list:
      cell.value="O_o"
  wb.update_cells(cell_list)
  time.sleep(2)
  try:
    shutil.move("/content/drive/My Drive/O_o.gsheet", "/content/drive/My Drive/000_Nothing_Here_To_See")
  except:
    os.remove("/content/drive/My Drive/O_o.gsheet")
