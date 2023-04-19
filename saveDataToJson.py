import json
# وارد کردن کلاس از ماژول
from kala import kala

# ساخت دیتای مجازی
kalas = [kala("link_1","image_link_1","Kala_1","145,0000"),kala("link_2","image_link_2","Kala_2","150,0000","4.5")]

# باز کردن فایل 
with open('kala.json', 'w') as f:
    # __dict__ باعث گرفتن دیتا به صورت دیکشنری می شود
    #json.dump خروجی را در فایل ذخیره می کند
    json.dump([p.__dict__ for p in kalas], f)