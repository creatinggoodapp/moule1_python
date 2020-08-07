from project import app
from flask import redirect, render_template, url_for, Markup, request
from project.xu_ly.xu_ly_nhap_hang import *

#return render_template('nhan_vien_nhap_hang/index.html',chuoiHTML=Markup(chuoiHTML))

@app.route('/nhaphangtest',methods =['GET','POST'])
def nhaphang():
    tim_tivi =''
    chuoiHTML =''
    dsTivi = Doc_Danh_Sach_Tivi() # full list 
    if request.method =='POST':
        result = request.form
        tim_tivi =result.get('TH_tim_tivi')
        dsTimTivi = Tra_Cuu(tim_tivi,dsTivi)
        if len (dsTimTivi) > 0:
            chuoiHTML = Danh_sach_Tivi_Nhap_Hang_HTML(dsTimTivi)
        else:
            chuoiHTML = "Khong tim thay ten Tivi!"
            
    elif request.method == 'GET':
        chuoiHTML = Danh_sach_Tivi_Nhap_Hang_HTML(dsTivi)
    
    print(chuoiHTML)
    return render_template('khach_tham_quan/index.html',chuoiHTML=Markup(chuoiHTML))

#http://localhost:5001/nhan_vien_ban_hang?maso=
@app.route('/nhan_vien_nhap_hang',methods =['GET'])
def nhan_vien_ban_hang():
    tim_tivi =''
    chuoiHTML =''
    dsTivi = Doc_Danh_Sach_Tivi()
    if request.method =='GET':        
        tim_tivi = str(request.args.get('maso'))

        if len (tim_tivi) > 0:    
            dsTimTivi = Tra_Cuu_Ma_So(tim_tivi,dsTivi)
            chuoiHTML = Phieu_Nhap_HTML(dsTimTivi)            
        else:
            chuoiHTML = "Khong tim thay ten Tivi!"

    return render_template('nhan_vien_nhap_hang/index.html',chuoiHTML=Markup(chuoiHTML))
