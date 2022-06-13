import sqlite3
#Мой тг ID 5279013889
def create_db():
    conn = sqlite3.connect('info.db')
    conn.execute("""CREATE TABLE "users" (
	"id"	INTEGER NOT NULL,
	"tgid"	INTEGER NOT NULL,
	"balance"	INTEGER,
	"permission"	INTEGER DEFAULT 0,
	"urls"	TEXT DEFAULT '',
    "url"	TEXT DEFAULT '',
	PRIMARY KEY("id" AUTOINCREMENT)
    )""")

def create_user(tgid, balance):
	conn = sqlite3.connect('info.db')
	sql = "INSERT OR IGNORE INTO users(tgid,balance) VALUES (?,?)"
	conn.execute(sql, [tgid, balance])
	conn.commit()

def check_user_exists(tgid):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    user_id = conn.execute("SELECT tgid FROM users WHERE tgid = ?", (tgid,)).fetchone()
    isExists = user_id is not None
    return isExists

def urls_to_str(urls):
    a = ",".join([str(x) for x in urls])
    #print(a, type(a))
    return [a]



def add_url(tgid, url):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()

    urls = conn.execute("SELECT urls FROM users WHERE tgid = ?", (tgid,)).fetchone()[0]
    if (urls == None or urls == ''):
        urls = [url]
        
    else:
        urls = urls.split(',')
        urls.append(url)
    print(urls_to_str(urls),tgid)
    conn.execute("""UPDATE users SET urls = ? WHERE tgid = ?""", (urls_to_str(urls)[0],tgid))
    conn.commit()

def check_balance(tgid):
    conn = sqlite3.connect('info.db')
    balance = conn.execute("SELECT balance FROM users WHERE tgid = ?", (tgid,)).fetchone()[0]
    return balance

def check_repeat_url(tgid, url):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    urls = conn.execute("SELECT urls FROM users WHERE tgid = ?", (tgid,)).fetchone()[0]
    result = url in urls
    return result

def get_url():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    urls = conn.execute("SELECT urls FROM users WHERE urls != ''").fetchall()[0][0]
    return urls

def get_tgid_by_url(url):
    conn = sqlite3.connect('info.db') 
    cursor = conn.cursor()
    tgid = conn.execute("SELECT tgid FROM users WHERE urls = ?",(url,)).fetchone()[0]
    return tgid

def delete_url_by_tgid(tgid, url):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    urls = conn.execute("SELECT urls FROM users WHERE tgid = ?", (tgid,)).fetchone()[0].split(',')
    urls.remove(url)
    conn.execute("""UPDATE users SET urls = ? WHERE tgid = ?""", (urls_to_str(urls)[0],tgid))
    conn.commit()

def put_active_url(tgid, url):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()   
    conn.execute("""UPDATE users SET url = ? WHERE tgid = ?""", (url,tgid))
    conn.commit()

def check_empty_active_url(tgid):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    result = None
    url = conn.execute("SELECT url FROM users WHERE tgid = ?",(tgid,)).fetchone()[0] 
    if (url ==''):
        result = True
    else:
        result = False
    return result 