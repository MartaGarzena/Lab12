from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():

    @staticmethod
    def getCountry():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gr.Country from go_retailers gr"""

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct YEAR(s.date) as y FROM go_daily_sales s  "

        cursor.execute(query)

        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getRetailers(country):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM go_retailers gr where gr.Country =%s"""

        cursor.execute(query, (country,))

        for row in cursor:
            result.append(Retailer(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(code1, code2, year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT count(distinct  s.Product_number) as peso
                    FROM go_daily_sales s, go_daily_sales s2 
                    where s.Retailer_code= %s
                    and s2.Retailer_code = %s
                    and s.Product_number=s2.Product_number 
                    and YEAR(s.date)=%s"""

        cursor.execute(query, (code1, code2, year))

        for row in cursor:
            result.append(row["peso"])
        cursor.close()
        conn.close()
        return result
