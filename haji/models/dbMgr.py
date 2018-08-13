# DB Mannager
import pymysql

def getConnection():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password ='1253', db='haji', charset='utf8', autocommit=True,cursorclass=pymysql.cursors.DictCursor) # 딕셔너리 형태로 변경하여 가져온다 
    return conn

def join_member(data):   # 회원가입 데이터 DB에 insert
    conn = getConnection()   # 연결객체, DB연결
    cursor = conn.cursor()   # 커서객체
    sql = "INSERT INTO member(id, pwd, name) VALUES(%s, %s, %s)"   # 3개의 값을 넣음
    affected = cursor.execute(sql, data)   # 넘어온 데이터로 sql문 실행
    cursor.close()
    conn.close()
    return affected


def member_addi_info(data):
    result = None
    try:
        conn = getConnection()   # 연결 객체. DB연결
        cursor = conn.cursor()
        sql = """
            update member 
            set age=%s, sex=%s, m_type=%s , 
            m_trouble=%s , used_prod=%s 
            where m_num=%s and pwd=%s
        """
        result = cursor.execute(sql, data)   # data로 sql의 %s부분 채워서 실행.
        cursor.close()
    except Exception as e:   # 예외상황(프로그래머가 컨트롤해줘야 하는 상황) 발생 / cf.에러 : 프로그래머가 컨트롤 할 수 없는 상황
        print('member_addi_info err===========', e)
    finally : conn.close()
    return result   # 정상 : 1리턴 / 비정상 : 0리턴

if __name__ =='__main__':
    data = ('26','Man','지성','모공','달팽이크림','1','1234')
    result = member_addi_info(data)
    print(result)