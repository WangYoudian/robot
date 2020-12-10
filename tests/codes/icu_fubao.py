import unicodedata


def append_head_tail(lst_unicodes):
    utf8_bytes = bytes()
    for unicode_char in lst_unicodes:
        # 将\uxxxx的转为utf-8
        utf8_bytes += unicode_char.encode('utf-8')

    return utf8_bytes


def str2unicode(string):
    """
    1.The opposite method of bytes.decode() is str.encode(),
    which returns a bytes representation of the Unicode string, encoded in the requested encoding.
    2.unicode能用ord方法变成数字 数字使用chr变成str
    """
    print(type(string.encode('utf-8')))  # <class 'bytes'>
    for char in string:
        print(type(chr(ord(char))), end='\t')
    head_tail = append_head_tail(['\u0367', '\u0368', '\u0365'])
    # str方法将bytes对象转为utf-8
    print(str(head_tail, 'utf-8'))
    print(u"%s" % string)


def unicode_property():
    """
    The category codes are abbreviations describing the nature of the character.
    These are grouped into categories such as “Letter”, “Number”, “Punctuation”,
    or “Symbol”, which in turn are broken up into subcategories. To take the codes
    from the above output, 'Ll' means ‘Letter, lowercase’, 'No' means “Number, other”,
    'Mn' is “Mark, nonspacing”, and 'So' is “Symbol, other”. See the General Category
    Values section of the Unicode Character Database documentation for a list of category codes.
    https://www.unicode.org/reports/tr44/#General_Category_Values
    """
    u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)

    for i, c in enumerate(u):
        print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
        print(unicodedata.name(c))

    # Get numeric value of second character
    print(unicodedata.numeric(u[1]))


def generate():
    # 以二进制方式写入文本文件
    with open('生成结果.txt', 'wb') as f:
        for letter in "福报":
            # 写入正文 将str转为bytes
            f.write(letter.encode('utf-8'))
            # 写入修饰符 icu
            # https://utf8-chartable.de/unicode-utf8-table.pl?number=1024
            # 例如：0364代表小e
            # 这种类型的字符为Combining Diacritical Marks组合变音符号
            head_tail = append_head_tail(['\u0367', '\u0368', '\u0365'])
            f.write(head_tail)


if __name__ == '__main__':
    str2unicode('icu')
    u = chr(40960) + 'abcd' + chr(1972)
    print(u.encode('utf-8'))
    # 避免UnicodeEncodeError的加参数方式
    print(u.encode('ascii', 'xmlcharrefreplace'))
    unicode_property()
