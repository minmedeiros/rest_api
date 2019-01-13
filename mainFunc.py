import requests, datetime

# define class for http requests
# also rearrange data
# functions could return other info, if desired
class Manage():
    # receives id and name and post them to server
    def post_bot(self, id, name):
        bot={"id": id, "name": name}
        response = requests.post('http://127.0.0.1:5000/bots', json=bot)
        print(response.status_code)
        if response.status_code == 201:
            print("Success!")
            print(response.json())
        else:
            print(response.content)

    # receives name and prints corresponding bot (could return it)
    def get_bot(self, name):
        response = requests.get('http://127.0.0.1:5000/bots/'+name)
        print(response.status_code)
        if (response.status_code == 200):
            print(response.json())
        else:
            print(response.content)

    # receives id and name and put them on server
    def put_bot(self, id, name):
        bot = {"id": id, "name": name}
        response = requests.put('http://127.0.0.1:5000/bots', json=bot)
        print(response.status_code)
        if response.status_code == 200:
            print("Bot already exist")
            print(response.json())
        elif response.status_code == 201:
            print("Bot added")
            print(response.json())
        else:
            print(response.content)

    # receives name and asks to delete corresponding bot on database
    def delete_bot(self, name):
        response = requests.delete('http://127.0.0.1:5000/bots/'+name)
        print(response.status_code)
        if (response.status_code == 200):
            print("Bot deleted")
        print(response.content)

    # receives conversation id (could be created on server as well),
    # from and to users, and message text
    # store them on database
    def post_msg(self, cID, frm, to, text):
        msg = {"conversationId": cID,
               "timestamp": datetime.datetime.now().isoformat(),
               "from_": frm,
               "to_": to,
               "text": text}
        response = requests.post('http://127.0.0.1:5000/messages', json=msg)
        print(response.status_code)
        if response.status_code == 201:
            print("Success!")
            print(response.json())
            return response.json()["id"]
        else:
            print(response.content)
            return "0"

    # receives message id and prints corresponding message
    def get_msg(self, mID):
        response = requests.get('http://127.0.0.1:5000/messages/' + mID)
        print(response.status_code)
        if (response.status_code == 200):
            print(response.json())
        else:
            print(response.content)

    # receives conversation id and prints corresponding messages
    def get_conversation(self, cID):
        response = requests.get('http://127.0.0.1:5000/messages', params={'conversationId': cID})
        print(response.status_code)
        if (response.status_code == 200):
            print(response.json())
        else:
            print(response.content)
