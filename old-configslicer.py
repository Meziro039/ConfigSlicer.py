import os
from QuickLayer import quicklayer

class file:

    '''
    # 変数
        # 入力
    self.file_cs = str 設定ファイル位置
        # 処理
    self.fileget = list 読み込み設定値リスト
    self.id_value = list 辞書格納用
    self.block_list = list ブロックの値を格納
    self.conf_dict = dict ブロックとコンフィグの値を格納
    self.ngword = list 入力不可文字の処理
        # その他
    fa = str ファイル読み込み
    fb = str ファイル読み込み
    while_a = int カウント
    while_b = int カウント
        #出力
    output = srt 出力値
    '''

    def __init__(self, file_cs):

        # 変数の処理
            # ファイルの扱い
        self.file_cs = quicklayer.get(__file__, file_cs)
            # 処理
        self.fileget = None
        self.id_value = []
        self.block_list = []
        self.conf_list = [] # 後で消す
        self.conf_dict = {}
        self.ngword = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "\"", ":", "?", "<", ">", "|"]
            # その他
        self.while_a = 0
        self.while_b = 0
            #出力
        output = None

        # ファイルの存在確認と作成
        if os.path.isfile(self.file_cs):
            pass
        else:
            with open(self.file_cs, 'w'):
                pass

        # ファイルの読み込み
        with open(self.file_cs, "r", encoding="utf-8") as fa:
            self.fileget = fa.read()
            self.fileget = self.fileget.replace(" ","")
            self.fileget = self.fileget.splitlines()

        # ファイルは空か
        if len(self.fileget) == 0 or "" in self.fileget:
            pass
        else:
            # リストに合体変換
            while True:

                # 空白行とコメントアウトの判定
                if self.fileget[self.while_a] == "" or self.fileget[self.while_a].find("#") == 0:
                    pass
                else:
                    # Blockを辞書に格納
                    if self.fileget[self.while_a].find("[") == 0 and self.fileget[self.while_a].find("]") == self.fileget[self.while_a].count("") - 2:

                        # []を外す
                        self.fileget[self.while_a] = self.fileget[self.while_a].replace("[","")
                        self.fileget[self.while_a] = self.fileget[self.while_a].replace("]","")

                        # 先頭が利用不可文字か判定
                        if self.fileget[self.while_a][0] in self.ngword:
                            output = None
                            print("Error: Incorrect input data.\nInfo: Blockの先頭に利用できない文字が含まれています。")
                            return(output)

                        # 値を設定
                        else:
                            self.block_list.append(self.fileget[self.while_a])
                            self.conf_dict[self.fileget[self.while_a]] = {}

                    # "["or"]"が先頭と末尾にない場合の処理
                    elif "[" in self.fileget[self.while_a] or "]" in self.fileget[self.while_a]:
                        output = None
                        print("Error: Incorrect input data.\nInfo: \"[\"または\"]\"が不正な位置に存在しています。")
                        return(output)

                    else:
                        # ブロックがあるか判定
                        if len(self.block_list) == 0:
                            output = None
                            print("Error: Incorrect input data.\nInfo: ブロックが存在しません。")
                            return(output)

                        # 先頭が利用不可文字か判定
                        if self.fileget[self.while_a][0] in self.ngword:
                            output = None
                            print("Error: Incorrect input data.\nInfo: IDの先頭に利用できない文字が含まれています。")
                            return(output)
                        
                        # IDとValueを辞書に格納
                        else:
                            self.fileget[self.while_a] = self.fileget[self.while_a].replace(":", "=")

                            # 不適切な設定値の処理と値を分割
                            if "=" not in self.fileget[self.while_a]:
                                output = None
                                print("Error: Incorrect input data.\nInfo: 設定ファイル(ID or Value)の値が正しくありません。")
                                return(output)
                            else:
                                self.id_value = self.fileget[self.while_a].split("=")

                                # イコールが複数あった場合の処理
                                if len(self.id_value) > 2:
                                    output = None
                                    print("Error: Incorrect input data.\nInfo: 設定値に\"=\"が含まれています。")
                                    return(output)

                                # 同じidがないか
                                if self.id_value[0] in self.conf_dict[self.block_list[-1]]:
                                    output = None
                                    print("Error: Incorrect input data.\nInfo: Block内に同じIDが存在します。")
                                    return(output)

                                # 値を設定
                                self.conf_dict[self.block_list[-1]] = {self.id_value[0] : self.id_value[1]}
                
                # break判定
                if self.while_a == len(self.fileget) - 1:
                    break
                else:
                    self.while_a += 1

        # 同じBlockの名前がないか
        if len(self.block_list) != len(set(self.block_list)):
            output = None
            print("Error: Incorrect input data.\nInfo: Blockに重複した文字列があります。")
            return(output)

    def read(self, block_cs=None, id_cs=None):
        
        # 値がない場合のエラー
        if block_cs == None or id_cs == None:
            output = None
            print("Error: Incorrect input data.\nInfo: 必要な入力がありません。(({Block}, {ID})である必要があります。)")
            return(output)

        # 入力値のBlock/IDが存在しない
        if block_cs not in self.conf_dict:
            output = None
            print("Error: Incorrect input data.\nInfo: 入力されたBlockは存在しません。")
            return(output)
        elif id_cs not in self.conf_dict[block_cs]:
            output = None
            print("Error: Incorrect input data.\nInfo: 入力されたIDは存在しません。")
            return(output)

        output = self.conf_dict#[block_cs][id_cs]
        return(output)

    def write(self, block_cs=None, id_cs=None, value_cs=None, opt="_=_"):
        
        # 値がない場合のエラー
        if block_cs == None or id_cs == None:
            output = None
            print("Error: Incorrect input data.\nInfo: 必要な入力がありません。(({Block}, {ID}, {Value(任意)})である必要があります。)")
            return(output)

        # Valueがない場合の処理
        if value_cs == None:
            value_cs = ""

        # Blockの判定(ない場合は作成する)
        if block_cs in self.conf_dict:
            pass
        else:
            self.conf_dict[block_cs] = {}
            print(self.conf_dict)

        self.conf_dict[block_cs] = {id_cs : value_cs}

        print(self.conf_dict)

        # ファイル読み込みと処理
        with open(self.file_cs, "r", encoding="utf-8") as fb:
            self.fileget = fb.read()
            self.fileget = self.fileget.replace(" ","")
            self.fileget = self.fileget.replace(":","=")
            self.fileget = self.fileget.splitlines()

        # 空白リストの削除
        while True:
            # 空白を削除
            if "" in self.fileget:
                self.fileget.remove("")
            else:
                break

        print(self.fileget)

# 確実に具チャットしたコードになってるから整理したい