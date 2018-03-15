from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging
import time
import urllib
from bs4 import BeautifulSoup

#Indentificador de Defeitos#
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
#---#
up=Updater(TOKENDOBOT)


chatid=-271486939

#FUNÇÕES DOS COMANDOS#

def startpost(bot, update):
    import urllib
    from bs4 import BeautifulSoup

    #DADOS DO COMANDO#
    url="https://titorexpress.000webhostapp.com/"
    #----------#
    
    pagina = urllib.request.urlopen(url)
    res = BeautifulSoup(pagina.read(),"html5lib")
    body=res.body
    for titulo in body.find_all("p"):
        principal=titulo.text
    bot.send_message(chat_id=chatid, text=principal)
 
################COMANDO QUE DEVE PUXAR OS DOIS INPUTS####################### 
def echo(bot, update):
    import urllib
    from bs4 import BeautifulSoup
    infart=update.message.text
    if(infart.startswith("http")):
        url=infart
        pagina = urllib.request.urlopen(url)
        res = BeautifulSoup(pagina.read(),"html5lib")
        title=res.head
        for titulo in title.find_all("title"):
            principal=titulo.text


        url_two="https://startpost.000webhostapp.com/"
        pagina_two=urllib.request.urlopen(url_two)
        read_that=BeautifulSoup(pagina_two.read(),"html5lib")
        body=read_that.body
        for ler in body.find_all("p"):
            para=ler.text

        bot.send_message(chat_id=chatid, text=para.format(rodada=1, cartaum=principal, lnkum=infart, cartadois="Em desenvolvimento", lnkdois="Em desenvolvimento"))
################COMANDO QUE DEVE PUXAR OS DOIS INPUTS#######################             

        
   
         
def greet(bot, update):
    text="Olá {nome}, bem vindo ao whatif!"
    bot.sendMessage(chat_id=chatid, text=text.format(nome=update.message.from_user.first_name))


up.dispatcher.add_handler(CommandHandler('start', greet))
up.dispatcher.add_handler(CommandHandler('newgame', startpost))

################RETORNO PRO USUÁRIO#######################
echo_handler = MessageHandler(Filters.text, echo)
final=up.dispatcher.add_handler(echo_handler)
################RETORNO PRO USUÁRIO#######################

up.start_polling()
while True:
    pass

