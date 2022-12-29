import unittest
from pathlib import Path
import pandas as pd
import os
from zhongwen.pandas_tools import show_html

class Test(unittest.TestCase):
    # @unittest.skip('不測試')
    def test(self):
        from zhongwen.花蓮縣法規 import 法規
        # df = cache.get('花蓮縣法規')
        # print(df)
        # for k in cache.iterkeys():
            # print(k)
        # print(cache.iterkeys())
        df = 法規()
        show_html(df, 自動格式=False)
        # df = df[['法規名稱', '公發布日']]
        # df.reset_index(inplace=True)
        # df = df.iloc[:100]

    def test_parser(self):
        from zhongwen.花蓮縣法規 import 法規分條
        c = "第一條花蓮縣政府(以下簡稱本府)為如期推動污水下水道工程，配合水資源回收中心運轉操作，經公告本縣境內污水下水道聯接使用（以下簡稱用戶接管)工程範圍內違章建築認定與拆遷作業，悉依本準則規定辦理。用戶接管工程範圍外之違章建築，依建築法、違章建築處理辦法及花蓮縣違章建築查報及拆除標準作業程序等相關規定辦理。第二條經公告用戶接管工程範圍內違章建築之拆遷作業，不適用有關補償及救濟法規之規定。第三條施工範圍內違章建築之拆除及施工作業，按下列規定辦理：一、施工單位應於施工前三十日內完成說明會之舉行與反映意見之答覆，並應於開工前十五日會同村里長逐戶張貼通告單，且與有爭議之用戶協調。二、施工範圍由用戶自行興闢留設單側七十五公分空間（雙側一點五公尺）以供作業者，依其留設空間施工，自行興闢留設用戶施工範圍之修復工程，由用戶自行負責。三、惟施工前未留設，經催告十五日後仍未留設者，依本準則查報拆除地面層防火間隔一百五十公分有危害防火逃生部分，及二樓以上有危害建物結構安全之違建，拆除後之修復工程，由用戶自行負責，其程序如附表所載。第四條工程竣工後如施工範圍再行增加違章建築，依第一條第二項規定辦理。第五條本準則自發布日實施。"
        l = 法規分條(c)
        self.assertEqual(l[0][0], 1)
        self.assertEqual(l[4][0], 5)
        self.assertEqual(l[4][1], '本準則自發布日實施。')

        c= "一、花蓮縣政府（以下簡稱本府）為統一審查農舍及農業設施申請建築執照，申請基地未臨接建築線，以其他土地通路或農路臨接道路使用，依內政部77年8月18日台內營字第622851號、內政部營建署99年7月30日營署建管字第0992914816號函意旨，訂定本原則。二、農業用地興建未達建築法第7條規定雜項工作物以外之簡易鋪面（混凝土、瀝青混凝土等類似材料）或透水性鋪面通路及農路，免依建築法規定申請建築執照。三、農舍或農業設施申請建築執照，於基地內興建通路或農路者應檢附農業用地作農業設施容許使用同意文件或經農業主管機關（或公共工程主管機關）認定為公共建設及通行需要所核發證明文件。四、農舍或農業設施申請建築執照以其他土地通路或農路臨接道路使用，除公有土地現況作為道路使用者之外，應取得該土地所有權人通行使用同意書。本府主管建築機關於核發農舍或農業設施建造執照時，除下列情形外應副知本府農業主管機關（都市計畫內土地另副知都市計畫主管機關）列管查處：（一）該通路或農路取得農業用地作農業設施容許使用同意文件。（二）該通路或農路經農業主管機關（或公共工程主管機關）認定為公共建設及通行需要所核發證明文件，且現況可供通行者。（三）該通路或農路範圍編定為交通用地。（四）該通路或農路之使用分區或土地編定為建築用地，符合建築技術規則建築設計施工編第一百六十三條基地內通路規定者。五、依本原則申請建築許可，其臨接通路或農路寬度及退讓應符合其他法令規定，倘涉及他人權益，應依私權及司法途徑調處，建築物起造人、或設計人、或監造人、或承造人，如有侵害他人財產，或肇致危險或傷害他人時，應分別依法負其責任。六、本原則奉縣長核定後公告實施。"
        l = 法規分條(c)
        self.assertEqual(l[0][0], 1)
        self.assertEqual(l[4][0], 5)
        self.assertEqual(l[5][1], '本原則奉縣長核定後公告實施。')
        c = "詳如附表所示。"
        l = 法規分條(c)
        self.assertEqual(l[0][0], 1)
        self.assertEqual(l[0][1], '詳如附表所示。')


if __name__ == '__main__':
    unittest.main()
