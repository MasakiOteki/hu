#Paizaで使えそうな関数一覧です

#num個分のstrを返す関数
def repeatStr(num,str):
    ret = ""
    for i in range(num):
        ret += str(str)
    return ret


#strとarray[n]を順番に比較していく。
def string_comparison(str,array,len):
    ret = False
    for i in range(len):
        if(array[i]==str):
            ret = True
            return ret        