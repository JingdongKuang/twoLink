import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from TL.db import get_db

bp = Blueprint('forward', __name__)

@bp.route('/hello')
def hello():
   return 'Hello, World!'
     
@bp.route('/forward')
def forward():
   return render_template("forward.html")

@bp.route('/addNum',methods = ['POST', 'GET'])
def addNum():
   if request.method == 'POST':
      try:
         db = get_db()
         
         L1 = float(request.form['L1'])
         print(L1,type(L1))
         
         L2 = float(request.form['L2'])
         Theta1 = float(request.form['Theta1'])
         Theta2 = float(request.form['Theta2']) 
         X=L1*
         Y=  
         db.execute("INSERT INTO forward_Data (L1,L2,Theta1,Theta2,X,Y) \
            VALUES (?,?,?,?,?,?)",(L1,L2,Theta1,Theta2,X,Y) )  
         db.commit()
         msg = "Record successfully added"
         
      except:
         db.rollback()
         msg = "error in insert operation"
            
      finally:
         location_x=0
         location_y=0
         return render_template("result.html",msg = msg,
                           location_x=location_x,location_y=location_y)
         con.close()
         
