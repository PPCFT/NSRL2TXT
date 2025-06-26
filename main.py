import sqlite3

conn = sqlite3.connect("X:\\Hashsets\\RDS_2025.03.1_ios_minimal\\RDS_2025.03.1_ios_minimal.db")
cursor = conn.cursor()

with open('X:\\Hashsets\\NIST_ios_HashSet.txt', 'w', encoding='utf-8') as f:
    for row in cursor.execute('SELECT DISTINCT md5 FROM FILE ORDER BY md5'):
        f.write(''.join(map(str, row)) + '\n')