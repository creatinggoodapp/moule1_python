import os
import json
def doc_file(_path):
    f = open(_path,'r', encoding='utf-8')
    noi_dung = json.load(f)
    f.close()
    return noi_dung

def ghi_file(_path, noi_dung):
    f =open(_path,'w', encoding='utf-8')
    json.dump(noi_dung,f,indent=4,ensure_ascii=False)
    f.close()
    return