from yt_dlp import YoutubeDL

print("Downloading...")

# オプション設定
ydl_opts = {
    'format': 'bestaudio/best',  # 最高品質の音声フォーマット
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',  # FFmpegを使って形式を変換
        'preferedformat': 'mp4'  # 出力形式をmp4に設定
    }],
    'outtmpl': '%(title)s.%(ext)s',  # 出力ファイル名のテンプレート
}

# ダウンロードと変換
with YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/Z6une9Dt1V0?si=eFpJkflA_SB2NTVt'])
