from psycopg2 import connect
from log import db_logger
from config import ACCESS_TOKEN_TABLE, SENSOR_READINGS_TABLE


class WorkerDB:
    def __init__(self, user: str, password: str, host: str, port: str, database: str):
        try:
            self.connection_db = connect(user=user,
                                         password=password,
                                         host=host,
                                         port=port,
                                         database=database)

            self._cursor = self.connection_db.cursor()
        except Exception:
            db_logger.exception("Error connecting to database")

    def create_table(self):
        sql_create_table_command = f"""CREATE TABLE IF NOT EXISTS {SENSOR_READINGS_TABLE}(
                                      id serial primary key,
                                      time TIMESTAMP DEFAULT now(),
                                      temperature double precision,
                                      pressure double precision,
                                      carbon_monoxide integer,
                                      humidity double precision);"""

        try:
            self._cursor.execute(sql_create_table_command)
            self.connection_db.commit()
        except Exception:
            db_logger.exception("Error creating table")

    def add_measurements(self, temperature: str,
                         pressure: str,
                         carbon_monoxide: str,
                         humidity: str):
        sql_insert_command = f"""
                            INSERT INTO {SENSOR_READINGS_TABLE} (
                            temperature, 
                            pressure,
                            carbon_monoxide,
                            humidity) 
                            VALUES (%s, %s, %s, %s);"""

        try:
            self._cursor.execute(sql_insert_command,
                                (float(temperature), float(pressure), float(carbon_monoxide), float(humidity)))
            self.connection_db.commit()
        except Exception:
            db_logger.exception(f"Error adding record: {temperature}, {pressure}, {carbon_monoxide}, {humidity}")

    def get_access_tokens(self):
        access_tokens = []
        try:
            sql_get_tokens_command = f"""SELECT * FROM {ACCESS_TOKEN_TABLE};"""
            self._cursor.execute(sql_get_tokens_command)
            access_tokens = self._cursor.fetchall()
        except Exception:
            db_logger.exception("Error get access tokes")

        return [token[-1] for token in access_tokens]

    def __del__(self):
        self.connection_db.close()
