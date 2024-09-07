import sqlite3

def test_find_contact(name):
    con = sqlite3.connect("jarvis.db")
    cursor = con.cursor()
    
    name = name.strip().lower()
    cursor.execute("SELECT mobile_no FROM contact1 WHERE LOWER(name) LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()
    
    print(f"Results for '{name}': {results}")
    
    con.close()

# Test the function with "Dad"
test_find_contact('Mom')
