import pymysql
#MySQL 서버 연결
conn = pymysql.connect(
    host = 'localhost',  #MySql주소
    user = 'root',  #유저이름
    password = '1234',   #비밀번호
    database = 'exampledb', #DB이름
)
#커서 생성 -> 명령어 작성
cursor = conn.cursor()
#명령어 실행
sql = 'SELECT  * FROM employees'
cursor.execute(sql)
employees = cursor.fetchall()
for employee in employees :
    print(employee)
print('데이터조회완료')
#DB 닫기
conn.close()
