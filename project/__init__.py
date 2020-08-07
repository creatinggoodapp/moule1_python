from flask import Flask

app = Flask(__name__)
app.secret_key = 'dn2020'

appnvnhaphang= Flask(__name__)
appnvnhaphang.secret_key = 'dn2020'

import project.app_khach_tham_quan
import project.app_nhan_vien_ban_hang
import project.app_nhan_vien_nhap_hang
import project.app_quan_ly_ban_hang
import project.app_quan_ly_cong_ty
import project.app_quan_ly_nhap_hang