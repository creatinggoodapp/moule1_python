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
        noi_dung=doc_file(_path)
        Danh_sach.append(noi_dung)
    return Danh_sach

def Tra_Cuu(chuoi_tra_cuu,Danh_Sach_Tivi):
    Danh_sach = list(filter (lambda  Tivi: chuoi_tra_cuu.lower() in Tivi['Ten'].lower(),Danh_Sach_Tivi))
    return Danh_sach

# print(Doc_Danh_Sach_Tivi())
danhsachtracuu = Tra_Cuu("sony",Doc_Danh_Sach_Tivi())
print (len(danhsachtracuu))
for i in danhsachtracuu:
    print (i['Ten'])