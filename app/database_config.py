import psycopg2

host = 'localhost'
user = 'postgres'
port = 5432
dbname = 'politico'
password = 'Iamnumberone'

# con_url = "dbname = 'politico' host = 'localhost' port = '5432' user = 'postgres' password = 'Iamnumber1'"
# con_url = "dbname = 'd1er6cirgqjdqu' host = 'ec2-54-225-237-84.compute-1.amazonaws.com' port = '5432' user = 'dtckzifdavniru' password = 'ca23489d6c5341a7bf703b8c0cacdb80ec690b9fe6883d4a5123597747743758'"
con_url = "postgres://dtckzifdavniru:ca23489d6c5341a7bf703b8c0cacdb80ec690b9fe6883d4a5123597747743758@ec2-54-225-237-84.compute-1.amazonaws.com:5432/d1er6cirgqjdqu"
# .format([dbname,host,port,user,password])
# url = os.getenv([])


def connection(url):
    """returns connection"""
    con = psycopg2.connect(url)
    return con


def init_db():
    """returns connection and creates tables"""
    con = connection(con_url)
    cur = con.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
    con.commit()
    return con


def init_test_db():
    """returns connection and creates tables for tests"""
    con = connection(test_url)
    cur = con.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
    con.commit()
    return con


def destroydb():
    """deletes all tables after tests have been run"""
    con = connection(con_url)
    cur = con.cursor()

    users = "DROP TABLE IF EXISTS users CASCADE;"
    parties = "DROP TABLE IF EXISTS party CASCADE;"
    offices = "DROP TABLE IF EXISTS office CASCADE;"
    candidates = "DROP TABLE IF EXISTS candidate CASCADE;"
    votes = "DROP TABLE IF EXISTS vote CASCADE;"

    queries = [parties, offices, users, candidates, votes]

    for query in queries:
        cur.execute(query)
    con.commit()


def tables():
    """contains all table creation queries"""
    offices = """CREATE TABLE IF NOT EXISTS office (
        office_id serial PRIMARY KEY NOT NULL,
        name character varying(50) NOT NULL UNIQUE,
        office_type character varying(50) NOT NULL,
        date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );"""
    parties = """CREATE TABLE IF NOT EXISTS party (
        party_id serial PRIMARY KEY NOT NULL,
        name character varying(50) NOT NULL UNIQUE,
        hqAddress character varying(50) NOT NULL,
        logoUrl character varying(50) NOT NULL,
        date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );"""
    users = """CREATE TABLE IF NOT EXISTS users (
        user_id serial PRIMARY KEY NOT NULL,
        firstname character varying(50) NOT NULL,
        lastname character varying(50) NOT NULL,
        othername character varying(50) NOT NULL,
        email character varying(50) NOT NULL UNIQUE,
        phoneNumber character varying(50) NOT NULL UNIQUE,
        passportUrl character varying(50) NOT NULL,
        isAdmin boolean,
        password character varying(100) NOT NULL,
        date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );"""
    candidates = """CREATE TABLE IF NOT EXISTS candidate (
        candidate_id serial UNIQUE,
        user_id integer REFERENCES users(user_id),
        office_id integer REFERENCES office(office_id),
        PRIMARY KEY(user_id,office_id),
        date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );"""
    votes = """CREATE TABLE IF NOT EXISTS vote (
        vote_id serial UNIQUE,
        candidate_id integer REFERENCES candidate(candidate_id),
        voter_id integer REFERENCES users(user_id),
        office_id integer REFERENCES office(office_id),
        PRIMARY KEY(voter_id,office_id),
        date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );"""

    queries = [offices, parties, users, candidates, votes]
    return queries
