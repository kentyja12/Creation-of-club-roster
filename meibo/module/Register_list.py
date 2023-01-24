from tkinter import messagebox

from Class import student_data

def register_list(app): 
    '''
    登録予定の名簿のリストを出力する
    Output a list of rosters to be registered.
    '''
    #df_joined = 読み込んだ名簿から登録されたもの+インスタント名簿から登録されたもの
    df_joined = list(set(list(student_data.df["学籍番号"])+student_data.gakuban_list)) 
    df_len = len(df_joined) #合計人数
    output_register_list = "登録人数：{}人".format(df_len) #ダイアログに表示するメッセージ
    output_register_list = output_register_list+"\n"+"\n".join(df_joined) 
    messagebox.showinfo("確認",output_register_list) #ダイアログの表示

    return "break" #ボタンが押された状態を回避する