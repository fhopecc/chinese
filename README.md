# 給懂中文的程式設計師

運用中文文字處理程式庫的程式設計師自然懂中文，
所以本程式庫設計哲學就是函數以中文命名且能簡明表達功能，
又以簡體名稱表示處理簡體中文，繁體名稱表示處理繁體中文，
如下例： 

    from zhongwen.number import 中文數字, 中文数字
    中文數字(10600)
    >>> '一萬零六百'
    中文数字(10600)
    >>> '一万零六百'
