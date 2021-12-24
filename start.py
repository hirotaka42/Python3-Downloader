
import yt_dlp

# フォルダーを開くために必要
import subprocess
import os


def is_open_dir():
    """
    現在のディレクトリを開く
    """

    # フォルダのパスを取得
    path = os.getcwd()
    try:
        # open
        subprocess.call(["open", path])
    except FileNotFoundError:
        # Error
        print("Error---------------------------------+")
        print('ディレクトリを開く事が出来ませんでした.\n予期していない環境の可能性があります.\n')
        # Error
        print("Pathを参考にしてください.-------------+")
        print('{}'.format(path))
        print("+-------------------------------------+\n")
        
    


def is_imput() -> str:
    """
    DLするURLを入力処理する
    """
    key = ""
    print("+-------------------------------------+")
    print("URLを入力してください(終了するには'n'を入力)")
    print("+-------------------------------------+")
    key = input("> ")

    print('{}'.format(key) + " が入力されました")

    return key


def is_download_finish():
    """
    デコレーター
    DL完了したらディレクトリを開く
    """
    print("+-------------------------------------+")
    print("Done downloading! ")
    
    

def main():
    """
    メイン関数
    入力されたURLから動画を保存する
    """

    # URLの入力受付
    imput_key = is_imput()
    if imput_key[:1] == "n" or imput_key[:1] == "N":
        print("ディレクトリを開き,終了します")
        # 終了選択がされた場合、ファイルのあるディレクトリを開く
        is_open_dir()
        exit()

    # yt_dlpの設定開始
    # ℹ️ See docstring of yt_dlp.YoutubeDL for a description of the options
    
    try:
        ydl_opts = {
            'format': '22',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['{}'.format(imput_key)])
    except yt_dlp.utils.DownloadError:
        print("yt_dlp.utils.DownloadError----- \n Retry")
        ydl_opts = {
            'format': '18',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['{}'.format(imput_key)])
    
    # DL完了のプリント表示
    is_download_finish()

if __name__ == '__main__' :

    while 1 :
        main()

