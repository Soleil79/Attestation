from datetime import datetime as dt
# from time import strptime, time

def access_logger(text):
    time = dt.today()
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{};{}\n'
                    .format(time, text))
