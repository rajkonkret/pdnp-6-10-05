# baza danych - przechowywanie danych
# sql, nosql
# # CRUD - insert, select, update, delete
# Działanie	Instrukcja  SQL	    HTTP	            DDS
# Create	            INSERT	PUT / POST	        write
# Read (Retrieve)	    SELECT	GET	                read / take
# Update	            UPDATE	POST / PUT / PATCH	write
# Delete (Destroy)	    DELETE	DELETE	            dispose

import sqlite3

try:
    conn = sqlite3.connect('baza_sqlite.db')
    c = conn.cursor()
    print("Baza danych zostałą podłączona")

    insert = """
    INSERT INTO software (id,name,price) VALUES (1,'Python',200);
    """

    select = """
    SELECT * FROM software;
    """

    update = """
    UPDATE software SET price=1000 WHERE id=1;
    """

    # c.execute(insert)
    # conn.commit()

    for row in c.execute(select):
        print(row)  # (1, 'Python', 200.0)

    # c.execute(update)
    # conn.commit()

    delete = """
    DELETE FROM software WHERE id=1;
    """

    c.execute(delete)
    conn.commit()

except sqlite3.Error as e:
    print("Bład połączenia z bazą", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
