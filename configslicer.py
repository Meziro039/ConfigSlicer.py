import os
from QuickLayer import quicklayer


class file:

    def __init__(self,file_cs):
        
        # 変数の設定
            # 入力
        self.file_cs = quicklayer.get(__file__, str(file_cs))
            # データ
        self.fileget = None
        self.ngword = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\"", ":", "?", "<", ">", "|", "[", "]", "="]
            # 処理
        self.tempfile = [] #fileget処理用
        self.blocklist = [] #ブロック名格納
        self.id_value = [] #idとvalueのリスト
        self.conf_dict = {} #コンフィグ辞書(二次元配列)
        self.delete = None # コメントアウト削除用
        self.cmout = "" # コメントアウト格納
        self.write_temp = [] # 書き込み処理データ保管
        self.writedata = None # 書き込みデータ

        self.while_a = 0 # カウント
        self.while_b = 0 # カウント
        self.while_c = 0 # カウント
        self.while_d = 0 # カウント
        self.while_e = 0 # カウント
        self.while_e_a = 0 # カウント
        self.while_f = 0 # カウント
        self.temp_a = None # 処理値
        self.temp_b = None # 処理値
        self.temp_c = None # 処理値
        self.temp_d = None # 処理値
            # その他
        self.output = None # 出力



        # ファイルの有無確認と作成
        if os.path.isfile(self.file_cs):
            pass
        else:
            with open(self.file_cs, mode='r', encoding='utf-8'):
                pass

        # ファイルの読み込みと処理
        with open(self.file_cs, mode='r', encoding='utf-8') as f:
            self.fileget = f.read()
            self.fileget = self.fileget.replace(" ", "")
            self.fileget = self.fileget.replace(":", "=")
            self.fileget = self.fileget.splitlines()
            
            # 空リストを削除
            while True:
                if "" in self.fileget:
                    self.fileget.remove("")
                else:
                    break

        # ファイルの中身の有無確認
            # filegetの中身を処理用に変換
            # 内容のエラー判定
            # 内容を辞書に登録
        if len(self.fileget) != 0:
            
            self.tempfile = self.fileget.copy()

            # コメントアウトを除去
            while True: # Aループ
                # コメントアウトを削除してtempfileに格納
                if "#" in self.tempfile[self.while_a]:
                    while True:
                        # #を含んでいたら削除
                        if "#" not in self.tempfile[self.while_a]:
                            break
                        else:
                            self.delete = self.tempfile[self.while_a][-1]
                            self.tempfile[self.while_a] = self.tempfile[self.while_a].rstrip(self.delete)
                else:
                    pass

                #break処理
                if self.while_a == len(self.tempfile) - 1:
                    break
                else:
                    self.while_a += 1


            # 空リストを削除
            while True:
                if "" in self.tempfile:
                    self.tempfile.remove("")
                else:
                    break


            ## エラー処理

            # ブロックは先端に存在するか
            if self.tempfile[0][0] != "[" and self.tempfile[0][-1] != "]":
                self.output = None
                print("Error: No block value." + "\n" + "Info: Blockが存在しません。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                return(self.output)
            else:
                pass

            while True: # Bループ

                # 不明な文字列が混じっていないか(hogeみたいな) []も=もない
                if "[" in self.tempfile[self.while_b] and "]" in self.tempfile[self.while_b]:
                    pass
                elif "=" in self.tempfile[self.while_b]:
                    pass
                else:
                    self.output = None
                    print("Error: Incorrect input data." + "\n" + "Info: 不正な文字列が含まれています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                    return(self.output)

                # 先端に利用できない文字が含まれているか
                if self.tempfile[self.while_b][0] == "[" and self.tempfile[self.while_b][1] in self.ngword:
                    self.output = None
                    print("Error: Incorrect block value." + "\n" + "Info: Blockの先端に利用できない文字列が含まれています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                    return(self.output)
                elif "[" not in self.tempfile[self.while_b] and self.tempfile[self.while_b][0] in self.ngword:
                    self.output = None
                    print("Error: Incorrect ID value." + "\n" + "Info: IDの先端に利用できない文字列が含まれています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                    return(self.output)
                else:
                    pass

                # Blockの先端と末尾に"["と"]"があるか/"["or"]"が1つ以上含まれていないか
                if self.tempfile[self.while_b][0] == "[" and self.tempfile[self.while_b][-1] == "]" and self.tempfile[self.while_b].count("[") == 1 and self.tempfile[self.while_b].count("]") == 1:
                    pass
                elif "[" not in self.tempfile[self.while_b] and "]" not in self.tempfile[self.while_b]:
                    pass
                else:
                    self.output = None
                    print("Error: Incorrect Block value." + "\n" + "Info: \"[\"もしくは\"]\"が不正な位置に存在します。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                    return(self.output)

                # Blockに"="が含まれていないか
                if "[" in self.tempfile[self.while_b] and "=" in self.tempfile[self.while_b]:
                    self.output = None
                    print("Error: Incorrect Block value." + "\n" + "Info: Blockに\"=\"を含んではいけません。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                    return(self.output)
                else:
                    pass

                # 設定値に"="が1つ以上含まれていないか
                if "=" in self.tempfile[self.while_b] and self.tempfile[self.while_b].count("=") != 1:
                    self.output = None
                    print("Error: Incorrect ID value." + "\n" + "Info: \"=\"が多く含まれています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                    return(self.output)
                else:
                    pass


                # Break処理
                if self.while_b == len(self.tempfile) - 1:
                    break
                else:
                    self.while_b += 1


            # 読み取り値を辞書に登録
            while True: # Cループ

                # Blockを登録
                if "[" in self.tempfile[self.while_c]:

                    self.tempfile[self.while_c] = self.tempfile[self.while_c].replace("[", "")
                    self.tempfile[self.while_c] = self.tempfile[self.while_c].replace("]", "")

                    # 同じBlockの名前がないか
                    if self.tempfile[self.while_c] in self.blocklist:
                        self.output = None
                        print("Error: Incorrect Block value." + "\n" + "Info: 同じ名前のBlockが存在しています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                        return(self.output)
                    else:
                        self.blocklist.append(self.tempfile[self.while_c])
                        self.conf_dict[self.tempfile[self.while_c]] = {}

                # IDを登録
                elif "=" in self.tempfile[self.while_c]:
                    
                    self.id_value = self.tempfile[self.while_c].split("=")

                    # ひとつのBlockに同じIDがないか
                    if self.id_value[0] in self.conf_dict[self.blocklist[-1]]:
                        self.output = None
                        print("Error: Incorrect ID value." + "\n" + "Info: ひとつのBlockに同じIDが存在しています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                        return(self.output)
                    else:
                        self.conf_dict[self.blocklist[-1]].update({self.id_value[0] : self.id_value[1]})

                # Break処理
                if self.while_c == len(self.tempfile) - 1:
                    break
                else:
                    self.while_c += 1

        else:
            pass


    
    def read(self, block_cs=None, id_cs=None):
        
        # 入力値が存在しない
        if block_cs == None or id_cs == None:
            self.output = None
            print("Error: Incorrect input data." + "\n" + "Info: 入力値がありません。")
            return(self.output)

        # 入力値の型変換
        block_cs = str(block_cs)
        id_cs = str(id_cs)

        # 入力禁止文字の処理

        # 入力値のBlock/IDが存在しない
        if block_cs not in self.conf_dict:
            self.output = None
            print("Error: Incorrect input data." + "\n" + "Info: 入力値のBlock名は存在しません。")
            return(self.output)
        elif id_cs not in self.conf_dict[block_cs]:
            self.output = None
            print("Error: Incorrect input data." + "\n" + "Info: 入力値のID名は存在しません。")
            return(self.output)

        # 出力
        self.output = self.conf_dict[block_cs][id_cs]
        return(self.output)


    
    def write(self, block_cs=None, id_cs=None, value_cs=None, opt_cs="_=_"):

        # 変数処理
        self.write_temp = self.fileget.copy()
        self.blocklist = []
        self.id_value = []

        # 入力値が存在しない
        if block_cs == None or id_cs == None or value_cs == None:
            self.output = None
            print("Error: Incorrect input data." + "\n" + "Info: 入力値がありません。")
            return(self.output)

        # 入力値の型変換
        block_cs = str(block_cs)
        id_cs = str(id_cs)
        value_cs = str(value_cs)
        opt_cs = str(opt_cs)        

        # optに仕様外の文字列(エラー)
        if opt_cs == "=" or opt_cs == "_=_" or opt_cs == ":" or opt_cs == "_:_":
            pass
        else:
            self.output = None
            print("Error: Incorrect input data." + "\n" + "Info: optの値が正しくありません。入力できる文字列は\"=\"or\"_=_\"or\":\"or\"_:_\"です。")
            return(self.output)

        # optの設定
        if opt_cs == "=":
            opt_cs = "="
        elif opt_cs == "_=_":
            opt_cs = " = "
        elif opt_cs == ":":
            opt_cs = ":"
        elif opt_cs == "_:_":
            opt_cs = " : "

        ## エラー処理

        # 入力できない文字列が含まれていないか
        if block_cs[0] in self.ngword or id_cs[0] in self.ngword:
            self.output = None
            print("Error: Incorrect input data." + "\n" + "Info: BlockまたはIDの先頭に利用できない文字列が含まれています。")
            return(self.output)

        if len(self.fileget) != 0:

            # Blockの検出
            while True: # Dループ

                # リスト切り出し
                self.temp_a = self.write_temp[self.while_d].split("#")[0]

                # ブロック判定
                if "" == self.temp_a:
                    pass
                elif "[" == self.temp_a[0] and "]" == self.temp_a[-1]:
                    self.temp_a = self.temp_a.replace("[", "")
                    self.temp_a = self.temp_a.replace("]", "")
                    self.blocklist.append(self.temp_a)

                # break処理
                if self.while_d == len(self.write_temp) - 1:
                    break
                else:
                    self.while_d += 1


            # 存在しないBlockか
            if block_cs in self.blocklist:
                # IDの値を更新/追加
                while True: # Eループ

                    # リスト切り出し
                    self.temp_a = self.write_temp[self.while_e].split("#")[0]

                    # Block/IDの判定と設定
                    if "" == self.temp_a:
                        pass
                    elif "[" == self.temp_a[0] and "]" == self.temp_a[-1]:
                        self.temp_b = self.temp_a
                        self.temp_b = self.temp_b.replace("[", "")
                        self.temp_b = self.temp_b.replace("]", "")
                        self.id_value = [""]
                    elif "=" in self.temp_a and self.temp_a.count("=") == 1:
                        self.id_value = self.temp_a.split("=")
                    else:
                        pass

                    # 入力値と適合するか
                    if block_cs == self.temp_b and id_cs == self.id_value[0]:

                        # コメントアウトがあるか
                        if "#" in self.write_temp[self.while_e]:
                            self.cmout = " " + self.write_temp[self.while_e][self.write_temp[self.while_e].find("#"):]

                        self.write_temp[self.while_e] = id_cs + "=" + value_cs + self.cmout
                        break

                    # IDが未格納
                    elif "" == self.id_value[0]:
                        pass

                    # Blockはあっているが適合していない
                    elif block_cs == self.temp_b and id_cs != self.id_value[0]:

                        self.while_e_a = self.while_e + 1
                        while True: # E_Aループ

                            # リスト切り出し
                            if self.while_e_a >= len(self.write_temp) - 1:
                                self.temp_c = "0"
                            else:
                                self.temp_c = self.write_temp[self.while_e_a].split("#")[0]

                            # 判定
                            if "=" in self.temp_c:
                                break
                            elif "" == self.temp_c:
                                self.while_e_a += 1
                            else:
                                if self.temp_c == "0":
                                    self.write_temp.append(id_cs + "=" + value_cs)
                                    break
                                else:
                                    self.write_temp.insert(self.while_e_a, id_cs + "=" + value_cs)
                                    break

                        if self.write_temp[self.while_e_a] == id_cs + "=" + value_cs:
                            break
                        elif self.write_temp[-1] == id_cs + "=" + value_cs:
                            break
                        else:
                            pass

                    else:
                        pass

                    # break処理
                    if self.while_e == len(self.write_temp) - 1:
                        break
                    else:
                        self.while_e += 1

            else:
                self.write_temp.append("[" + block_cs + "]")
                self.write_temp.append(id_cs + "=" + value_cs)
        else:
            self.write_temp.append("[" + block_cs + "]")
            self.write_temp.append(id_cs + "=" + value_cs)


        # 書き込み前処理
        while True: # Fループ

            # リスト切り出し
            self.temp_a = self.write_temp[self.while_f].split("#")[0]

            # 設定された設定値区切り文字に変換
            if "=" in self.temp_a:
                self.write_temp[self.while_f] = self.write_temp[self.while_f].replace("=", opt_cs)
            else:
                pass

            # ブロックとIDの空白を作成
            if "" == self.temp_a:
                pass
            elif "[" == self.temp_a[0] and "]" == self.temp_a[-1]:
                self.write_temp.insert(self.while_f, "")
                self.while_f += 1

            # break処理
            if self.while_f == len(self.write_temp) - 1:
                break
            else:
                self.while_f += 1

        if self.write_temp[0] == "":
            del self.write_temp[0]

        self.writedata = "\n".join(self.write_temp)

        with open(self.file_cs, mode='w', encoding='utf-8') as f:
            f.write(self.writedata)

# C/https://github.com/Meziro039