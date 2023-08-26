from tg_token import my_token
bot_token = my_token
my_id = 669525450

import telebot

def send_message_to_tg_user(user_id: int, text: str):
    bot = telebot.TeleBot(bot_token)
    bot.send_message(user_id, text)



def send_learning_results(name='Model', log = [], where = 'tg'):

    message = '{} was trained\n'.format(name)    
    
    for log_record in log:
        message += (log_record )

    if where == 'tg':
        try:
            send_message_to_tg_user(my_id, message)
        except:
            raise RuntimeError('cant send messege in telegram. May be you didnt start the bot. Use link " t.me/model_notifier_bot " and press "start"')
    else:
        raise NotImplementedError('You destination "{}" for sending not supporting'.format(where)) 

'''class TgReporter:
    def __init__(self):
        pass
    def __call__(self):
        print('call')
    def notify(self, name='Model', log = []):
        message = '{} was trained\n'.format(name)
        
        for log_record in log:
            message += log_record

        send_message_to_tg_user(my_id, message)   '''

send_message_to_tg_user(my_id, 'test')
    