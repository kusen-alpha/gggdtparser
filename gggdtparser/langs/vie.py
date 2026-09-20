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
    (r"(?i)\bthứ\s+(hai|2|ba|3|tư|4|năm|5|sáu|6|bảy|7)\s+(?:tuần\s+sau|sau|tới)\b",
     lambda m: "下%s" % {
         "hai": "周一", "2": "周一", "ba": "周二", "3": "周二",
         "tư": "周三", "4": "周三", "năm": "周四", "5": "周四",
         "sáu": "周五", "6": "周五", "bảy": "周六", "7": "周六"}[
            m.group(1).lower()]),
    (r"(?i)\bthứ\s+(hai|2|ba|3|tư|4|năm|5|sáu|6|bảy|7)\s+(?:tuần\s+trước|trước)\b",
     lambda m: "上%s" % {
         "hai": "周一", "2": "周一", "ba": "周二", "3": "周二",
         "tư": "周三", "4": "周三", "năm": "周四", "5": "周四",
         "sáu": "周五", "6": "周五", "bảy": "周六", "7": "周六"}[
            m.group(1).lower()]),
    (r"(?i)\bthứ\s+(hai|2|ba|3|tư|4|năm|5|sáu|6|bảy|7)\s+(?:này|tuần\s+này)\b",
     lambda m: "这%s" % {
         "hai": "周一", "2": "周一", "ba": "周二", "3": "周二",
         "tư": "周三", "4": "周三", "năm": "周四", "5": "周四",
         "sáu": "周五", "6": "周五", "bảy": "周六", "7": "周六"}[
            m.group(1).lower()]),
    (r"(?i)\bchủ\s+nhật\s+(?:tuần\s+sau|sau|tới)\b", "下周日"),
    (r"(?i)\bchủ\s+nhật\s+(?:tuần\s+trước|trước)\b", "上周日"),
    (r"(?i)\bchủ\s+nhật\s+(?:này|tuần\s+này)\b", "这周日"),
    (r"(?i)\bthứ\s+(?:hai|2)\b", "周一"),
    (r"(?i)\bthứ\s+(?:ba|3)\b", "周二"),
    (r"(?i)\bthứ\s+(?:tư|4)\b", "周三"),
    (r"(?i)\bthứ\s+(?:năm|5)\b", "周四"),
    (r"(?i)\bthứ\s+(?:sáu|6)\b", "周五"),
    (r"(?i)\bthứ\s+(?:bảy|7)\b", "周六"),
    (r"(?i)\bchủ\s+nhật\b", "周日"),
    (r"(?i)\bsáng\s+nay\b", "今天 08:00 am"),
    (r"(?i)\bchiều\s+nay\b", "今天 15:00 pm"),
    (r"(?i)\btối\s+nay\b", "今天 20:00 pm"),
    (r"(?i)\bđêm\s+nay\b", "今天 23:00 pm"),
    (r"(?i)\bsáng\s+mai\b", "明天 08:00 am"),
    (r"(?i)\bchiều\s+mai\b", "明天 15:00 pm"),
    (r"(?i)\btối\s+mai\b", "明天 20:00 pm"),
    (r"(?i)\btối\s+hôm\s+qua\b", "昨天 20:00 pm"),
    (r"(?i)\bbuổi\s+trưa\b", "12:00 pm"),
    (r"(?i)\bnửa\s+đêm\b", "12:00 am"),
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
