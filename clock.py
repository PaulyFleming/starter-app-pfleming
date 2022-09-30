from apscheduler.schedulers.blocking import BlockingScheduler 
import psycopg2
import time, os
from datetime import datetime   

# this is only here for speed - in an actual app I would not do this.
DATABASES = [
    {"name": "HEROKU_POSTGRESQL_STARTER_AMBER_URL",  "connection_url": "postgres://u2nro9e7skkvpa:p3c453fdeddc4fade1076e60667b7cd0f844e1093e36187faeef577de5d82b631@ec2-54-156-74-18.compute-1.amazonaws.com:5432/d9ba10ld43hpt2"},
    {"name": "HEROKU_POSTGRESQL_STARTER_BLUE_URL", "connection_url": "postgres://u5huut0jc85fen:pb31b56642f476f656e5f156219bf782052be15dfe5e192114a2953058293f025@ec2-34-199-172-182.compute-1.amazonaws.com:5432/dquge67c0u7vr"},
    {"name": "HEROKU_POSTGRESQL_STARTER_COBALT_URL", "connection_url": "postgres://u2ebfjqukd7m1n:p115983ed88d2cb058fd6517e3fc699b66c288ea9ad076a93c456a658d0bf8b01@ec2-34-199-137-141.compute-1.amazonaws.com:5432/d2cua5t5e8i2me"},
    {"name": "HEROKU_POSTGRESQL_STARTER_GRAY_URL", "connection_url": "postgres://u9hjn4ggoehlup:pf8aa15eac5abd5922e21d5118a5a6487615bd5e28bd4e39d28af778d32f19055@ec2-3-228-90-88.compute-1.amazonaws.com:5432/d3cs8tbk044po"},
    {"name": "HEROKU_POSTGRESQL_STARTER_GREEN_URL", "connection_url": "postgres://u9rjq7i12lto3g:pe92f35258f103dec6556d812596b0b9eb7d93e96b1273e24aacdf8459fb5127a@ec2-52-55-208-240.compute-1.amazonaws.com:5432/d4qki4jdnshbo5"},
    {"name": "HEROKU_POSTGRESQL_STARTER_OLIVE_URL", "connection_url": "postgres://u9us305nmiv07i:peac933dd1527880b5d28beeceaf021c201cc6ca94db7bb2504ec52ce285b65ee@ec2-34-200-193-3.compute-1.amazonaws.com:5432/ddb673f9ctje4n"},
    {"name": "HEROKU_POSTGRESQL_STARTER_PINK_URL", "connection_url": "postgres://u3nik3s29642am:p72c10eb3f8b6d6053394d13919a641732090e2cc63676ca263e9d5ff7076e145@ec2-35-172-58-177.compute-1.amazonaws.com:5432/d2dgga7h1dls0v"},
    {"name": "HEROKU_POSTGRESQL_STARTER_PURPLE_URL", "connection_url": "postgres://u2qhjfbkh1qivf:p68ef67c5527ab3bcf310f16bc08cf6f4a144a3ca76741c48067bb776a090b4c4@ec2-3-223-0-251.compute-1.amazonaws.com:5432/d7og7tthacivm8"},
    {"name": "HEROKU_POSTGRESQL_STARTER_URL",  "connection_url": "postgres://ue6aed9cfh9so4:p1468cba7163f6f166ae5992afb4bb3c2933bb3abfbef9e57efff14838d01a227@ec2-34-194-101-191.compute-1.amazonaws.com:5432/d4lcrlfsj6k63h"},
    {"name": "HEROKU_POSTGRESQL_STARTER_YELLOW_URL", "connection_url": "postgres://u8r9urn67k56lt:p81b97018a8c7be03a9c2e32cbf3f814c8031dda5d98c6c792c4f087986850855@ec2-54-157-206-176.compute-1.amazonaws.com:5432/dfccehaej7imf5"}
]

sched = BlockingScheduler()

down_since = 0

@sched.scheduled_job('interval', seconds=15)
def test_connection():
    for database in DATABASES:
        name = database["name"]
        connection_url = database["connection_url"]
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S:%s")
        global down_since
        if (down_since == 0):
            try:
                conn = psycopg2.connect(connection_url, connect_timeout=7)
                print(f"Connection to {name} succesful at {current_time}")
            except:
                print(f"Connection to {name} failure at {current_time}")
                down_since = current_time
                return down_since
        else:
            try:
                conn = psycopg2.connect(connection_url, connect_timeout=7)
                print(f"Connection to {name} succesful at {current_time}")
                down_since = 0
                return down_since
            except:
                print(f"Connection to {name} down since {down_since}. Retrying")

sched.start()
