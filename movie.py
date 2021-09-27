import sqlite3
conn=sqlite3.connect('Movies.db')
c=conn.cursor()
c.execute("""CREATE TABLE movie(
        Interesting_Movie text,
        lead_Actor text,
        Actress text,
        Year_of_Release integer,
        Director_name text
        )""")
c.execute("INSERT INTO movie VALUES('Interstellar','Mathew McCoughey','Jessica Chastain',2014,'Christopher Nolan')")
c.execute("INSERT INTO movie VALUES('Avatar','Sam Worthington','Zoe Saldana',2009,'James Cameron')")
print("Data successfully added...")
c.execute("SELECT rowid, * FROM movie")


items=c.fetchall()
for x in items:
    print(x)


print("Movie_name"+"\t\tLead_Actor"+"\t\tActress"+"\t\tDirector")
print("-------"+"\t\t--------"+"\t\t--------"+"\t--------")
for item in items:
    print(item[1]+"\t\t"+item[2]+"\t\t"+item[3]+"\t\t"+item[5])

conn.commit()
conn.close()