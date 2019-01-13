from mainFunc import Manage

# call functions to test them
# should be connected to an interface later
teste = Manage()
teste.post_bot("18632", "Yasmin")
teste.get_bot("Yasmin")
teste.put_bot("932362", "Jason")
teste.delete_bot("Jason")
msgId = teste.post_msg("55837", "Yasmin", "William", "oiboatarde")
teste.get_msg(msgId)
teste.get_conversation("55837")