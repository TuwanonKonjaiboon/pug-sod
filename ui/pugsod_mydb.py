import settings
import mysql.connector
import asyncio
from os import environ
from mysql.connector import Error
from datetime import datetime, date

MYSQL_USER = environ['MYSQL_USER']
MYSQL_PASSWORD = environ['MYSQL_PASSWORD']
MYSQL_HOST = environ['MYSQL_HOST']
MYSQL_DATABASE = environ['MYSQL_DATABASE']


class UserDB:

    async def login(self, email, password):
        try:

            connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )
            cursor = connection.cursor()

            # assertion
            assert email != ""
            assert password != ""

            q = """
                SELECT * FROM `user`
                WHERE `email` = %s AND `password` = %s;
            """

            cursor.execute(q, (email, password))
            res = cursor.fetchone()

            # test print user
            print(res)

            if res != None:
                return {'status': 1, 'msg': 'success', 'data': res}
            else:
                return {'status': 0, 'msg': 'not found'}

        except AssertionError:
            return {'status': 0, 'msg': 'email or password incorrect'}
        except:
            return {'status': 0, 'msg': 'error'}
        finally:
            if connection.is_connected:
                connection.close()
                cursor.close()

    # dont need to anything
    async def logout(self):
        pass


class ProductDB:
    async def createDB(self, user_id, product_title, product_detail, price, amount):
        try:

            connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )
            cursor = connection.cursor()

            # assertion
            assert product_title != ""

            cursor.execute("""
                INSERT INTO product (seller_id, product_title, product_detail, price, amount, update_at)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (
                user_id,
                product_title,
                product_detail,
                price,
                amount,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ))

            connection.commit()

            return {'status': 1, 'msg': 'create success'}
        except:
            connection.rollback()
            return {'status': 0, 'msg': 'create fail'}
        finally:
            if connection.is_connected:
                connection.close()
                cursor.close()

    async def readDB(self, query="", size=None):
        try:
            connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )

            q = """
                SELECT * FROM product
                WHERE
                    product_title LIKE '%{0}%'
                UNION
                SELECT * FROM product
                WHERE
                    product_detail LIKE '%{0}%'
                ORDER BY
                    avg_rating DESC, product_title ASC
            """.format(query)

            if type(size) is int:
                q = q + "\tLIMIT {}".format(size)

            cursor = connection.cursor()
            cursor.execute(q)

            res = cursor.fetchall()

            return {'status': 1, 'msg': 'read success', 'data': res}
        except:
            return {'status': 0, 'msg': 'read fail'}
        finally:
            if connection.is_connected:
                connection.close()
                cursor.close()

    async def updateDB(self, product_id, **values):
        try:
            connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )
            cursor = connection.cursor()

            # assertion
            assert len(values) != 0

            print("old values")
            cursor.execute(
                """SELECT * FROM product WHERE product_id = %s""", (product_id, ))
            record = cursor.fetchone()
            print(record)

            # print(f"""
            #     UPDATE product
            #     SET
            #         {','.join([ f"`{key}`='{val}'" for key, val in values.items()])}
            #     WHERE product_id = {product_id}
            # """)

            cursor.execute(f"""
                UPDATE product
                SET
                    {','.join(
                        [*[f"`{key}`='{val}'" for key, val in values.items()], 'update_at=NOW()'])}
                WHERE product_id = {product_id}
            """)
            connection.commit()

            print("after updated values")
            cursor.execute(
                """SELECT * FROM product WHERE product_id = %s""", (product_id, ))
            record = cursor.fetchone()
            print(record)

            return {'status': 1, 'msg': 'udpate success'}
        except:
            connection.rollback()
            return {'status': 0, 'msg': 'update fail'}

        finally:
            if connection.is_connected:
                connection.close()
                cursor.close()

    async def deleteDB(self, size=1, **kwargs):
        try:
            connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )
            cursor = connection.cursor()

            # keep before delete
            cursor.execute(
                f"""SELECT 
                        * 
                    FROM 
                        product 
                    WHERE  {'AND'.join([
                            f'{key}="{val}"' for key, val in kwargs.items()
                        ])}""")
            records = cursor.fetchone()

            # there is no data to delete
            if records == None:
                return {'status': 0, 'msg': 'not found'}

            cursor.execute(f"""
                DELETE FROM product 
                WHERE {'AND'.join([
                            f'{key}="{val}"' for key, val in kwargs.items()
                        ])}
                LIMIT {size}
            """)
            connection.commit()

            return {'status': 1, 'msg': 'delete success', 'data': records}
        except:
            connection.rollback()
            return {'status': 0, 'msg': 'delete fail'}
        finally:
            if connection.is_connected:
                connection.close()
                cursor.close()

    async def searchDB(self, query="", size=None):
        return self.readDB(query, size)


class OrderItemDB:
    async def createDB(self, user_id, product_id, quantity=1):
        try:

            connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO orderItem (customer_id, product_id, order_id, quantity)
                VALUES (%s, %s, NULL, %s);
            """, (user_id, product_id, quantity))

            connection.commit()

            return {'status': 1, 'msg': 'create success'}
        except:
            connection.rollback()
            return {'status': 0, 'msg': 'create fail'}
        finally:
            if connection.is_connected:
                connection.close()
                cursor.close()

    async def readDB(self, size=None, **kwargs):
        try:
            connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )

            q = f"""
                SELECT *
                FROM 
                    orderItem 
                WHERE {'AND'.join([
                    f'{key}="{val}"' for key, val in kwargs.items()
                ])}
            """

            if type(size) is int:
                q = q + "\tLIMIT {}".format(size)

            cursor = connection.cursor()
            cursor.execute(q)

            res = cursor.fetchall()

            return {'status': 1, 'msg': 'read success', 'data': res}
        except:
            return {'status': 0, 'msg': 'read fail'}
        finally:
            if connection.is_connected:
                connection.close()
                cursor.close()

    async def updateDB(self, orderItem_id, **values):
        try:
            connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )
            cursor = connection.cursor()

            # assertion
            assert len(values) != 0

            print(f"""
                UPDATE orderItem
                SET
                    {','.join([ f"`{key}`='{val}'" for key, val in values.items()])}
                WHERE orderItem_id = {orderItem_id}
            """)

            cursor.execute(f"""
                UPDATE orderItem
                SET
                    {','.join([f"`{key}`='{val}'" for key, val in values.items()])}
                WHERE orderItem_id = {orderItem_id}
            """)
            connection.commit()

            print("after updated values")
            cursor.execute(
                """SELECT * FROM orderItem WHERE orderItem_id = %s""", (orderItem_id, ))
            record = cursor.fetchone()
            print(record)

            return {'status': 1, 'msg': 'udpate success'}
        except:
            connection.rollback()
            return {'status': 0, 'msg': 'update fail'}

        finally:
            if connection.is_connected:
                connection.close()
                cursor.close()

    async def deleteDB(self, size=1, **kwargs):
        try:
            connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )
            cursor = connection.cursor()
            # keep before delete
            cursor.execute(
                f"""
                    SELECT * FROM orderItem 
                    WHERE {'AND'.join([
                            f'{key}="{val}"' for key, val in kwargs.items()
                        ])}
                """)
            records = cursor.fetchall()

            print(records)

            # there is no data to delete
            if records == None or len(records) <= 0:
                return {'status': 0, 'msg': 'not found'}

            cursor.execute(f"""
                DELETE FROM orderItem 
                WHERE {'AND'.join([
                            f'{key}="{val}"' for key, val in kwargs.items()
                        ])}
                LIMIT {size}
                """)
            connection.commit()

            return {'status': 1, 'msg': 'delete success', 'data': records}
        except:
            connection.rollback()
            return {'status': 0, 'msg': 'delete fail'}
        finally:
            if connection.is_connected:
                connection.close()
                cursor.close()
