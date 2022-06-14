quiz_sazae = ["サザエの旦那の名前は？","マスオ","ますお"]
quiz_katuo = ["カツオの妹の名前は？","ワカメ","わかめ"]
quiz_tarao = ["タラオはカツオから見てどんな関係？","甥","おい","甥っ子","おいっこ",]
print("問題："+quiz_sazae[0])
sazae_ans = input("答えるんだ\n")
for i in range (len(sazae_ans)):
    if sazae_ans == quiz_sazae[i+1]:
        print("正解")
        break
    else:
        print("出直してこい")

print("問題："+quiz_katuo[0])
katuo_ans = input("答えるんだ\n")
for i in range (len(katuo_ans)):
    if katuo_ans == quiz_katuo[i+1]:
        print("正解")
        break
    else:
        print("出直してこい")


print("問題："+quiz_tarao[0])
tarao_ans = input("答えるんだ\n")
for i in range (len(tarao_ans)):
    if tarao_ans == quiz_tarao[i+1]:
        print("正解")
        break
    else:
        print("出直してこい")
