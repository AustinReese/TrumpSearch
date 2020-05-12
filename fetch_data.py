import sqlite3

def fetch_data(form):
    
    mentioned = form.mentioned.data
    hashtag = form.hashtag.data
    keystring = form.keystring.data
    
    sql_query = "SELECT * FROM trump WHERE "
    
    if mentioned != "":
        sql_query += f"mentions LIKE '%@{mentioned}%' AND "
    if hashtag != "":
        sql_query += f"hashtags LIKE '%#{hashtag}%' AND " 
    if keystring != "":
        sql_query += f"content LIKE '%{keystring}%'"
        
    if sql_query == "SELECT * FROM trump WHERE ":
        sql_query = sql_query[:-6]
    elif keystring == "":
        sql_query = sql_query[:-4]
    
    sql_query += "LIMIT 100;"
    
    conn = sqlite3.connect('secure_database.db')
    curs = conn.cursor()
    
    #good code
    #curs.execute(sql_query)

    #bad code
    try:
        curs.execute(sql_query)
    except sqlite3.Warning:
        curs.executescript(sql_query)
    # good code
    #headers = [des[0] for des in curs.description]

    # bad code
    headers = ['id', 'link', 'content', 'date', 'retweets', 'favorites', 'mentions', 'hashtags']
    
    #fatal query in keystring field
    #a%';drop table trump ;
    #create table trump(
    #id text,
    #link text,
    #content text,
    #date text,
    #retweets text,
    #favorites text,
    #mentions text,
    #hashtags text,
    #foo text);
    #insert into trump (id, link, content, date, retweets, favorites, mentions, hashtags, foo)
    #select name, birthday, address, phone_number, email, ssn, credit_card_number, credit_card_code, credit_card_expire from user_data;
    #select * from trump where content like '%a
 
    res = curs.fetchall()
    conn.close()
    return res, headers
