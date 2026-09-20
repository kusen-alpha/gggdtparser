# -*- coding:utf-8 -*-
# author: kusen
# email: 1194542196@qq.com
# date: 2023/5/16


"""
越南语
"""

ACCURATE_REGEX_LIST = [
    r"(?P<d>\d{1,2})\s*[\-\|/\.月]\s*(?P<m>\d{1,2})\s*[\-\|/\.年]\s*(?P<Y>\d{2,4})"
    # 29 tháng 3 năm 2023
]

SUB_TRANSLATE = [
    (r"hôm\s+kia", "前天"),
    (r"ngày\s+kia", "后天"),
    (r"hôm\s+qua", "昨天"),
    (r"hôm\s+nay", "今天"),
    (r"ngày\s+mai", "明天"),
    (r"bây\s+giờ|ngay\s+bây\s+giờ", "刚刚"),
    (r"tuần\s+(?:sau|tới)|tuần\s+đến", "下周"),
    (r"tuần\s+trước", "上周"),
    (r"tháng\s+(?:sau|tới)", "下个月"),
    (r"tháng\s+trước", "上个月"),
    (r"năm\s+sau", "明年"),
    (r"năm\s+ngoái|năm\s+trước", "去年"),
    (r"(?:sau)\s+(?P<num>\d+)\s*(?P<unit>giờ|小时|phút|分钟|ngày|天|tuần|周|tháng|月|năm|年)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"giờ": "小时", "小时": "小时", "phút": "分钟", "分钟": "分钟",
          "ngày": "天", "天": "天", "tuần": "周", "周": "周",
          "tháng": "月", "月": "月", "năm": "年", "年": "年"}[
             m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>giờ|小时|phút|分钟|ngày|天|tuần|周|tháng|月|năm|年)\s+(?:sau|nữa)",
     lambda m: "%s%s后" % (
         m.group("num"),
         {"giờ": "小时", "小时": "小时", "phút": "分钟", "分钟": "分钟",
          "ngày": "天", "天": "天", "tuần": "周", "周": "周",
          "tháng": "月", "月": "月", "năm": "年", "年": "年"}[
             m.group("unit")])),
    (r"(?P<num>\d+)\s*(?P<unit>giờ|小时|phút|分钟|ngày|天|tuần|周|tháng|月|năm|年)\s+trước",
     lambda m: "%s%s前" % (
         m.group("num"),
         {"giờ": "小时", "小时": "小时", "phút": "分钟", "分钟": "分钟",
          "ngày": "天", "天": "天", "tuần": "周", "周": "周",
          "tháng": "月", "月": "月", "năm": "年", "年": "年"}[
             m.group("unit")])),
    (r"phút", "分钟"),
    (r"trước", "前"),
    (r"giờ", "小时"),
    (r"tháng", "月"),
    (r"năm", "年"),
]
FUZZY_REGEX_LIST = []
