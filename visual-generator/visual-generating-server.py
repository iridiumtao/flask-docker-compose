from flask import Flask, request
import requests

from define import visual_port, visual_host, voice_server_url, is_debug_mode

app = Flask(__name__)


@app.route("/image", methods=['GET', 'POST'])
def request_image():
    """
    請求圖像

    我不太確定這是不是需要的，但我想說可能需要一個生成影片首圖的 function

    Returns:
        _type_: _description_
    """
    date = request.values.get('date')
    additional_info = request.values.get('additional_info')

    return f"This is not an image but anyway. This is the date: {date}. And this is the additional_info: {additional_info}"

@app.route("/video", methods=['GET', 'POST'])
def request_video():
    # 這些都是文章生成所需的參數
    date = request.values.get('date')
    date_interval = request.values.get('date_interval')
    topic = request.values.get('topic')
    additional_info = request.values.get('additional_info')

    # 取得生成好的語音
    voice = requests.post(voice_server_url,
                         data={'date': date, 
                               'date_interval': date_interval, 
                               'topic': topic, 
                               'additional_info': additional_info})

    # todo
    # 未確定要直接接收檔案，還是接收檔案路徑
    # 總之最後這個語音會是 .wav 檔案

    # 此外還需要基底影片 .mp4 檔案

    # 接著做某些事情，取得影片

    return f"This is not a video but anyway. from voice:\n{voice.text}"


if __name__ == "__main__":
    app.run(debug=is_debug_mode, host=visual_host, port=visual_port)