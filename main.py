from flask import *
import time
import os
import requests
import pandas as pd
import datetime
import gspread
import sesmt
import smtplib, ssl
from email.message import EmailMessage

app = Flask(__name__,static_url_path='', static_folder='frontend/static',template_folder='frontend/templates')
app.secret_key = 'rudraisagoodboy'
port = int(os.environ.get("PORT", 5454))
# os.system('npx tailwindcss -i ./frontend/static/css/src/input.css -o ./frontend/static/css/dist/output.css')

@app.route('/')
@app.route('/index')
def index():
    session.clear()
    t1 = pd.read_csv('s1.csv')
    t2 = pd.read_csv('s2.csv')
    t3 = pd.read_csv('faqs.csv')
    # tm = "Hooray!! Registrations are open"
    # if(shet.unique_rows()>=600):
    tm = "Problem Statement are out!!"
    return render_template('index.html',timeline1=t1, len1=len(t1), timeline2=t2, len2=len(t2), faqs=t3, len3=len(t3),tm=tm)

@app.route('/register')
def register():
    # if("paycomplete" in session):
    #     if(session["paycomplete"]=="no"):
    #         return redirect(url_for('payment'))
    # if(shet.unique_rows()>=600):
    #     return render_template('register.html',reg=shet.unique_rows())
    return render_template('closed.html')


# @app.route('/submitform', methods=['POST', 'GET'])
# def submitform():
    if request.method == 'POST':
        fname = request.form['first-name']
        lname = request.form['last-name']
        col = request.form['col']
        colrno = request.form['colrno']
        prog = request.form['prog']
        year = request.form['year']
        pnum = request.form['pnum']
        email = request.form['email']
        pay = request.form['push-notifications']
        # shet.add_user(fname,lname,col,colrno,prog,year,pnum,email,pay)
        session['user'] = pnum
        session['fname'] = fname
        session['email'] = email
        session['pay'] = pay
        if(pay=="yes"):
            return redirect(url_for('payment'))
        else:
            l = sesmt.sendmail(email,fname,"no")
            if(l=="Sent"):
                session['paycomplete'] = "yes"
                # shet.mailsent(pnum,"yes")
            else:
                session['paycomplete'] = "yes"
                # shet.mailsent(pnum,"no") 
            return redirect(url_for('success'))
    return "Form Submitted Successfully"

# @app.route('/payment', methods=['POST', 'GET'])
# def payment():
#     session['paycomplete'] = "no"
#     if("user" not in session):
#         return redirect(url_for('index'))
#     return render_template('payment.html')

# @app.route('/submitpayment', methods=['POST', 'GET'])
# def pay():
#     if request.method == 'POST':
#         trid = request.form['trid']
#         pnum = session['user']
#         shet.update_pay(pnum,trid)
#         l = sesmt.sendmail(session['email'],session['fname'],"yes")
#         if(l=="Sent"):
#             session['paycomplete'] = "yes"
#             shet.mailsent(pnum,"yes")
#         else:
#             session['paycomplete'] = "yes"
#             shet.mailsent(pnum,"no")
#         session['paycomplete'] = "yes"
#         return redirect(url_for('success'))
#     return redirect(url_for('success'))

@app.route('/success')
def success():
    if("user" not in session):
        return redirect(url_for('index'))
    return render_template('success.html')

@app.route('/ps')
def ps():
    return render_template('ps.html')

@app.route('/fileac/<string:fname>')
def fileac(fname):
    return render_template('psview.html',pathoffile='/psfile/'+fname)

@app.route('/readu/<string:api>')
def readu(api):
    if(api=="mii81483uh3mo5pyeqgo80oaah7lws6hztijnmdv"):
        df = pd.read_csv('dataU.csv')
        return df.to_html()
    return "Invalid API Key"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)