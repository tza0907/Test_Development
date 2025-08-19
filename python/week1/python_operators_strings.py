#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python运算符与字符串介绍
本模块介绍Python的运算符和字符串操作，以及它们在测试开发中的应用
"""

# ===============================
# 第一部分：Python运算符概述
# ===============================
print("=" * 50)
print("第一部分：Python运算符概述")
print("=" * 50)

print("Python运算符分为以下几类：")
print("1. 算术运算符：+, -, *, /, //, %, **")
print("2. 比较运算符：==, !=, >, <, >=, <=")
print("3. 赋值运算符：=, +=, -=, *=, /=, //=, %=, **=")
print("4. 逻辑运算符：and, or, not")
print("5. 位运算符：&, |, ^, ~, <<, >>")
print("6. 成员运算符：in, not in")
print("7. 身份运算符：is, is not")

# ===============================
# 第二部分：算术运算符
# ===============================
print("\n" + "=" * 50)
print("第二部分：算术运算符")
print("=" * 50)

a, b = 10, 3

print(f"假设 a = {a}, b = {b}")
print(f"加法: a + b = {a + b}")
print(f"减法: a - b = {a - b}")
print(f"乘法: a * b = {a * b}")
print(f"除法(浮点结果): a / b = {a / b}")
print(f"整除(向下取整): a // b = {a // b}")
print(f"取余: a % b = {a % b}")
print(f"幂运算: a ** b = {a ** b}")

# 算术运算符的优先级
print("\n算术运算符的优先级:")
print(f"2 + 3 * 4 = {2 + 3 * 4}")  # 乘法优先级高于加法
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")  # 括号内的运算优先执行
print(f"2 ** 3 ** 2 = {2 ** 3 ** 2}")  # 幂运算是右结合的，相当于2 ** (3 ** 2)

# ===============================
# 第三部分：比较运算符
# ===============================
print("\n" + "=" * 50)
print("第三部分：比较运算符")
print("=" * 50)

a, b = 10, 5

print(f"假设 a = {a}, b = {b}")
print(f"等于: a == b 结果为 {a == b}")
print(f"不等于: a != b 结果为 {a != b}")
print(f"大于: a > b 结果为 {a > b}")
print(f"小于: a < b 结果为 {a < b}")
print(f"大于等于: a >= b 结果为 {a >= b}")
print(f"小于等于: a <= b 结果为 {a <= b}")

# 比较运算符链式使用
print("\n比较运算符的链式使用:")
x = 5
print(f"1 < x < 10 结果为 {1 < x < 10}")  # 相当于 1 < x and x < 10
print(f"10 > x <= 5 结果为 {10 > x <= 5}")  # 相当于 10 > x and x <= 5

# ===============================
# 第四部分：赋值运算符
# ===============================
print("\n" + "=" * 50)
print("第四部分：赋值运算符")
print("=" * 50)

# 基本赋值
x = 10
print(f"基本赋值: x = 10, 结果 x = {x}")

# 复合赋值
x += 5  # 相当于 x = x + 5
print(f"加法赋值: x += 5, 结果 x = {x}")

x -= 3  # 相当于 x = x - 3
print(f"减法赋值: x -= 3, 结果 x = {x}")

x *= 2  # 相当于 x = x * 2
print(f"乘法赋值: x *= 2, 结果 x = {x}")

x /= 4  # 相当于 x = x / 4
print(f"除法赋值: x /= 4, 结果 x = {x}")

x = 20
x //= 3  # 相当于 x = x // 3
print(f"整除赋值: x //= 3, 结果 x = {x}")

x %= 4  # 相当于 x = x % 4
print(f"取余赋值: x %= 4, 结果 x = {x}")

x **= 3  # 相当于 x = x ** 3
print(f"幂运算赋值: x **= 3, 结果 x = {x}")

# ===============================
# 第五部分：逻辑运算符
# ===============================
print("\n" + "=" * 50)
print("第五部分：逻辑运算符")
print("=" * 50)

a, b = True, False

print(f"假设 a = {a}, b = {b}")
print(f"逻辑与: a and b = {a and b}")
print(f"逻辑或: a or b = {a or b}")
print(f"逻辑非: not a = {not a}, not b = {not b}")

# 短路求值
print("\n短路求值:")
print("在逻辑运算中，Python使用短路求值策略：")
print("- 对于 and 运算，如果第一个操作数为 False，则不会计算第二个操作数")
print("- 对于 or 运算，如果第一个操作数为 True，则不会计算第二个操作数")

def func():
    print("函数被调用")
    return True

print("\n短路求值示例:")
# False and func() 不会调用func()
result = False and func()
print(f"False and func() = {result}")

# True or func() 不会调用func()
result = True or func()
print(f"True or func() = {result}")

# True and func() 会调用func()
result = True and func()
print(f"True and func() = {result}")

# False or func() 会调用func()
result = False or func()
print(f"False or func() = {result}")

# ===============================
# 第六部分：位运算符
# ===============================
print("\n" + "=" * 50)
print("第六部分：位运算符")
print("=" * 50)

a, b = 60, 13  # 二进制: a = 0011 1100, b = 0000 1101

print(f"假设 a = {a} (二进制: {bin(a)}), b = {b} (二进制: {bin(b)})")
print(f"按位与: a & b = {a & b} (二进制: {bin(a & b)})")
print(f"按位或: a | b = {a | b} (二进制: {bin(a | b)})")
print(f"按位异或: a ^ b = {a ^ b} (二进制: {bin(a ^ b)})")
print(f"按位取反: ~a = {~a} (二进制: {bin(~a)})")
print(f"左移两位: a << 2 = {a << 2} (二进制: {bin(a << 2)})")
print(f"右移两位: a >> 2 = {a >> 2} (二进制: {bin(a >> 2)})")

# ===============================
# 第七部分：成员运算符和身份运算符
# ===============================
print("\n" + "=" * 50)
print("第七部分：成员运算符和身份运算符")
print("=" * 50)

# 成员运算符
fruits = ["苹果", "香蕉", "橙子"]
print(f"列表: {fruits}")
print(f"'香蕉' in fruits = {'香蕉' in fruits}")
print(f"'葡萄' in fruits = {'葡萄' in fruits}")
print(f"'葡萄' not in fruits = {'葡萄' not in fruits}")

# 身份运算符
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"\na = {a}, b = {b}, c = a")
print(f"a is b = {a is b}")  # False，a和b是不同的对象
print(f"a is c = {a is c}")  # True，a和c是同一个对象
print(f"a == b = {a == b}")  # True，a和b的值相等

# ===============================
# 第八部分：运算符优先级
# ===============================
print("\n" + "=" * 50)
print("第八部分：运算符优先级")
print("=" * 50)

print("Python运算符优先级从高到低排列：")
print("1. 括号 ()")
print("2. 幂运算 **")
print("3. 正负号 +x, -x")
print("4. 乘除模 *, /, //, %")
print("5. 加减 +, -")
print("6. 移位 <<, >>")
print("7. 按位与 &")
print("8. 按位异或 ^")
print("9. 按位或 |")
print("10. 比较运算符 ==, !=, >, >=, <, <=, is, is not, in, not in")
print("11. 逻辑非 not")
print("12. 逻辑与 and")
print("13. 逻辑或 or")
print("14. 条件表达式 if-else")
print("15. 赋值运算符 =, +=, -=, 等")

# 复杂表达式示例
print("\n复杂表达式示例:")
result = 2 ** 3 * 4 + 5 & 7 or 8 and 9
print(f"2 ** 3 * 4 + 5 & 7 or 8 and 9 = {result}")
print("计算过程: 2 ** 3 = 8, 8 * 4 = 32, 32 + 5 = 37, 37 & 7 = 5, 8 and 9 = 9, 5 or 9 = 5")

# ===============================
# 第九部分：字符串基础
# ===============================
print("\n" + "=" * 50)
print("第九部分：字符串基础")
print("=" * 50)

# 字符串创建
single_quotes = '单引号字符串'
double_quotes = "双引号字符串"
triple_quotes = '''三引号字符串，
可以跨越多行'''
raw_string = r'原始字符串，不处理转义字符如\n'

print(f"单引号: {single_quotes}")
print(f"双引号: {double_quotes}")
print(f"三引号: {triple_quotes}")
print(f"原始字符串: {raw_string}")

# 转义字符
print("\n转义字符:")
print("换行符: 'Hello\\nWorld' 显示为:")
print('Hello\nWorld')
print("制表符: 'Hello\\tWorld' 显示为:")
print('Hello\tWorld')
print("反斜杠: 'C:\\\\Users\\\\Admin' 显示为:")
print('C:\\Users\\Admin')
print("引号: 'He said, \\'Hello\\'' 显示为:")
print('He said, \'Hello\'')

# ===============================
# 第十部分：字符串操作
# ===============================
print("\n" + "=" * 50)
print("第十部分：字符串操作")
print("=" * 50)

# 字符串索引和切片
text = "Python测试开发"
print(f"字符串: {text}")
print(f"长度: {len(text)}")
print(f"第一个字符: {text[0]}")
print(f"最后一个字符: {text[-1]}")
print(f"切片 [0:6]: {text[0:6]}")
print(f"切片 [6:]: {text[6:]}")
print(f"切片 [:6]: {text[:6]}")
print(f"步长为2的切片 [::2]: {text[::2]}")
print(f"反向切片 [::-1]: {text[::-1]}")

# 字符串拼接
print("\n字符串拼接:")
s1 = "Hello"
s2 = "World"
print(f"s1 = {s1}, s2 = {s2}")
print(f"s1 + s2 = {s1 + s2}")
print(f"s1 + ' ' + s2 = {s1 + ' ' + s2}")
print(f"s1 * 3 = {s1 * 3}")

# 字符串方法
print("\n字符串常用方法:")
s = " Hello, World! "
print(f"原始字符串: '{s}'")
print(f"大写: s.upper() = '{s.upper()}'")
print(f"小写: s.lower() = '{s.lower()}'")
print(f"首字母大写: s.capitalize() = '{s.capitalize()}'")
print(f"标题化: s.title() = '{s.title()}'")
print(f"去除两端空格: s.strip() = '{s.strip()}'")
print(f"替换: s.replace('World', 'Python') = '{s.replace('World', 'Python')}'")
print(f"分割: s.split(',') = {s.split(',')}")
print(f"查找: s.find('World') = {s.find('World')}")
print(f"计数: s.count('l') = {s.count('l')}")
print(f"判断开头: s.startswith(' Hello') = {s.startswith(' Hello')}")
print(f"判断结尾: s.endswith('! ') = {s.endswith('! ')}")
print(f"判断是否为字母数字: 'abc123'.isalnum() = {'abc123'.isalnum()}")
print(f"判断是否为字母: 'abc'.isalpha() = {'abc'.isalpha()}")
print(f"判断是否为数字: '123'.isdigit() = {'123'.isdigit()}")
print(f"判断是否为小写: 'abc'.islower() = {'abc'.islower()}")
print(f"判断是否为大写: 'ABC'.isupper() = {'ABC'.isupper()}")
print(f"判断是否为空白: '   '.isspace() = {'   '.isspace()}")

# 字符串格式化
print("\n字符串格式化:")
name = "张三"
age = 30

# f-string (Python 3.6+)
print(f"f-string: f'姓名: {{name}}, 年龄: {{age}}' = '姓名: {name}, 年龄: {age}'")

# format方法
print(f"format方法: '姓名: {{name}}, 年龄: {{age}}'.format(name='{name}', age={age}) = '姓名: {name}, 年龄: {age}'")
print(f"format位置参数: '姓名: {{}}, 年龄: {{}}'.format('{name}', {age}) = '姓名: {name}, 年龄: {age}'")
print(f"format索引参数: '{{1}}在{{0}}岁时'.format('{age}', '{name}') = '{name}在{age}岁时'")

# %操作符
print(f"%操作符: '姓名: %s, 年龄: %d' % ('{name}', {age}) = '姓名: {name}, 年龄: {age}'")

# 格式化规范
print("\n格式化规范:")
pi = 3.14159265359
print(f"保留两位小数: {pi:.2f}")
print(f"百分比格式: {pi:.2%}")
print(f"科学计数法: {pi:.2e}")
print(f"宽度为10，右对齐: '{pi:10.2f}'")
print(f"宽度为10，左对齐: '{pi:<10.2f}'")
print(f"宽度为10，居中对齐: '{pi:^10.2f}'")
print(f"使用0填充: '{pi:010.2f}'")
print(f"带符号: '{pi:+.2f}'")

# 字符串的不可变性
print("\n字符串的不可变性:")
s = "Hello"
print(f"原始字符串: {s}")
print("尝试修改字符串会创建新的字符串对象")
s = s + " World"
print(f"修改后: {s}")

# ===============================
# 第十一部分：字符串与其他类型的转换
# ===============================
print("\n" + "=" * 50)
print("第十一部分：字符串与其他类型的转换")
print("=" * 50)

# 字符串转数值
print("字符串转数值:")
print(f"int('42') = {int('42')}")
print(f"float('3.14') = {float('3.14')}")
print(f"int('0xFF', 16) = {int('0xFF', 16)}")  # 十六进制
print(f"int('0b1010', 2) = {int('0b1010', 2)}")  # 二进制

# 数值转字符串
print("\n数值转字符串:")
print(f"str(42) = {str(42)}")
print(f"str(3.14) = {str(3.14)}")
print(f"hex(255) = {hex(255)}")  # 转十六进制字符串
print(f"bin(10) = {bin(10)}")  # 转二进制字符串
print(f"oct(8) = {oct(8)}")  # 转八进制字符串

# 字符串与列表转换
print("\n字符串与列表转换:")
s = "Hello"
chars = list(s)
print(f"字符串: {s}")
print(f"转换为列表: list(s) = {chars}")
print(f"列表转回字符串: ''.join(chars) = {''.join(chars)}")

# 字符串与字节转换
print("\n字符串与字节转换:")
text = "Python测试"
encoded = text.encode('utf-8')
print(f"字符串: {text}")
print(f"编码为bytes: {encoded}")
decoded = encoded.decode('utf-8')
print(f"解码回字符串: {decoded}")

# ===============================
# 第十二部分：运算符和字符串在测试开发中的应用
# ===============================
print("\n" + "=" * 50)
print("第十二部分：运算符和字符串在测试开发中的应用")
print("=" * 50)

# 1. 测试断言中的比较运算符
print("\n1. 测试断言中的比较运算符:")
expected_status = 200
actual_status = 200
print(f"断言HTTP状态码: expected_status({expected_status}) == actual_status({actual_status})")
assert expected_status == actual_status, "HTTP状态码不匹配"
print("断言通过!")

expected_response = {"status": "success", "data": {"id": 123}}
actual_response = {"status": "success", "data": {"id": 123}}
print(f"\n断言响应内容: expected_response == actual_response")
assert expected_response == actual_response, "响应内容不匹配"
print("断言通过!")

# 2. 测试条件判断中的逻辑运算符
print("\n2. 测试条件判断中的逻辑运算符:")
status_code = 201
is_created = True
print(f"检查是否创建成功: status_code == 201 and is_created")
if status_code == 201 and is_created:
    print("资源创建成功!")

response_time = 1.5  # 秒
timeout = 2.0  # 秒
print(f"\n检查响应时间: response_time({response_time}) < timeout({timeout}) or status_code == 200")
if response_time < timeout or status_code == 200:
    print("响应时间在可接受范围内!")

# 3. 测试数据处理中的算术运算符
print("\n3. 测试数据处理中的算术运算符:")
test_durations = [1.2, 0.8, 1.5, 0.9, 1.1]
total_duration = sum(test_durations)
average_duration = total_duration / len(test_durations)
print(f"测试用例执行时间: {test_durations}")
print(f"总执行时间: {total_duration:.2f}秒")
print(f"平均执行时间: {average_duration:.2f}秒")

# 4. 测试报告生成中的字符串操作
print("\n4. 测试报告生成中的字符串操作:")
test_results = [
    {"name": "test_login", "status": "PASS", "duration": 1.2},
    {"name": "test_logout", "status": "PASS", "duration": 0.8},
    {"name": "test_payment", "status": "FAIL", "duration": 1.5},
    {"name": "test_profile", "status": "PASS", "duration": 0.9}
]

# 生成测试报告
report = []
report.append("=" * 40)
report.append("测试执行报告")
report.append("=" * 40)
report.append(f"执行时间: 2023-08-20 10:30:00")
report.append(f"测试用例数: {len(test_results)}")
report.append(f"通过数量: {sum(1 for r in test_results if r['status'] == 'PASS')}")
report.append(f"失败数量: {sum(1 for r in test_results if r['status'] == 'FAIL')}")
report.append("-" * 40)
report.append(f"{'测试用例名称':<20}{'状态':<10}{'执行时间(秒)':<15}")
report.append("-" * 40)

for test in test_results:
    report.append(f"{test['name']:<20}{test['status']:<10}{test['duration']:<15.2f}")

report.append("=" * 40)
report_text = "\n".join(report)
print(report_text)

# 5. 测试数据解析中的字符串方法
print("\n5. 测试数据解析中的字符串方法:")
log_line = "2023-08-20 10:30:45 [INFO] User 'admin' logged in successfully from 192.168.1.100"
print(f"日志行: {log_line}")

# 解析日志
parts = log_line.split(" ", 3)  # 分割日期、时间、级别和消息
date = parts[0]
time = parts[1]
level = parts[2].strip("[]")
message = parts[3]

print(f"日期: {date}")
print(f"时间: {time}")
print(f"日志级别: {level}")
print(f"消息: {message}")

# 进一步解析消息
if "logged in" in message:
    username = message.split("'")[1]
    ip = message.split("from ")[1]
    print(f"用户名: {username}")
    print(f"IP地址: {ip}")

# 6. 测试用例参数化中的字符串格式化
print("\n6. 测试用例参数化中的字符串格式化:")
test_cases = [
    {"id": 1, "input": "admin", "expected": "Welcome, admin!"},
    {"id": 2, "input": "guest", "expected": "Welcome, guest!"},
    {"id": 3, "input": "", "expected": "Please enter a username"}
]

for tc in test_cases:
    # 生成测试用例名称
    test_name = f"test_login_case_{tc['id']}"
    # 生成测试用例描述
    description = f"测试用户 '{tc['input']}' 登录响应"
    # 模拟测试执行
    actual = f"Welcome, {tc['input']}!" if tc['input'] else "Please enter a username"
    # 检查结果
    result = "PASS" if actual == tc['expected'] else "FAIL"
    
    print(f"执行测试: {test_name}")
    print(f"描述: {description}")
    print(f"预期结果: {tc['expected']}")
    print(f"实际结果: {actual}")
    print(f"测试结果: {result}")
    print("-" * 30)

# 7. 测试环境配置中的字符串操作
print("\n7. 测试环境配置中的字符串操作:")
# 解析配置文件内容
config_text = """
[server]
host = api.example.com
port = 443
protocol = https

[auth]
username = test_user
password = test_pass
token_expiry = 3600

[logging]
level = INFO
file = /var/log/test.log
"""

print("配置文件内容:")
print(config_text)

# 简单解析配置
config = {}
current_section = None

for line in config_text.strip().split("\n"):
    line = line.strip()
    if not line:
        continue
    
    if line.startswith("[") and line.endswith("]"):
        current_section = line[1:-1]
        config[current_section] = {}
    elif current_section and "=" in line:
        key, value = line.split("=", 1)
        config[current_section][key.strip()] = value.strip()

print("\n解析后的配置:")
for section, items in config.items():
    print(f"[{section}]")
    for key, value in items.items():
        print(f"  {key} = {value}")

# 构建API URL
base_url = f"{config['server']['protocol']}://{config['server']['host']}"
if config['server']['port'] != "80" and config['server']['port'] != "443":
    base_url += f":{config['server']['port']}"

print(f"\n构建的API基础URL: {base_url}")

# 8. 测试数据验证中的位运算符
print("\n8. 测试数据验证中的位运算符:")
# 使用位掩码表示权限
READ = 1      # 0001
WRITE = 2     # 0010
UPDATE = 4    # 0100
DELETE = 8    # 1000

# 用户权限
user_permission = READ | WRITE  # 0011

print(f"权限常量: READ={READ}, WRITE={WRITE}, UPDATE={UPDATE}, DELETE={DELETE}")
print(f"用户权限: {user_permission} (二进制: {bin(user_permission)})")

# 检查用户是否有特定权限
print(f"用户是否有读权限: {bool(user_permission & READ)}")
print(f"用户是否有写权限: {bool(user_permission & WRITE)}")
print(f"用户是否有更新权限: {bool(user_permission & UPDATE)}")
print(f"用户是否有删除权限: {bool(user_permission & DELETE)}")

# 添加权限
user_permission |= UPDATE
print(f"添加更新权限后: {user_permission} (二进制: {bin(user_permission)})")

# 移除权限
user_permission &= ~WRITE
print(f"移除写权限后: {user_permission} (二进制: {bin(user_permission)})")

print("\n总结：")
print("Python的运算符和字符串操作在测试开发中有广泛的应用：")
print("- 比较运算符用于测试断言和结果验证")
print("- 逻辑运算符用于测试条件判断和复合条件")
print("- 算术运算符用于测试数据处理和统计")
print("- 字符串操作用于测试报告生成、日志解析和数据处理")
print("- 位运算符用于权限和标志位的处理")
print("掌握这些操作可以帮助测试开发人员编写更高效、更可靠的测试代码。")