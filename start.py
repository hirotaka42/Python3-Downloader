
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

    imput_key = is_imput()
    if imput_key[:1] == "n" or imput_key[:1] == "N":
        print("ディレクトリを開き,終了します")
        # ディレクトリを開く
        is_open_dir()

        exit()

    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['{}'.format(imput_key)])
        
    is_download_finish()


if __name__ == '__main__' :

    while 1 :
        main()

