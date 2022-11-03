from flask import Flask, render_template, request
import time
import requests
from define import news_server_url, voice_server_url, visual_server_url, virtual_to_news_host, virtual_to_news_port, is_debug_mode

app = Flask(__name__)

server_compute_url = "http://visual-generating-server:25502"

TEXT = """
敗部復活的蘇納克，會是團結保守黨的新領袖...還是另一顆生菜？」英國首相在特拉斯的閃辭之後，24日確定由前財政大臣蘇納克（Rishi Sunak）接任英國保守黨黨魁暨英國首相。現年42歲的蘇納克將成為英國首位亞裔首相，同時也是英國近200多年來最年輕的首相。但是將於25日接受國王查爾斯三世任命的蘇納克，即將執掌的是無比混亂的局面：全球局勢導致的經濟衰退、前任首相特拉斯政策導致的英國金融動盪、民眾對保守黨的信任盡失，甚至黨內也對他懷抱不滿。與此同時，蘇納克的「富有多金」和稅務問題，卻也成了公眾批評的輿論風暴。
"""


@app.route('/')
def home():
    """
    首頁？

    但其實這隻程式是API的頭，如果要有網頁的話，應該要寫在別的地方

    """
    return 'Flask Dockerized by server A'

@app.route('/news', methods=['POST'])
def news():
    """
    請求新聞文稿

    以下 parameters 意指POST請求的輸入參數

    Parameters:
    ----------
    :param date: 文章搜尋日期，須符合ISO 8601

    :return: 新聞文稿
    :rtype: str
    """
    date = request.values.get('date')
    date_interval = request.values.get('date_interval')
    topic = request.values.get('topic')
    additional_info = request.values.get('additional_info')

    news = requests.post(url=news_server_url,
                         data={'date': date, 
                               'date_interval': date_interval, 
                               'topic': topic, 
                               'additional_info': additional_info})
    return news.text

@app.route('/topic', methods=['POST'])
def topic():
    """
    請求新聞主題

    以下 parameters 意指POST請求的輸入參數

    Parameters:
    ----------
    :param date: 文章搜尋日期，須符合ISO 8601

    :return: 新聞文稿
    :rtype: str
    """
    date = request.values.get('date')
    date_interval = request.values.get('date_interval')
    topic = request.values.get('topic')
    additional_info = request.values.get('additional_info')

    news = requests.post(url=news_server_url+"topic",
                         data={'date': date, 
                               'date_interval': date_interval, 
                               'topic': topic, 
                               'additional_info': additional_info})
    return news.text

@app.route("/image", methods=['POST'])
def image():
    date = request.values.get('date')
    date_interval = request.values.get('date_interval')
    topic = request.values.get('topic')
    additional_info = request.values.get('additional_info')

    x = requests.post(url=visual_server_url+"image",
                      data={'date': date, 
                            'date_interval': date_interval, 
                            'topic': topic, 
                            'additional_info': additional_info})
    return x.text


@app.route("/video", methods=['POST'])
def video():
    date = request.values.get('date')
    date_interval = request.values.get('date_interval')
    topic = request.values.get('topic')
    additional_info = request.values.get('additional_info')

    x = requests.post(url=visual_server_url+"video",
                      data={'date': date, 
                            'date_interval': date_interval, 
                            'topic': topic, 
                            'additional_info': additional_info})
    return x.text

@app.route("/voice", methods=['POST'])
def voice():
    date = request.values.get('date')
    date_interval = request.values.get('date_interval')
    topic = request.values.get('topic')
    additional_info = request.values.get('additional_info')

    x = requests.post(url=voice_server_url,
                      data={'date': date, 
                            'date_interval': date_interval, 
                            'topic': topic, 
                            'additional_info': additional_info})
    return x.text



@app.route('/news-long')
def news_long():
    time.sleep(20)
    return render_template("news.html")


if __name__ == "__main__":
    print("version: 0.0.10")
    app.run(debug=is_debug_mode, host=virtual_to_news_host, port=virtual_to_news_port)
