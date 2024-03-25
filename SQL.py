import sqlite3 as sq


class Data_base():
    def __init__(self, file):
        self.con = sq.connect(file)
        self.cur = self.con.cursor()
        self.create_table("score")

    def create_table(self, table_name):
        que = f"""CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score_points INTEGER
        )
        """
        self.cur.execute(que)
        self.con.commit()

    def get(self, que="SELECT * FROM score ORDER BY score_points DESC"):
        return self.cur.execute(que).fetchall()


    def insert(self, name, score):
        que_insert = f"""
        INSERT INTO score (name,score_points)
        VALUES ('{name}',{score})
        """
        self.cur.execute(que_insert)
        self.con.commit()
    def update(self,name,score):
        que = f"""update score SET score_points = {score} WHERE name = '{name}'"""
        self.cur.execute(que)
        self.con.commit()
    def __del__(self):
        self.con.close()


data_base = Data_base("game.sqlite")
# data_base.insert("best_plaer555", 10)
# data_base.insert('qweerty', 4)
# data_base.insert("testdsv12345", 15)

data = data_base.get()
# data = sorted(data, key=lambda x: -x[2])

for line in data:
    print(line)

data_base.update("best_plaer555",123)
for line in data_base.get():
    print(line)