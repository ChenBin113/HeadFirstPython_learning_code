# 标准库string，类Template，字符串$
# 支持简单的字符串替换模板
from string import Template


# 默认参数，初始响应--目录
def start_response(resp="text/html"):
    return 'Content-type: ' + resp + '\n\n'


# 关键字参数，标题可以替换，页面本身存储在一个文件中
def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return header.substitute(title=the_title)


# 关键字参数，页脚，参数应当是一个字典
def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + \
                       '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
        # '</a>&nbsp;&nbsp;&nbsp;&nbsp;'加入空格的一种做法
    footer = Template(foot_text)
    return footer.substitute(links=link_string)


# 开始形式，调用表单数据到页面
def start_form(the_url, form_type="POST"):
    return '<form action="' + the_url + '" method="' + form_type + '">'


# 结束形式，定制表单，提交按钮的文本
def end_form(submit_msg="Submit"):
    return '<p></p><input type=submit value="' +\
           submit_msg + '"></form>'


# 按钮
def radio_button(rb_name, rb_value):
    return '<input type="radio" name="' + rb_name +\
           '" value="' + rb_value + '"> ' + rb_value + '<br />'


# 列表
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return u_string


# 标题
def header(header_text, header_level=2):
    return '<h' + str(header_level) + '>' + header_text +\
           '</h' + str(header_level) + '>'


# 暂不清楚，好像没必要
def para(para_text):
    return '<p>' + para_text + '</p>'


# 以下为测试用
print(start_response())
print(start_response("text/plain"))
print(start_response("application/json"))
print(include_header("Welcome to my home on the web"))
print(include_footer({'Home': '/index.html',
                      'Select': '/cgi-bin/select.py'}))
print(include_footer({}))
print(start_form("/cgi-bin/process-athlete.py"))
print(end_form())
print(end_form("Click to Confirm your Order"))
for fab in ['John', 'Paul', 'George', 'Ringo']:
    print(radio_button(fab, fab))
print(u_list(['Life of Brian', 'Holy Grail']))
# 默认是2
print(header("Welcome to my home on the web"))
print(header("This is a sub-sub-sub-sub heading", 5))
print(para("Was it worth the wait? We hope it was ..."))

