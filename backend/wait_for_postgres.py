from time import sleep;from psycopg import OperationalError,connect
def wait_for_postgres(host, port):
    while True:
        try:connection = connect(user="admin",password="admin",host=host,port=port,dbname="pycampadb_sl");connection.close();print("Postgres is up - executing command");break
        except OperationalError:print("Postgres is unavailable - sleeping");sleep(1)
if __name__ == "__main__":wait_for_postgres("db", "5432")