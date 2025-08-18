#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python基本数据类型介绍
本模块介绍Python的基本数据类型及其在测试开发中的应用
"""

# ===============================
# 第一部分：Python基本数据类型概述
# ===============================
print("=" * 50)
print("第一部分：Python基本数据类型概述")
print("=" * 50)

print("Python有以下几种基本数据类型：")
print("1. 数值类型：整数(int)、浮点数(float)、复数(complex)")
print("2. 字符串类型(str)")
print("3. 布尔类型(bool)")
print("4. 空值类型(None)")
print("5. 序列类型：列表(list)、元组(tuple)、范围(range)")
print("6. 映射类型：字典(dict)")
print("7. 集合类型：集合(set)、固定集合(frozenset)")
print("8. 二进制类型：字节(bytes)、字节数组(bytearray)、内存视图(memoryview)")

# ===============================
# 第二部分：数值类型
# ===============================
print("\n" + "=" * 50)
print("第二部分：数值类型")
print("=" * 50)

# 整数类型(int)
print("\n1. 整数类型(int):")
int_num = 42
negative_int = -100
big_int = 10000000000000000000000
print(f"普通整数: {int_num}, 类型: {type(int_num)}")
print(f"负整数: {negative_int}, 类型: {type(negative_int)}")
print(f"大整数: {big_int}, 类型: {type(big_int)}")
print("特点: Python整数没有大小限制，只受限于可用内存")

# 进制表示
print("\n整数的不同进制表示:")
print(f"十进制: {42}")
print(f"二进制: {0b101010} (0b前缀)")
print(f"八进制: {0o52} (0o前缀)")
print(f"十六进制: {0x2A} (0x前缀)")

# 浮点数类型(float)
print("\n2. 浮点数类型(float):")
float_num = 3.14
scientific = 1.23e-4  # 科学计数法
print(f"普通浮点数: {float_num}, 类型: {type(float_num)}")
print(f"科学计数法: {scientific}, 类型: {type(scientific)}")
print("特点: 浮点数可能存在精度问题")

# 浮点数精度问题
print("\n浮点数精度问题:")
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # 不等于0.3
print(f"解决方法 - 使用decimal模块:")
from decimal import Decimal
print(f"Decimal('0.1') + Decimal('0.2') = {Decimal('0.1') + Decimal('0.2')}")

# 复数类型(complex)
print("\n3. 复数类型(complex):")
complex_num = 3 + 4j
print(f"复数: {complex_num}, 类型: {type(complex_num)}")
print(f"实部: {complex_num.real}, 虚部: {complex_num.imag}")
print(f"共轭复数: {complex_num.conjugate()}")

# ===============================
# 第三部分：字符串类型(str)
# ===============================
print("\n" + "=" * 50)
print("第三部分：字符串类型(str)")
print("=" * 50)

# 字符串创建
print("\n字符串创建:")
single_quotes = '单引号字符串'
double_quotes = "双引号字符串"
triple_quotes = '''三引号字符串，
可以跨越多行'''
raw_string = r'原始字符串，不处理转义字符如\n'

print(f"单引号: {single_quotes}")
print(f"双引号: {double_quotes}")
print(f"三引号: {triple_quotes}")
print(f"原始字符串: {raw_string}")

# 字符串操作
print("\n字符串操作:")
text = "Python测试开发"
print(f"原始字符串: {text}")
print(f"长度: {len(text)}")
print(f"索引访问: text[0] = {text[0]}")
print(f"切片: text[0:6] = {text[0:6]}")
print(f"拼接: text + '很有趣' = {text + '很有趣'}")
print(f"重复: 'abc' * 3 = {'abc' * 3}")
print(f"成员检查: '测试' in text = {'测试' in text}")

# 字符串方法
print("\n常用字符串方法:")
s = " hello, world! "
print(f"原始字符串: '{s}'")
print(f"大写: s.upper() = '{s.upper()}'")
print(f"小写: s.lower() = '{s.lower()}'")
print(f"首字母大写: s.capitalize() = '{s.capitalize()}'")
print(f"标题化: s.title() = '{s.title()}'")
print(f"去除两端空格: s.strip() = '{s.strip()}'")
print(f"替换: s.replace('world', 'Python') = '{s.replace('world', 'Python')}'")
print(f"分割: s.split(',') = {s.split(',')}")
print(f"查找: s.find('world') = {s.find('world')}")

# 字符串格式化
print("\n字符串格式化:")
name = "张三"
age = 30
# f-string (Python 3.6+)
print(f"f-string: f'姓名: {name}, 年龄: {age}' = '姓名: {name}, 年龄: {age}'")
# format方法
print(f"format方法: '姓名: {{name}}, 年龄: {{age}}'.format(name='{name}', age={age}) = '姓名: {name}, 年龄: {age}'")
# %操作符
print(f"%%操作符: '姓名: %s, 年龄: %d' %% (name, age) = '姓名: {name}, 年龄: {age}'")

# ===============================
# 第四部分：布尔类型(bool)和空值(None)
# ===============================
print("\n" + "=" * 50)
print("第四部分：布尔类型(bool)和空值(None)")
print("=" * 50)

# 布尔类型
print("\n布尔类型(bool):")
true_value = True
false_value = False
print(f"True的值: {true_value}, 类型: {type(true_value)}")
print(f"False的值: {false_value}, 类型: {type(false_value)}")

print("\n布尔运算:")
print(f"与运算: True and False = {True and False}")
print(f"或运算: True or False = {True or False}")
print(f"非运算: not True = {not True}")

print("\n隐式布尔转换:")
print("以下值在布尔上下文中被视为False:")
print(f"False: {bool(False)}")
print(f"None: {bool(None)}")
print(f"0: {bool(0)}")
print(f"0.0: {bool(0.0)}")
print(f"空字符串: {bool('')}")
print(f"空列表: {bool([])}")
print(f"空元组: {bool(())}")
print(f"空字典: {bool({})}")
print(f"空集合: {bool(set())}")

print("\n其他所有值在布尔上下文中被视为True")

# None类型
print("\nNone类型:")
none_value = None
print(f"None的值: {none_value}, 类型: {type(none_value)}")
print("None表示空值或缺少值，常用于表示函数没有返回值或参数的默认值")

# ===============================
# 第五部分：序列类型
# ===============================
print("\n" + "=" * 50)
print("第五部分：序列类型")
print("=" * 50)

# 列表(list)
print("\n1. 列表(list):")
my_list = [1, 2, 3, "四", "五", True, [7, 8]]
print(f"列表示例: {my_list}, 类型: {type(my_list)}")
print(f"长度: {len(my_list)}")
print(f"索引访问: my_list[3] = {my_list[3]}")
print(f"切片: my_list[2:5] = {my_list[2:5]}")
print(f"嵌套访问: my_list[6][0] = {my_list[6][0]}")

print("\n列表操作:")
fruits = ["苹果", "香蕉", "橙子"]
print(f"原始列表: {fruits}")
fruits.append("葡萄")
print(f"添加元素(append): {fruits}")
fruits.insert(1, "梨")
print(f"插入元素(insert): {fruits}")
removed = fruits.pop(2)
print(f"删除元素(pop): {fruits}, 删除的元素: {removed}")
fruits.remove("葡萄")
print(f"移除指定元素(remove): {fruits}")
fruits.sort()
print(f"排序(sort): {fruits}")
fruits.reverse()
print(f"反转(reverse): {fruits}")
fruits_copy = fruits.copy()
print(f"复制(copy): {fruits_copy}")

# 列表推导式
print("\n列表推导式:")
squares = [x**2 for x in range(1, 6)]
print(f"平方列表: [x**2 for x in range(1, 6)] = {squares}")
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"偶数平方: [x**2 for x in range(1, 11) if x % 2 == 0] = {even_squares}")

# 元组(tuple)
print("\n2. 元组(tuple):")
my_tuple = (1, 2, 3, "四", "五", True)
print(f"元组示例: {my_tuple}, 类型: {type(my_tuple)}")
print(f"长度: {len(my_tuple)}")
print(f"索引访问: my_tuple[3] = {my_tuple[3]}")
print(f"切片: my_tuple[2:5] = {my_tuple[2:5]}")

print("\n元组特点:")
print("- 元组是不可变的，创建后不能修改")
print("- 元组通常用于表示固定的数据集合")
print("- 元组比列表更高效（内存使用和性能）")

# 单元素元组需要逗号
single_tuple = (42,)
print(f"单元素元组: {single_tuple}, 类型: {type(single_tuple)}")
not_tuple = (42)
print(f"没有逗号: {not_tuple}, 类型: {type(not_tuple)} (这不是元组!)")

# 元组解包
print("\n元组解包:")
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"坐标: {coordinates}")
print(f"解包后: x={x}, y={y}, z={z}")

# range类型
print("\n3. range类型:")
r1 = range(5)
r2 = range(2, 10)
r3 = range(0, 10, 2)
print(f"range(5): {list(r1)}")
print(f"range(2, 10): {list(r2)}")
print(f"range(0, 10, 2): {list(r3)}")
print("range对象是不可变的序列，通常用于for循环")

# ===============================
# 第六部分：映射类型 - 字典(dict)
# ===============================
print("\n" + "=" * 50)
print("第六部分：映射类型 - 字典(dict)")
print("=" * 50)

# 字典创建
print("\n字典创建:")
person = {
    "name": "张三",
    "age": 30,
    "skills": ["Python", "测试", "自动化"],
    "is_tester": True
}
print(f"字典示例: {person}, 类型: {type(person)}")

# 另一种创建方式
dict_constructor = dict(name="李四", age=25, is_tester=False)
print(f"使用dict()构造: {dict_constructor}")

# 字典操作
print("\n字典操作:")
print(f"长度: {len(person)}")
print(f"访问键值: person['name'] = {person['name']}")
print(f"get方法(安全访问): person.get('salary', '未设置') = {person.get('salary', '未设置')}")

# 修改字典
print("\n修改字典:")
person["age"] = 31
print(f"修改值: {person}")
person["salary"] = 15000
print(f"添加新键值对: {person}")
del person["is_tester"]
print(f"删除键值对: {person}")

# 字典方法
print("\n字典方法:")
print(f"所有键: {person.keys()}")
print(f"所有值: {person.values()}")
print(f"所有键值对: {person.items()}")

# 字典推导式
print("\n字典推导式:")
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"平方字典: {{x: x**2 for x in range(1, 6)}} = {squares_dict}")

# ===============================
# 第七部分：集合类型
# ===============================
print("\n" + "=" * 50)
print("第七部分：集合类型")
print("=" * 50)

# 集合(set)
print("\n1. 集合(set):")
my_set = {1, 2, 3, 4, 5, 3, 2}  # 重复元素会被自动去除
print(f"集合示例: {my_set}, 类型: {type(my_set)}")
print(f"长度: {len(my_set)}")
print("特点: 集合中的元素是唯一的，无序的，且元素必须是可哈希的")

# 集合操作
print("\n集合操作:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"集合1: {set1}")
print(f"集合2: {set2}")
print(f"并集: set1 | set2 = {set1 | set2}")
print(f"交集: set1 & set2 = {set1 & set2}")
print(f"差集: set1 - set2 = {set1 - set2}")
print(f"对称差集: set1 ^ set2 = {set1 ^ set2}")

# 集合方法
print("\n集合方法:")
fruits_set = {"苹果", "香蕉", "橙子"}
print(f"原始集合: {fruits_set}")
fruits_set.add("葡萄")
print(f"添加元素(add): {fruits_set}")
fruits_set.remove("香蕉")
print(f"删除元素(remove): {fruits_set}")
fruits_set.discard("不存在的元素")  # 不会引发错误
print(f"安全删除(discard): {fruits_set}")

# 固定集合(frozenset)
print("\n2. 固定集合(frozenset):")
frozen = frozenset([1, 2, 3, 4, 5])
print(f"固定集合: {frozen}, 类型: {type(frozen)}")
print("特点: frozenset是不可变的集合，可以作为字典的键或其他集合的元素")

# ===============================
# 第八部分：二进制类型
# ===============================
print("\n" + "=" * 50)
print("第八部分：二进制类型")
print("=" * 50)

# bytes类型
print("\n1. bytes类型:")
byte_data = b'Hello'
print(f"bytes示例: {byte_data}, 类型: {type(byte_data)}")
print(f"长度: {len(byte_data)}")
print(f"索引访问: byte_data[0] = {byte_data[0]} (ASCII码)")
print("特点: bytes是不可变的字节序列")

# bytearray类型
print("\n2. bytearray类型:")
byte_array = bytearray(b'Hello')
print(f"bytearray示例: {byte_array}, 类型: {type(byte_array)}")
byte_array[0] = 74  # ASCII码为'J'
print(f"修改后: {byte_array}")
print("特点: bytearray是可变的字节序列")

# 字符串与字节转换
print("\n字符串与字节转换:")
text = "Python测试"
encoded = text.encode('utf-8')
print(f"字符串: {text}")
print(f"编码为bytes: {encoded}")
decoded = encoded.decode('utf-8')
print(f"解码回字符串: {decoded}")

# ===============================
# 第九部分：类型转换
# ===============================
print("\n" + "=" * 50)
print("第九部分：类型转换")
print("=" * 50)

print("Python内置类型转换函数:")
print(f"int('42') = {int('42')}")
print(f"float('3.14') = {float('3.14')}")
print(f"str(42) = {str(42)}")
print(f"bool(1) = {bool(1)}")
print(f"list('abc') = {list('abc')}")
print(f"tuple([1, 2, 3]) = {tuple([1, 2, 3])}")
print(f"set([1, 2, 2, 3]) = {set([1, 2, 2, 3])}")
print(f"dict([('a', 1), ('b', 2)]) = {dict([('a', 1), ('b', 2)])}")

# ===============================
# 第十部分：数据类型在测试开发中的应用
# ===============================
print("\n" + "=" * 50)
print("第十部分：数据类型在测试开发中的应用")
print("=" * 50)

# 1. 测试数据准备
print("\n1. 测试数据准备:")
# 使用字典存储测试用例
test_cases = [
    {
        "id": 1,
        "name": "登录测试",
        "input": {"username": "test_user", "password": "password123"},
        "expected": {"status": 200, "message": "登录成功"}
    },
    {
        "id": 2,
        "name": "注册测试",
        "input": {"username": "new_user", "email": "new@example.com", "password": "secure123"},
        "expected": {"status": 201, "message": "注册成功"}
    }
]

print(f"测试用例集: {test_cases}")

# 2. 测试结果收集
print("\n2. 测试结果收集:")
# 使用列表存储测试结果
test_results = []

for case in test_cases:
    # 模拟测试执行
    result = {
        "case_id": case["id"],
        "case_name": case["name"],
        "status": "通过" if case["id"] % 2 == 1 else "失败",
        "actual": {"status": 200, "message": "登录成功"} if case["id"] % 2 == 1 else {"status": 400, "message": "参数错误"},
        "timestamp": "2023-08-18 14:30:00"
    }
    test_results.append(result)

print(f"测试结果: {test_results}")

# 3. 测试数据分析
print("\n3. 测试数据分析:")
# 使用集合去重
test_statuses = {result["status"] for result in test_results}
print(f"测试状态类型: {test_statuses}")

# 使用字典统计
status_counts = {}
for result in test_results:
    status = result["status"]
    if status in status_counts:
        status_counts[status] += 1
    else:
        status_counts[status] = 1

print(f"测试状态统计: {status_counts}")

# 4. 测试配置管理
print("\n4. 测试配置管理:")
# 使用字典存储配置
test_config = {
    "environment": "staging",
    "base_url": "https://api.example.com",
    "timeout": 30,
    "retry": {
        "max_attempts": 3,
        "backoff_factor": 0.5
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer token123"
    },
    "features": ["login", "register", "profile"]
}

print(f"测试配置: {test_config}")
print(f"API基础URL: {test_config['base_url']}")
print(f"请求头: {test_config['headers']}")
print(f"重试配置: 最大尝试次数={test_config['retry']['max_attempts']}, 退避因子={test_config['retry']['backoff_factor']}")

# 5. 测试数据生成
print("\n5. 测试数据生成:")
import random
import string

# 生成随机用户数据
def generate_test_user():
    user_id = random.randint(1000, 9999)
    username = f"user_{user_id}"
    email = f"{username}@example.com"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return {
        "id": user_id,
        "username": username,
        "email": email,
        "password": password,
        "is_active": random.choice([True, False])
    }

# 生成测试用户列表
test_users = [generate_test_user() for _ in range(3)]
print(f"生成的测试用户: {test_users}")

# 6. 测试断言
print("\n6. 测试断言:")
# 模拟API响应
api_response = {
    "status": 200,
    "data": {
        "user_id": 1234,
        "username": "test_user",
        "email": "test@example.com",
        "roles": ["user", "tester"]
    },
    "message": "获取用户信息成功"
}

# 使用不同数据类型进行断言
assert api_response["status"] == 200, "状态码不是200"
assert "user_id" in api_response["data"], "响应中缺少user_id字段"
assert isinstance(api_response["data"]["user_id"], int), "user_id不是整数类型"
assert "tester" in api_response["data"]["roles"], "用户不具有tester角色"
assert api_response["message"].startswith("获取"), "消息不是以'获取'开头"

print("所有断言通过!")

# 7. 测试报告生成
print("\n7. 测试报告生成:")
# 使用字典和列表组织测试报告数据
# 先计算关键指标
total_tests = len(test_results)
passed_tests = sum(1 for r in test_results if r["status"] == "通过")
failed_tests = sum(1 for r in test_results if r["status"] == "失败")

# 然后创建测试报告
test_report = {
    "summary": {
        "total": total_tests,
        "passed": passed_tests,
        "failed": failed_tests,
        "duration": "00:05:23"
    },
    "results": test_results,
    "environment": test_config["environment"],
    "timestamp": "2023-08-18 15:00:00"
}

print(f"测试报告摘要: {test_report['summary']}")

# 直接使用已知类型的变量计算通过率
pass_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
print(f"通过率: {pass_rate:.2f}%")

print("\n总结：")
print("Python的基本数据类型为测试开发提供了强大的工具集。")
print("- 数值类型用于计算和比较")
print("- 字符串类型用于文本处理和格式化")
print("- 布尔类型用于条件判断和测试断言")
print("- 列表和元组用于存储有序数据集合")
print("- 字典用于存储键值对数据，如测试用例和配置")
print("- 集合用于数据去重和集合操作")
print("- 二进制类型用于处理二进制数据，如网络通信和文件操作")
print("掌握这些数据类型及其操作，对于编写高效、可靠的测试代码至关重要。")