from flask import Flask, render_template, request
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import os


my_bot = ChatBot(
    'Bangla ChatBot',
    filters=["chatterbot.filters.RepetitiveResponseFilter"]
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    try:
        return str(my_bot.get_response(userText))
    except Exception:
        return str("দুঃখিত! প্রশ্নটি আরেকবার করুন")

@app.route("/train")
def training():
    trainer = ChatterBotCorpusTrainer(my_bot)
    trainer.train(
        "./data/"
    )
    return " ট্রেনিং সম্পূর্ণ হয়েছে "







if __name__ == '__main__':
    app.run(debug=False, host='192.168.0.117', port=3000)