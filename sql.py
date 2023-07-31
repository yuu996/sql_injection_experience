import mysql.connector

# クレデンシャル情報を書き換えてください
config = {
    'user': 'username',  # データベースユーザー名
    'password': '',  # データベースパスワード
    'host': 'localhost',  # データベースホスト（ローカルホストの場合）
    'database': 'user'  # データベース名
}
# MySQLに接続
connection = mysql.connector.connect(**config)

# カーソルの作成
cursor = connection.cursor()

# ユーザ名の入力（ここでSQLインジェクションの脆弱性がある）
search_username = input("ユーザ名を入力してください: ")
search_password = input("ログインパスワードを入力してください: ")

# ユーザテーブルからユーザ名とパスワードを取得するクエリ（SQLインジェクションの脆弱性あり）
query = f"SELECT * FROM users WHERE username = '{search_username}' AND password = '{search_password}' "
cursor.execute(query)

# 結果の取得
result = cursor.fetchall()
if result:
    for res in result:
        print(res)
    print("---------------------------------------")
    print("ログインに成功しました。")
    print("---------------------------------------")
else:
    print("---------------------------------------")
    print("ログイン失敗\nユーザ名かパスワードが一致しませんでした。")
    print("---------------------------------------")
# カーソルと接続をクローズ
cursor.close()
connection.close()

# ' OR '1'='1
# 'OR '1' = '1';--
# drop table users;--