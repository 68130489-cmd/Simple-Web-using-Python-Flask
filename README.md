โปรเจกต์นี้เป็นตัวอย่างการพัฒนาเว็บแอปพลิเคชันด้วย Flask (Python)
เพื่อศึกษาการใช้งาน @app.route, templates, และ static รวมถึงการนำค่าจากผู้ใช้มาประมวลผลด้วยฟังก์ชันจากไฟล์ภายนอก (mylib.py)

เว็บไซต์นี้มีทั้งหมด 5 ส่วนหลัก คือ

หน้าแนะนำสถานที่ท่องเที่ยว (/)
หน้าแสดงเทคโนโลยีที่สนใจ (/tech)
หน้าแสดงรหัสนักศึกษา (/myid)
หน้าแบบฟอร์มรับข้อมูลและผลลัพธ์ (/draw)
หน้าแสดงผลลัพธ์จากการรับข้อมูล (/result)
# โครงสร้างของโปรเจกต์
├─ Simple-Web-using-Python-Flask
   .
├── app.py                              # ไฟล์หลักของ Flask (กำหนด route แต่ละหน้า)
├── mylib.py                            # ไฟล์ฟังก์ชันที่ใช้คำนวณหรือประมวลผล (myfunc)
├── __pycache__
│   └── mylib.cpython-313.pyc
├── README.md
├── static                              # เก็บไฟล์ภาพ
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   ├── 4.jpg
│   ├── 5.jpg
│   ├── 6.jpg
│   ├── 7.jpg
│   └── 8.jpg
└── templates                            # เก็บไฟล์ HTML (Template)
    ├── draw.html                        # หน้า Input Form
    ├── index.html                       # หน้าแนะนำสถานที่ท่องเที่ยว
    ├── result.html                      # หน้าแสดงผลลัพธ์
    └── tech.html                        # หน้าเทคโนโลยีที่สนใจ
ขั้นตอนการสร้างเว็บด้วย Flask

ติดตั้ง Flask

pip install flask
สร้างไฟล์หลัก main.py ใช้สำหรับกำหนด route ของแต่ละหน้า เช่น /, /tech, /myid, /draw

สร้างโฟลเดอร์ templates/ เก็บไฟล์ HTML เช่น tourist-site.html, tech.html, draw.html, result.html

สร้างโฟลเดอร์ static/ สำหรับเก็บรูปภาพหรือไฟล์อื่น ๆ เช่น samui.png, cloud.png

สร้างไฟล์ mylib.py เก็บฟังก์ชันที่ใช้คำนวณหรือประมวลผล เช่น

 def myfunc(x, y):
 return x * y
เชื่อมโยง HTML กับ Flask ด้วย render_template() และใช้ request.form รับค่าจากแบบฟอร์ม (POST)

รันเว็บ

 http://127.0.0.1/
หรือ

http://localhost/

