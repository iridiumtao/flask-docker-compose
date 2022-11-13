from flask import Flask, request
import requests
from datetime import datetime
from pathlib import Path
from define import news_host, news_port, is_debug_mode

app = Flask(__name__)

@app.route('/', methods=['POST'])
def request_news():
    date = request.values.get('date')
    if date is None:
        date = datetime.now()
    date_interval = request.values.get('date_interval')

    if date_interval is None:
        date_interval = 7

    topic = request.values.get('topic')

    if topic == "":
        topic = None
    
    additional_info = request.values.get('additional_info')

    uuid = request.values.get('uuid')

    # todo: do something to actually generate the news
    transcript = "Okay, so obviously this is the news that you are requiring for. \n敗部復活的蘇納克，會是團結保守黨的新領袖...還是另一顆生菜？」英國首相在特拉斯的閃辭之後，24日確定由前財政大臣蘇納克（Rishi Sunak）接任英國保守黨黨魁暨英國首相。現年42歲的蘇納克將成為英國首位亞裔首相，同時也是英國近200多年來最年輕的首相。但是將於25日接受國王查爾斯三世任命的蘇納克，即將執掌的是無比混亂的局面：全球局勢導致的經濟衰退、前任首相特拉斯政策導致的英國金融動盪、民眾對保守黨的信任盡失，甚至黨內也對他懷抱不滿。與此同時，蘇納克的「富有多金」和稅務問題，卻也成了公眾批評的輿論風暴。"

    Path(f"./outputs/{uuid}").mkdir(parents=True, exist_ok=True)
    f = open("./outputs/uuid/transcript.txt", "w")
    f.write(transcript+"\n")
    f.close()


    return {"uuid": uuid, "data": transcript}

    # return f"Okay, so obviously this is the news that you are requiring for. \n敗部復活的蘇納克，會是團結保守黨的新領袖...還是另一顆生菜？」英國首相在特拉斯的閃辭之後，24日確定由前財政大臣蘇納克（Rishi Sunak）接任英國保守黨黨魁暨英國首相。現年42歲的蘇納克將成為英國首位亞裔首相，同時也是英國近200多年來最年輕的首相。但是將於25日接受國王查爾斯三世任命的蘇納克，即將執掌的是無比混亂的局面：全球局勢導致的經濟衰退、前任首相特拉斯政策導致的英國金融動盪、民眾對保守黨的信任盡失，甚至黨內也對他懷抱不滿。與此同時，蘇納克的「富有多金」和稅務問題，卻也成了公眾批評的輿論風暴。\nDate: {date}\ndate_interval: {date_interval}\ntopic: {topic}\nadditional_info: {additional_info}"

@app.route('/topic', methods=['POST'])
def request_topic():
    date = request.values.get('date')
    if date is None:
        date = datetime.now()
    date_interval = request.values.get('date_interval')

    if date_interval is None:
        date_interval = 7

    topic = request.values.get('topic')
    if topic is not None:
        return topic
    
    if topic is None:
        # todo get topic
        return "popular_topic_here"

if __name__ == "__main__":
    app.run(debug=is_debug_mode, host=news_host, port=news_port)