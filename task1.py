import psycopg2

def left_join():
    connection = psycopg2.connect("dbname=testing user=postgres")
    cursor = connection.cursor()
    cursor.execute("SELECT article.id, title, article.text FROM article LEFT JOIN comment ON article.id = article_id WHERE article_id IS NULL")
    return cursor.fetchall()

print(left_join())



