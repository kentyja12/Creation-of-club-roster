import tkinter
from tkinter import messagebox
import pandas as pd

from Class import tmp
from Class import student_data
from Class import default

def instant_meibo_register(app): #インスタント名簿登録
    '''
    インスタント学生情報を出力予定の名簿に追加する。その前にインスタント名簿情報を修正する。
    Add the instant student information to the list to be Printed. 
    Before that, fix the instant student information.
    '''
    #学籍番号の数が集会名簿の上限を超えてるかチェック
    if student_data.count >= default.limit_count:
        messagebox.showerror("エラー","名簿に登録できる人数の上限に達しました。\n一度出力し、新規名簿を作成してください。")
    else:
        #生データ代入
        instant_gakuban = tmp.EditBox_instant1_tmp.upper() #学籍番号
        instant_name = tmp.EditBox_instant2_tmp #名前
        instant_phonenum = tmp.EditBox_instant3_tmp #電話番号
        #Check
        if " " in list(instant_name): #名前：性と名の間を修正する。
            instant_name = instant_name.replace(" ","　")
        if " " in list(instant_phonenum): #電話番号：3桁、4桁、4桁の形で処理する。
            instant_phonenum = instant_phonenum.replace(" ","")
        elif "　" in list(instant_phonenum):
            instant_phonenum = instant_phonenum.replace("　","")
        instant_phonenum = list(instant_phonenum)
        for index in [3,8]:
            if instant_phonenum[index] != "-": #番号の間にハイフンを入れる。
                instant_phonenum.insert(index,'-')
        instant_phonenum_surgeried = "".join([str(_) for _ in instant_phonenum])
        if (instant_gakuban in student_data.df_meibo["学籍番号"]) or (student_data.df["学籍番号"].str.contains(instant_gakuban).any()) or (instant_gakuban in student_data.gakuban_list): #読み込んだ名簿に同じ学籍番号がないかどうかチェック
            messagebox.showinfo("確認","既に部員名簿、登録予定の名簿に存在します。\n重複を回避してください。")
        surgeried_info = messagebox.askyesno("確認","学籍番号：{}\n名前：{}\n電話番号：{}".format(instant_gakuban,instant_name,instant_phonenum_surgeried))
        app.EditBox_instant1.delete(0,tkinter.END) #入力欄に記載された文字を消す。
        app.EditBox_instant2.delete(0,tkinter.END)
        app.EditBox_instant3.delete(0,tkinter.END)
        if surgeried_info == True: #登録をする場合
            df_tmp = pd.DataFrame({"学籍番号":[instant_gakuban],"役職":[" "],"氏名":[instant_name],"電話番号":[instant_phonenum_surgeried]})
            student_data.df = student_data.df.append(df_tmp)
            messagebox.showinfo("確認","登録しました")
            student_data.count = student_data.count +1
            if len(student_data.df['学籍番号']) == 1:
                app.Button3['state'] = 'normal' #名簿クリアボタンを有効
    return "break" #ボタンが押された状態を回避