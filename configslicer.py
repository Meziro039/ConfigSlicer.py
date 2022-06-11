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
        self.file_write = [] # 書き込みデータ保管

        self.while_a = 0 # カウント
        self.while_b = 0 # カウント
        self.while_c = 0 # カウント
        self.while_d = 0 # カウント
        self.while_d_a = 0 # カウント
            # その他
        self.output = None # 出力


        # ショートカット
        self.ls = os.linesep


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


            # エラー処理

            # ブロックは先端に存在するか
            if self.tempfile[0][0] != "[" and self.tempfile[0][-1] != "]":
                self.output = None
                print("Error: No block value." + self.ls + "Info: Blockが存在しません。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
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
                    print("Error: Incorrect input data." + self.ls + "Info: 不正な文字列が含まれています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                    return(self.output)

                # 先端に利用できない文字が含まれているか
                if self.tempfile[self.while_b][0] == "[" and self.tempfile[self.while_b][1] in self.ngword:
                    self.output = None
                    print("Error: Incorrect block value." + self.ls + "Info: Blockの先端に利用できない文字列が含まれています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                    return(self.output)
                elif "[" not in self.tempfile[self.while_b] and self.tempfile[self.while_b][0] in self.ngword:
                    self.output = None
                    print("Error: Incorrect ID value." + self.ls + "Info: IDの先端に利用できない文字列が含まれています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
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
                    print("Error: Incorrect Block value." + self.ls + "Info: \"[\"もしくは\"]\"が不正な位置に存在します。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                    return(self.output)

                # Blockに"="が含まれていないか
                if "[" in self.tempfile[self.while_b] and "=" in self.tempfile[self.while_b]:
                    self.output = None
                    print("Error: Incorrect Block value." + self.ls + "Info: Blockに\"=\"を含んではいけません。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
                    return(self.output)
                else:
                    pass

                # 設定値に"="が1つ以上含まれていないか
                if "=" in self.tempfile[self.while_b] and self.tempfile[self.while_b].count("=") != 1:
                    self.output = None
                    print("Error: Incorrect ID value." + self.ls + "Info: \"=\"が多く含まれています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
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
                        print("Error: Incorrect Block value." + self.ls + "Info: 同じ名前のBlockが存在しています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
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
                        print("Error: Incorrect ID value." + self.ls + "Info: ひとつのBlockに同じIDが存在しています。" + "(文字列:" + self.tempfile[self.while_b] + "/" + str(self.while_b + 1) + "列目付近)")
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
            print("Error: Incorrect input data." + self.ls + "Info: 入力値がありません。")
            return(self.output)

        # 入力値の型変換
        block_cs = str(block_cs)
        id_cs = str(id_cs)

        # 入力禁止文字の処理

        # 入力値のBlock/IDが存在しない
        if block_cs not in self.conf_dict:
            self.output = None
            print("Error: Incorrect input data." + self.ls + "Info: 入力値のBlock名は存在しません。")
            return(self.output)
        elif id_cs not in self.conf_dict[block_cs]:
            self.output = None
            print("Error: Incorrect input data." + self.ls + "Info: 入力値のID名は存在しません。")
            return(self.output)

        # 出力
        self.output = self.conf_dict[block_cs][id_cs]
        return(self.output)
        
'''

    def write(self, block_cs=None, id_cs=None, value_cs=None, opt_cs="_=_"):

        # 変数の初期化
        self.blocklist = []
        self.file_write = self.fileget.copy()

        # 入力値が存在しない
        if block_cs == None or id_cs == None or value_cs == None:
            self.output = None
            print("Error: Incorrect input data." + self.ls + "Info: 入力値がありません。")
            return(self.output)

        # 入力値の型変換
        block_cs = str(block_cs)
        id_cs = str(id_cs)
        value_cs = str(value_cs)
        opt_cs = str(opt_cs)

        # 入力禁止文字の処理

        # optに仕様外の文字列(エラー)
        if opt_cs == "=" or opt_cs == "_=_" or opt_cs == ":" or opt_cs == "_:_":
            pass
        else:
            self.output = None
            print("Error: Incorrect input data." + self.ls + "Info: optの値が正しくありません。入力できる文字列は\"=\"or\"_=_\"or\":\"or\"_:_\"です。")
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

        self.file_writes = ""

        # データの確認と変更
        while True:
            # Block適合
            if "[" == self.file_write[self.while_d][0]:
                self.file_writes = self.file_write[self.while_d].replace("[", "") # 仮処置
                self.file_writes = self.file_write[self.while_d].replace("]", "")
                self.blocklist.append(self.file_writes)

            # ID適合
            if block_cs == self.blocklist[-1] and id_cs == self.file_write[self.while_d].split("=")[0]:

                # コメントアウト処理
                if "#" in self.file_write[self.while_d]:
                    self.cmout = " " + self.file_write[self.while_d][self.file_write[self.while_d].find("#"):]
                else:
                    self.cmout = ""

                self.file_write[self.while_d] = id_cs + opt_cs + value_cs + self.cmout + self.cmout
                break

            # IDがない(新規ID)
            elif block_cs == self.blocklist[-1]:

                # コメントアウトを除いた次の行がブロックか/設定値の新規追加
                self.while_d_a = self.while_d
                while True:
                    if "[" != self.file_write[self.while_d_a + 1][0] and "=" in self.file_write[self.while_d_a + 1]:
                        break
                    elif "[" == self.file_write[self.while_d_a + 1][0]: # D_Aループ
                        self.file_write.insert(self.while_d + 1, block_cs + opt_cs + id_cs)
                    elif "#" == self.file_write[self.while_d_a + 1][0]:
                        self.while_d_a += 1
                
                if self.file_write[self.while_d + 1] == block_cs + opt_cs + id_cs:
                    break
                else:
                    pass

            if self.while_d == len(self.file_write) - 1:
                break
            else:
                self.while_d += 1

        # 新規ブロックの作成
        if self.blocklist != block_cs:
            self.file_write.append("[" + block_cs + "]")
            self.file_write.append(id_cs + opt_cs + value_cs)

        self.file_write = self.ls.join(self.file_write)

        print(self.file_write)

        with open(self.file_cs, mode='w', encoding='utf-8') as f:
            f.write(self.file_write)

'''
        

'''
            
        # 書き込みデータ作成
        while True: # Dループ
            
            # コメントアウトの摘出と削除
            if "#" in self.fileget[self.while_d]:
                # コメントアウトを登録
                self.cmout = self.fileget[self.while_d][self.fileget[self.while_d].find("#"):]

                # コメントアウトを削除
                while True:
                    print(self.fileget)
                    if "#" not in self.fileget[self.while_d]:
                        break
                    else:
                        self.delete = self.fileget[self.while_d][-1]
                        self.fileget[self.while_d] = self.fileget[self.while_d].rstrip(self.delete)
            else:
                pass

            # 空リストを削除
            while True:
                if "" in self.fileget:
                    self.fileget.remove("")
                    self.while_d -= 1
                else:
                    break

            # Block/ID/コメントアウトの判定と書き込み用リストに登録
            if "[" == self.fileget[self.while_d][0]:
                self.fileget[self.while_d].replace("[", "")
                self.fileget[self.while_d].replace("]", "")
                if self.fileget[self.while_d] == self.conf_dict:
                    self.blocklist.append(self.fileget[self.while_d])
                    self.file_write.append(self.fileget[self.while_d])
            elif "=" == self.fileget[self.while_d]:
                pass
            elif self.cmout != "":
                pass    

        # Break処理
            if self.while_d == len(self.fileget) - 1:
                break
            else:
                self.while_d += 1
                

        print(self.fileget)

# C/https://github.com/Meziro039

            # Block/IDの先端に利用できない文字が含まれているか。
            while True:
                if self.tempfile[self.while_b][0] == "[" and self.tempfile[self.while_b][1] in self.ngword:
                    self.output = None
                    print("Error: Incorrect block value." + self.ls + "Info: Blockの先端に利用できない文字が含まれています。")
                    return(self.output)
                else:
                    pass
                
                if self.tempfile[self.while_b][0] != "[" and self.tempfile[self.while_b][0] in self.ngword:
                    self.output = None
                    print("Error: Incorrect ID value." + self.ls + "Info: IDの先端に利用できない文字が含まれています。")
                    return(self.output)
                else:
                    pass

                # break判定
                if self.while_b == len(self.tempfile) - 1:
                    break
                else:
                    self.while_b += 1
            

            # Blockの先端と末尾に"["と"]"があるか(不正な位置にないか)
            while True:
                if self.tempfile[self.while_c][0] == "[" and self.tempfile[self.while_c][-1] == "]" and self.tempfile[self.while_c].count("[") == 1 and self.tempfile[self.while_c].count("]") == 1:
                    pass
                elif "[" in self.tempfile[self.while_c] or "]" in self.tempfile[self.while_c]:
                    self.output = None
                    print("Error: Incorrect block value." + self.ls + "Info: Block記号(\"[\" or \"]\")の位置が不正または多く含まれています。")
                    return(self.output)
                else:
                    pass

                # break判定
                if self.while_c == len(self.tempfile) - 1:
                    break
                else:
                    self.while_c += 1

            # "="が1つ以上含まれていないか/ブロック,コメントアウト,設定値以外の文字列が混じっていないか
            while True:
                if self.tempfile[self.while_d].count("=") > 1:
                    self.output = None
                    print("Error: Incorrect delimiter value." + self.ls + "Info: 設定値の区切り文字が多く含まれています。")
                    return(self.output)
                else:
                    pass

                # break判定
                if self.while_d == len(self.tempfile) - 1:
                    break
                else:
                    self.while_d += 1
            # 

        else:
            pass

        print(self.tempfile)

        

            # 誤ったデータのエラー処理
            while True:

            # 内容を辞書に登録
            while True:

        else:
            pass

        print(self.fileget)

        

'''

# 入力のBlock/IDが存在しない