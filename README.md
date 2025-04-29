# NSRL2TXT


1. Przerobienie SQL do listy txt

   ```python
   import sqlite3
   conn = sqlite3.connect("X:\\Hashsets\\RDS_2025.03.1_ios_minimal\\RDS_2025.03.1_ios_minimal.db")
   cursor = conn.cursor()
   with open('X:\\Hashsets\\NIST_ios_HashSet.txt', 'w', encoding='utf-8') as f:
       for row in cursor.execute('SELECT md5 FROM FILE'):
           f.write(''.join(map(str, row)) + '\n')
   ```

2. Posortowanie i usunięcie duplikatów:

   ` echo "MD5" > NISTWhiteList.txt`

   ` pv NISTHashSet.txt | sort --parallel=8 --buffer-size=16G | uniq >> NISTWhiteList.txt`

3. Przetwarzanie pliku XML zawierającego znane pliki i wyciągnięcie listy MD5

   `pv Raport.xml | grep -oP '(?<=<!\[CDATA\[)[a-f0-9]{32}(?=\]\]>)' >  /mnt/g/Hashsets/KnownFiles/Android_20250429.txt`

