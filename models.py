import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def createpost(name, content):
    conn = sql.connect(path.join(ROOT, 'data.db'))
    cur = conn.cursor()
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content))
    conn.commit()
    conn.close()

def getposts():
    conn = sql.connect(path.join(ROOT, 'data.db'))
    cur = conn.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts

def reset():
    conn = sql.connect(path.join(ROOT, 'data.db'))
    cur = conn.cursor()
    cur.execute('drop table posts')
    makenew = """
                    create table posts (
                    tstamp datetime not null,
                    name text not null,
                    content text not null
                    );"""
    cur.execute(makenew)
    conn.commit()
    conn.close()
