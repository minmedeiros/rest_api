import requests, sqlite3, random, string
from flask import Flask
from flask_restful import Api, Resource, reqparse

#init api
app = Flask(__name__)
api = Api(app)

#connect to database
conn = sqlite3.connect('bots.db')
cursor = conn.cursor()

#init list of bots and messages for this run based on database snapshot
botslist=[]
cursor.execute('''SELECT * FROM botslist''')
for linha in cursor.fetchall():
            botslist.append({'id': linha[0], 'name': linha[1]})

messagelist = []
cursor.execute('''SELECT * FROM messageslist''')
for linha in cursor.fetchall():
            messagelist.append({'id': linha[0], 'conversationId': linha[1], "timestamp": linha[2], "from_": linha[3], "to_": linha[4], "text": linha[5]})

# functions definitions for no argument requests with bots
class BotsIn(Resource):
    #post user/bot to database
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("name")
        args = parser.parse_args()

        for bot in botslist:
            if (args["name"] == bot["name"]):
                return "User with name {} already exists".format(args["name"]), 400

        bot = {
            "id": args["id"],
            "name": args["name"]
        }
        botslist.append(bot)
        conn = sqlite3.connect('bots.db')  # Carregando banco de dados
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO botslist (id, name) VALUES (?, ?)""", (args["id"], args["name"]))
        conn.commit()
        return bot, 201

    # put user/bot on database
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("name")
        args = parser.parse_args()

        for bot in botslist:
            if (args["name"] == bot["name"]):
                bot["id"] = args["id"]
                return bot, 200

        bot = {
            "id": args["id"],
            "name": args["name"]
        }
        botslist.append(bot)
        conn = sqlite3.connect('bots.db')  # Carregando banco de dados
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO botslist (id, name) VALUES (?, ?)""", (args["id"], args["name"]))
        conn.commit()
        return bot, 201

# functions definitions for bot requests with arguments
class Bots(Resource):
    # returns bot data by name
    def get(self, iname):
        for bot in botslist:
            if (iname == bot["name"]):
                return bot, 200
        return "User not found", 404

    # delete bot from database, identified by name
    def delete(self, iname):
        global botslist
        botslist = [bot for bot in botslist if bot["name"] != iname]
        conn = sqlite3.connect('bots.db')  # Carregando banco de dados
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM botslist WHERE name = ?""", (iname,))
        conn.commit()
        return "{} is deleted.".format(iname), 200

# functions definitions for message requests with arguments
class Message(Resource):
    # returns message by id
    def get(self, id):
        for msg in messagelist:
            if (id == msg["id"]):
                return msg, 200
        return "Message not found", 404

#  functions definitions for no argument requests with messages
class MessageIn(Resource):
    # store message on database and give an id
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("conversationId")
        parser.add_argument("timestamp")
        parser.add_argument("from_")
        parser.add_argument("to_")
        parser.add_argument("text")
        args = parser.parse_args()

        msg = {
            "id": ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)]),
            "conversationId": args["conversationId"],
            "timestamp": args["timestamp"],
            "from_": args["from_"],
            "to_": args["to_"],
            "text": args["text"]
        }
        messagelist.append(msg)
        conn = sqlite3.connect('bots.db')  # Carregando banco de dados
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO messageslist (id, conversationId, timestamp, from_, to_, text) VALUES 
        (?, ?, ?, ?, ?, ?)""", (msg["id"], args["conversationId"], args["timestamp"], args["from_"], args["to_"], args["text"]))
        conn.commit()
        return msg, 201

    # return list of messages by conversation id
    def get(self):
        conversationId = reqparse.RequestParser().add_argument("conversationId").parse_args()["conversationId"]
        print(conversationId)
        temp = []
        for msg in messagelist:
            if (conversationId == msg["conversationId"]):
                temp.append(msg)
        if(temp):
            return temp, 200
        return "Conversation not found", 404

# call respective functions based on bots/message and yes/no input
api.add_resource(BotsIn, "/bots")
api.add_resource(Bots, "/bots/<string:iname>")
api.add_resource(Message, "/messages/<string:id>")
api.add_resource(MessageIn, "/messages")

app.run(debug=True)