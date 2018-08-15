# dbMgr.py
import pymysql
import time


def getConnection():
    conn = pymysql.connect(host='localhost', port=3307, user='root', password='1234', db='pythondb', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
    return conn


def board_write(data):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "INSERT INTO signin( names , pwd, age) VALUES(%s,%s,%s)"
    affected = cursor.execute(sql, data)
    cursor.close()
    conn.close()
    return affected

# def board_update(data):
#     result = None
#     try:
#         conn=getConnection()
#         cursor = conn.cursor()
#         sql = """
#         update board
#         set name=%s, title=%s,
#         content=%s, regdate=now()
#         where num=%s and pwd=%s     
#         """
#         result = cursor.execute(sql,data)
#         cursor.execute(sql,data)
#         cursor.close()

    # except Exception as e: #예외. 
    #     print('board_update err=====',e)
    # finally: #마지막에 close해줘야한다.연결객체 50개 만들게 되있어 디폴트 51개부터는 안돼
    #         #sql 은 메모리 끝까지 쓴다. 없을때까지. 3일에 한번 finally에서 클로즈 해줘야한다. 
    #     conn.close()
    # return result


# 방법 1 : try ~ finally
def board_list():
    rows = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = "SELECT * FROM board ORDER BY num DESC"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print("err=====", e)
    finally:
        conn.close()
    return rows


# 방법 2 : try ~ finally 와 with (cursor) 사용
def board_list2():
    rows = None
    try:
        conn = getConnection()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM board ORDER BY num DESC"
            cursor.execute(sql)
            rows = cursor.fetchall()
    except Exception as e:
        print("err=====", e)
    finally:
        conn.close()
    return rows


# 방법 3 : with 사용 <== 자동 close 가 안되니 사용하지 말아야 하는 코드 예
def board_list3():
    rows = None
    try:
        with getConnection() as cursor:
            sql = "SELECT * FROM board ORDER BY num DESC"
            cursor.execute(sql)
            rows = cursor.fetchall()
    except Exception as e:
        print("err=====", e)
    return rows


# def board_read(num):
#     row = None
#     try:
#         conn = getConnection()
#         cursor = conn.cursor()
#         sql = "SELECT * FROM board WHERE num=%s"
#         data = ( num )
#         cursor.execute( sql, data )
#         row = cursor.fetchone()
#     except Exception as e:
#         print('read err==========', e)
#     finally:
#         conn.close()
#     return row


# def board_hit_up(num):
#     try:
#         conn = getConnection()
#         cursor = conn.cursor()
#         sql = "UPDATE board set hit=hit+1 WHERE num=%s"
#         data = ( num )
#         cursor.execute(sql, data)
#         cursor.close()
#     except Exception as e:
#         print('hit up=========', e)
#     finally:
#         conn.close
		
# def board_delete(data):

#     result=None
#     try:
# 	    conn = getConnection()
# 	    cursor = conn.cursor()
# 	    sql="DELETE FROM board WHERE num=%s AND pwd=%s"
# 	    result=cursor.execute(sql,data)
# 	    cursor.close()
#     except Exception as e:
# 	    print('board_delete err=',e)
		
#     finally:
# 		    conn.close()
#     return result

# def comment_insert(data):
#     try:
#         conn= getConnection()
#         cursor = conn.cursor()
#         sql= "INSERT INTO comments(c_name,c_content,num) VALUES (%s,%s,%s)"
#         result=cursor.execute(sql,data)
#         cursor.close()
        
#     except Exception as e:
#         print("comment_insert err=====",e)
#     finally:
#         conn.close()
#     return result

# def comment_list(num):
#     rows=None
#     try:
#         conn=getConnection()
#         cursor = conn.cursor()
#         sql="SELECT * FROM commentsDESC WHERE num=%s ORDER BY c_no"
#         cursor.execute(sql,(num))
#         rows= cursor.fetchall()

if __name__ == '__main__':
    data=('홍길동','제목1','내용',2, '123')
    # result = board_update(data)
    # print(result)


