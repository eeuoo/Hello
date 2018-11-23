data = (    ('김**', 'M', 20, 'B', '노원구 중계동'),
            ('홍**', 'F', 20, 'C', '동래구 동래1동'),
            ('박**', 'M', 40, 'F', '영구 을미동'),
            ('최**', 'M', 30, 'A', '북구 만덕동'),
            ('강**', 'M', 90, 'A', '부구 덕천동'),
            ('갑**', 'M', 30, 'D', '속초시 중구'),
            ('박**', 'F', 30, 'C', '남구 대밭동'),
            ('김**', 'F', 20, 'B', '남구 논개동'),
            ('이**', 'F', 20, 'B', '전주시 맛구'),
            ('이**', 'M', 80, 'B', '바다구 물회동')  )

import sqlite3
 
conn = sqlite3.connect("exam.db")

with conn:
    cur = conn.cursor()
    sql = "insert into Student(name, gender, age, grade, addr ) values(?,?,?,?,?)"        
    cur.executemany(sql, data)
    
    conn.commit()
