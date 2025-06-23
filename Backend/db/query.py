import bcrypt
from db.conn import create_connection

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def insert_user(name, useremail, password, firstname, lastname, account_status='Active'):
    connection = create_connection()
    if connection:
        try:
            hashed_password = hash_password(password)

            cursor = connection.cursor()
            sql = """
                INSERT INTO users (name, useremail, password, firstname, lastname, account_status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (name, useremail, hashed_password, firstname, lastname, account_status)
            cursor.execute(sql, values)
            connection.commit()
            print("✅ User inserted successfully with hashed password.")
            return True

        except Exception as e:
            print(f"❌ Error inserting user: {e}")
            return False

        finally:
            cursor.close()
            connection.close()
            print("🔒 Connection closed after insert.")

def login_user(useremail, password):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT * FROM users WHERE useremail = %s OR name = %s"
            cursor.execute(sql, (useremail, useremail))  # ✅ Provide two parameters

            user = cursor.fetchone()

            if user and check_password(password, user['password']):
                print("✅ Login successful.")
                return user
            else:
                print("❌ Invalid email or password.")
                return None

        except Exception as e:
            print(f"❌ Error during login: {e}")
            return None

        finally:
            cursor.close()
            connection.close()
            print("🔒 Connection closed after login.")

