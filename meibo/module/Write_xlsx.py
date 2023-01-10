
from Class import default
from Class import student_data

def write_xlsx(df):
    '''
    原本に名簿の書き込み、そして出力する。
    Write the list on the original(genpon) and then print it.

    paramaters
        df : pd.DataFrame
            出力予定の名簿
    '''
    cnt = df.shape #(人数,Columns数)を取得
    cnt = cnt[0] #人数を取得
    for i in range(cnt): #wsに書き込み
        for j in range(4):
            index = str(chr(j+66)+str(i+6))
            default.ws[index] = df.at[i,default.Columns[j]]