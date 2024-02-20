import sqlite3

#подлючение к базе данных
connection = sqlite3.connect('pablic')

#создание таблиц
cursor = connection.cursor()

punishmane_table = """
    CREATE  TABLE IF NOT EXISTS punishments (
    name STRING NOT NULL,
    second_name STRING NOT NULL,
    father_name STRING NOT NULL,
    date_of_birthday DATE
    );
"""

regions_jale = """
    CREATE TABLE IF NOT EXISTS jale_regions (
    regions STRING NOT NULL,
    index INT NOT NULL,
    jail_name STRING NOT NULL
    );
"""

cursor.execute(punishmane_table)
cursor.execute(regions_jale)
connection.commit()