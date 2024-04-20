from tkinter import messagebox
from tkinter import filedialog


from .sub_module.Make_df_from_list import make_df_from_list
from .Write_xlsx import write_xlsx
from .Meibo_clear import meibo_clear

from Class import default
from Class import student_data

def print_xlsx(app): 
    '''
    xlsx形式のクラブ名簿を出力
    Output club list in xlsx format.
    '''    
    ask_print = messagebox.askyesno("確認","名簿を作成していいですか?") #最終確認
    if ask_print == True:
        make_df_from_list(student_data.gakuban_list) #入力された学籍番号のリストを元にDFを作成
        write_xlsx(student_data.df) # xlsxへの書き込み
        default.ws['A3'] = '●団体名：' + student_data.club_name #クラブ名をセルに入れる
        savename = filedialog.asksaveasfilename(
                                                title = "名前を付けて保存",
                                                initialfile = "集会参加者名簿_{}_{}".format(student_data.club_name,default.yyyymmdd),
                                                initialdir = "./", #自身のディレクトリを指定
                                                defaultextension= "xlsx",
                                                filetypes = [("エクセル形式",".xlsx"),]
        ) #ダイアログを表示し、保存するファイルの絶対パスを取得
        if savename != '':
            default.wb.save(savename) # xlsxを出力
            # ボタンを初期状態に戻す
            app.Button_print_xlsx['state'] = 'disabled'
            app.Button['state'] = 'disabled'
            app.Button2['state'] = 'disabled'
            app.Button4['state'] = 'disabled'  
            # 名簿をクリアする
            meibo_clear(app)
    return "break" #ボタンが押された状態を回避する
