from flask import Markup, url_for
import os
import json
from project.thu_vien.libFile import *
thu_muc_tu_lieu = "project/du_lieu"
thu_muc_tivi = "project/du_lieu/Tivi/"

def Doc_Danh_Sach_Tivi():
    Danh_sach = []
    for ten_file_json in os.listdir(thu_muc_tivi):
        _path = thu_muc_tivi + ten_file_json
        #print (_path)
        noi_dung= doc_file(_path)
        Danh_sach.append(noi_dung)
    return Danh_sach

def Tra_Cuu(chuoi_tra_cuu,Danh_Sach_Tivi):
      Danh_sach = list(filter (lambda  Tivi: chuoi_tra_cuu.lower() in Tivi['Ten'].lower(),Danh_Sach_Tivi))
      return Danh_sach

def Tra_Cuu_Ma_So(chuoi_tra_cuu,Danh_Sach_Tivi):
      Danh_sach = list(filter (lambda  Tivi: chuoi_tra_cuu == Tivi['Ma_so'],Danh_Sach_Tivi))
      return Danh_sach


def Danh_sach_Tivi_Ban_Hang_HTML(Danh_sach_Tivi):
  chuoiHTML =''
  for tivi in Danh_sach_Tivi:
    chuoiHTML += '''<div class="col-md-3">
      <img src="'''+ url_for('static',filename='media/'+tivi['Ma_so']+'.png') + '''" class="card-img-top" width="158" height="150">
      <div class="card-body">
        <h5 class="card-title">'''+ tivi['Ten'] +'''</h5>
        <p class="card-text">'''+ str(tivi['Don_gia_Ban']) +'''VND </p>
        <a href="http://127.0.0.1:5001/nhan_vien_nhap_hang?maso=''' + str(tivi['Ma_so']) + '''"> Nhap </a>
      </div>
      </div>'''
    print (str(tivi['Ma_so']))
  return chuoiHTML


def Phieu_Nhap_HTML(Danh_sach_Tivi):
  chuoiHTML =''
  for tivi in Danh_sach_Tivi:
    chuoiHTML += '''<div class="col-md-3">
      <h1>Phiếu Nhập</h1>
      <img src="'''+ url_for('static',filename='media/'+tivi['Ma_so']+'.png') + '''" class="card-img-top" width="158" height="150">
      <div class="card-body">
        <h5 class="card-title">'''+ tivi['Ten'] +'''</h5>
        <p class="card-text">Don gia nhap: '''+ str(tivi['Don_gia_Nhap']) +'''VND </p>
        <p class="card-text">So luong ton: '''+ str(tivi['So_luong_Ton']) +'''</p>
      </div>
      </div>
      <form method="POST"> 
        <div class="form-group">
          <input type="text" class="form-control" name="TH_so_luong_nhap">
        </div>
          <button type="submit" class="btn btn-primary">Dong y</button>
      </form>'''

  return chuoiHTML

