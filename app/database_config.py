import pdb
import psycopg2
import os
from tests.v2 import run_tests
import app


con_url = ""


class Database():

    def __init__(self):
        self.con_url = os.environ['DATABASE_URL']

    def connection(self, url):
        """returns connection"""
        con = psycopg2.connect(url)
        return con

    def init_db(self):
        """returns connection and creates tables"""
        con = self.connection(self.con_url)
        # print(str(self.con_url))
        cur = con.cursor()
        queries = self.tables()

        for query in queries:
            cur.execute(query)
        con.commit()
        return con

    def destroydb(self):
        """deletes all tables after tests have been run"""
        con = self.connection(self.con_url)
        cur = con.cursor()

        users = "DROP TABLE IF EXISTS users CASCADE;"
        parties = "DROP TABLE IF EXISTS party CASCADE;"
        offices = "DROP TABLE IF EXISTS office CASCADE;"
        candidates = "DROP TABLE IF EXISTS candidate CASCADE;"
        votes = "DROP TABLE IF EXISTS vote CASCADE;"
        petitions = "DROP TABLE IF EXISTS petition CASCADE;"

        queries = [parties, offices, users, candidates, votes]

        for query in queries:
            cur.execute(query)
        con.commit()

    def tables(self):
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
            logoUrl character varying(500) NOT NULL,
            date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
        );"""
        users = """CREATE TABLE IF NOT EXISTS users (
            user_id serial PRIMARY KEY NOT NULL,
            firstname character varying(50) NOT NULL,
            lastname character varying(50) NOT NULL,
            othername character varying(50) NOT NULL,
            email character varying(50) NOT NULL UNIQUE,
            phoneNumber character varying(50) NOT NULL UNIQUE,
            passportUrl character varying(500) NOT NULL,
            isAdmin boolean DEFAULT false,
            password character varying(100) NOT NULL,
            date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
        );"""

        candidates = """CREATE TABLE IF NOT EXISTS candidate (
            candidate_id serial UNIQUE,
            user_id integer REFERENCES users(user_id),
            office_id integer REFERENCES office(office_id),
            party_id integer REFERENCES party(party_id),
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
        petitions = """CREATE TABLE IF NOT EXISTS petition (
            petition_id serial UNIQUE,
            office_id integer REFERENCES office(office_id),
            user_id integer REFERENCES users(user_id),
            text character varying(900) NOT NULL,
            evidence character varying(900) NOT NULL,
            date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
        );"""

        queries = [offices, parties, users, candidates, votes, petitions]
        return queries
