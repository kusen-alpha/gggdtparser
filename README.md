# gggdtparser

通用时间解析器(General General General DateTime Parser)
，是基于Python编写的字符串时间抽取解析工具,经过了众多测试用例进行测试，具有通用、高效、准确的解析能力。

## 项目背景

1. 在日常开发中，特别是爬虫采集时，来自各种语言、各种格式、语义化话的字符串时间，对其解析非常复杂繁琐。
2. 通用的字符串解析需要考虑的情况很多，既要尽可能多地满足各类字符串时间格式，还需对解析出的结果的准确有很高要求。
3. Python中各类解析库，在解析前的要求很高，只能解析无噪声的字符串时间，极为不方便。

## 项目原理

1. 采用正则的方式完成对时间的抽取，进一步对抽取到的时间进行解析，即抽取和解析一体，用户给与的时间文本可以有很多非时间内容，使得解析更加便捷。
2. 对语义话时间进行计算，对其他语言进行支持。
3. 使用正则规则，后续增加特殊时间格式较为方便。

## 项目特色

1. 模糊抽取解析
2. 解析速度快
3. 支持自定义解析规则

## 使用方法

### 安装

    pip install gggdtparser

### 使用

    import gggdtparser
    parse_dt = gggdtparser.parse("发布：2022/02/02 02:02:02，来源：xxx网")
    print(parse_dt)  # 2022-02-02 02:02:02

### 测试

    import datetime
    import gggdtparser
    parse_dt = gggdtparser.parse("发布：2022/02/02 02:02:02，来源：xxx网")
    is_right = gggdtparser.check(parse_dt, datetime.datetime(year=2022, month=2, day=2, hour=2, minute=2, second=2))
    print(is_right)  # True

## 使用案例

### 详细案例

1. 参考dtformat.md中支持的格式。
2. 参考test.py中的测试案例。

### 特色案例

1. 语义时间的支持

```
   il y a 26 minutes
   il y a 1 heure
   Publié aujourd’hui à 10h34, modifié à 10h39
   23分鐘前
   ......      

```

2. 允许噪音

```
   发布于：2023/2/20
   Hoje Macau - 4 Abr 2023 
   2023年04月10日 07:46　来源：新闻网
   ......
```

3. 支持多种语言

```
   31 март 2023  # 俄语
   31 de marzo de 2023  # 西班牙语
   27 Fev 2023  # 卡拜尔语
   ......
```

4. 指定formats

```python
import gggdtparser

dt = gggdtparser.parse("2023-02-20", format_list=["%Y-%m-%d"])
print(dt)
```

5. 指定正则

正则使用有名分组形式，对应关系如下：

| 关键词 |     含义      |            示例            |
|:---:|:---:|:------------------------:|
|  Y  |      年      |      (?P<Y>\d{4})年       |
|  m  |      月      |     (?P<Y>\d{1,2})月      |
|  d  |      日      |     (?P<Y>\d{1,2})日      |
|  H  |      时      |     (?P<Y>\d{1,2})时      |
|  M  |      分      |     (?P<Y>\d{1,2})分      |
|  S  |      秒      |     (?P<Y>\d{1,2})秒      |
| bY  |   在...年前    | (?P<bY>\d+)\s*(年)\s*(前)  |
| bm  |   在...月前    | (?P<bm>\d+)\s*(月)\s*(前)  |
| bd  |   在...日前    | (?P<bd>\d+)\s*(天)\s*(前)  |
| bH  |   在...时前    | (?P<bH>\d+)\s*(小时)\s*(前) |
| bM  |   在...分前    | (?P<bM>\d+)\s*(分钟)\s*(前) |
| bS  |   在...秒前    | (?P<bS>\d+)\s*(秒)\s*(前)  |
| ba  |   在...星期前   | (?P<ba>\d+)\s*(周)\s*(前)  |
| wY  |   在...年内    | (?P<wY>\d+)\s*(年)\s*(内)  |
| wm  |   在...月内    | (?P<wm>\d+)\s*(月)\s*(内)  |
| wd  |   在...日内    | (?P<wd>\d+)\s*(天)\s*(内)  |
| wH  |   在...时内    | (?P<wH>\d+)\s*(小时)\s*(内)  |
| wM  |   在...分内    | (?P<wM>\d+)\s*(分钟)\s*(内)  |
| wS  |   在...秒内    | (?P<wS>\d+)\s*(秒)\s*(内)  |
| wa  |   在...星期内   | (?P<wa>\d+)\s*(周)\s*(内)  |
| sd | 今天/昨天/前天/刚刚 | (?P<sd>前天) | 
| apm |    上午下午     | (?P<apm>am) | 

示例如下：

```python
import gggdtparser

dt = gggdtparser.parse("2023-02-20",
                       regex_list=[r"(?P<Y>\d{4})(?P<m>\d{2})(?P<d>\d{2})"])
print(dt)
```

6. 自定义翻译

```python
import gggdtparser


def translate(s):
    # 翻译
    return ""


dt = gggdtparser.parse("xxx", translate_func=translate)
print(dt)

```

## 待完善

1. 兼容更多语言
2. 对时区的解析

## 关于作者

1. 邮箱：1194542196@qq.com
2. 微信：hu1194542196
3. 目前对常见的时间格式解析支持比较全，但是一些特殊的时间格式和其他语言的支持不够完善，如果遇到解析bug
   或不能解析的时间格式，可以私信作者，你们的提供越多，本库才能更完善。