import pymysql

connection = pymysql.connect(host='localhost', user='root', password='', db='Python_Books', charset='utf8mb4', port=3307)


with connection.cursor() as cursor:

    sql = "SELECT * FROM Book_Table"

    cursor.execute(sql)

    result = cursor.fetchall()

    print(result)

        list1 = {}
        list1["book_id"] = self.book_id.get()
        list1["book_store"] = self.book_store.get()
        list1["book_name"] = self.book_name.get()
        list1["book_author"] = self.book_author.get()
        list1["book_isbn"] = self.book_isbn.get()
        list1["book_copies"] = self.book_copies.get()
        list1["book_checked"] = self.book_checked.get()
        for i in list1:
            print(i)