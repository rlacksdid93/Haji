# dbMgr.py

import pymysql


def getConnection():   # 연결하는 함수
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='1234', db='haji', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)   # 자동으로 commit, 자동으로 dict의 형태로 변환.
    return conn


def join(data):   # 회원가입 데이터 DB에 insert
    try:
        conn = getConnection()   # 연결객체, DB연결
        cursor = conn.cursor()   # 커서객체
        sql = "INSERT INTO member(id, pwd, name) VALUES(%s, %s, %s)"   # 3개의 값을 넣음
        affected = cursor.execute(sql, data)   # 넘어온 데이터로 sql문 실행
        # print(affected)
        cursor.close()
    except Exception as e:
        print("join_member err========", e)
    finally : conn.close()
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


def login(data):
    try:
        conn = getConnection()   # 연결 객체. DB연결
        cursor = conn.cursor()
        sql1 = 'SELECT m_num FROM member WHERE id=%s'
        cursor.execute(sql1, data[0])   # data로 sql의 %s부분 채워서 실행.
        db_m_num = cursor.fetchone()['m_num']   # dict
        sql2 = 'select pwd from member where m_num=%s'
        cursor.execute(sql2, db_m_num)   # data로 sql의 %s부분 채워서 실행.
        db_pwd = cursor.fetchone()['pwd']
        if db_pwd==data[1]:
            print ("True")
        else : print("Flase")
        cursor.close()
    except Exception as e:   # 예외상황(프로그래머가 컨트롤해줘야 하는 상황) 발생 / cf.에러 : 프로그래머가 컨트롤 할 수 없는 상황
        print('login err===========', e)
    finally : conn.close()
    return    # 정상 : 1리턴 / 비정상 : 0리턴










if __name__ == '__main__':
    # pass

    # test : join_member() 
    # data = ('ttotto', '1234', '또치')
    # result = join_member(data)
    # print(result)

    # test : member_addi_info()
    # data = ('20', '여', '건성', '여드름', 'YYY 클렌징 오일', 4, '1234')
    # result = member_addi_info(data)
    # print(result)

    # test : login
    data = ('ttotto', '1234')
    login(data)
