import gspread
import datetime

gc = gspread.service_account(filename='she1key.json')
sh = gc.open(title='csihack2')
sheet = sh.sheet1

def add_user(fname,lname,col,colrno,prog,year,pnum,email,pay):
    sheet.append_row([str(datetime.datetime.now()),fname,lname,col,colrno,prog,year,pnum,email,pay])
    return "Added"

def update_pay(pnum,trcid):
    cell = sheet.find(pnum)
    crow = cell.row
    ccol = cell.col
    sheet.update_cell(crow, ccol+3, "yes")
    sheet.update_cell(crow, ccol+4, str(trcid))
    return "Updated"

def mailsent(pnum,val):
    cell = sheet.find(pnum)
    crow = cell.row
    ccol = cell.col
    sheet.update_cell(crow, ccol+5, val)
    return "Updated"

def unique_rows():
    l = sheet.col_values(8)
    return len(set(l))+120