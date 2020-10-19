import os
from os.path import join, dirname
import dotenv
import pymysql.cursors
import boto3

dotenv_path = join(dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

# 環境変数の値をAPに代入
DB_Host = os.environ.get("host")
DB_User = os.environ.get("user")
DB_Password = os.environ.get("pw")
DB_Name = os.environ.get("dbname")


def lambda_handler(event, context):
    client = boto3.client("rds")
    password = client.generate_db_auth_token(
        DBHostname=DB_Host, Port=3306, DBUsername=DB_User
    )
    connection = pymysql.connect(host=DB_Host,
                                 user=DB_User,
                                 password=password,
                                 db=DB_Name,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 ssl=dict(ssl={'ca': 'rds-ca-2019-root.pem'}))
    with connection.cursor() as cursor:
        sql = "SELECT * FROM t2"
        cursor.execute(sql)
        results = cursor.fetchall()
        for r in results:
            print(r)

    connection.close()


lambda_handler("", "");
