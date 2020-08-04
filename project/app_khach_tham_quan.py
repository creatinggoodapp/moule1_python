from project import app
from flask import redirect, render_template, url_for, Markup, request
from project.xu_ly.xu_ly_khach_tham_quan import *

@app.route('/',methods =['GET','POST'])
def index():
    tim_tivi =''
    chuoiHTML =''
    dsTivi = Doc_Danh_Sach_Tivi() # full list 
    if request.method =='POST':
        result = request.form
        tim_tivi =result.get('TH_tim_tivi')
        dsTimTivi = Tra_Cuu(tim_tivi,dsTivi)
        if len (dsTimTivi) > 0:
            chuoiHTML = Danh_sach_Tivi_HTML(dsTimTivi)
        else:
            chuoiHTML = "Khong tim thay ten Tivi!"
            
    elif request.method == 'GET':
        chuoiHTML = Danh_sach_Tivi_HTML(dsTivi)

    return render_template('khach_tham_quan/index.html',chuoiHTML=Markup(chuoiHTML))