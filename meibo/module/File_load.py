import tkinter
from tkinter import messagebox
import pandas as pd

from Class import student_data
from Class import default

def file_load(app):
    '''
    基本となる名簿の読み込み
    loading the basic list
    '''
    #ファイル選択ダイアログの表示
    file_path = tkinter.filedialog.askopenfilename()

    xlsx_check = file_path.split(".")
    xlsx_check = xlsx_check[-1]
    if (len(file_path) != 0) and (xlsx_check=="xlsx"): #ファイルが選択された場合
        student_data.df_meibo = pd.read_excel(file_path,
                                usecols=[4,5,6,8],
                                skiprows=[0],
                                names=default.Columns,
                                engine='openpyxl',)
        student_data.df_meibo = student_data.df_meibo.dropna(subset=["学籍番号"],axis=0) #データがない行を削除
        if len(student_data.df_meibo["学籍番号"] != 0): #名簿に記載されている人数が0人でない場合
            return_bool = messagebox.askyesno("確認",
                                            "この名簿には、{}人が登録されています。これを元に名簿を作成しますか？".format(len(student_data.df_meibo["学籍番号"])))
            if return_bool == False: #名簿を使わない場合
                student_data.df_meibo = '' #df_meiboを初期化する
    else:
        messagebox.showinfo("確認","適切な名簿が選択されませんでした。")
        student_data.df_meibo = '' #df_meiboを初期化する
    return "break" #ボタンが押された状態を回避