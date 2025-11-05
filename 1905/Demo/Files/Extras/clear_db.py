import sqlite3
import os

os.chdir(r'C:\Course\1905\Data')
con = sqlite3.connect('airline')
con.execute('''drop table aircraft''')
con.execute('''drop table airports''')
con.execute('''drop table flight''')
con.execute('''drop table reservations''')

con.close()
