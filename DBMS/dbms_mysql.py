import pymysql
#MySQL 서버 연결
conn = pymysql.connect(
    host = 'localhost',  #MySql주소
    user = 'root',  #유저이름
    password = '1234',   #비밀번호
    database = 'exampledb', #DB이름
    charset = 'utf8mb4',    #Encoding
    #pymysql.cursors.DictCursor = 조회된결과를 딕셔너리 형태로 반환
    cursorclass = pymysql.cursors.DictCursor
)
#cursor함수 객체 생성
cursor = conn.cursor()
#선택된 DB확인 + 명령어 실행
cursor.execute('SELECT DATABASE()')
#.fetchone() -> 한번호출에 하나의 row를 가져올때 사용 
print(f'현재대이터베이스 : {cursor.fetchone()}')
#DB 닫기
conn.close()
