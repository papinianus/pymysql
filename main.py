import os
from os.path import join, dirname
import dotenv
import pymysql.cursors

dotenv_path = join(dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

# 環境変数の値をAPに代入
DB_Host = os.environ.get("host")
DB_User = os.environ.get("user")
DB_Password = os.environ.get("pw")
DB_Name = os.environ.get("dbname")


def lambda_handler(event, context):
    connection = pymysql.connect(host=DB_Host,
                                 user=DB_User,
                                 password=DB_Password,
                                 db=DB_Name,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = "SELECT * FROM t2"
        cursor.execute(sql)
        results = cursor.fetchall()
        for r in results:
            print(r)

    connection.close()


lambda_handler("", "");
