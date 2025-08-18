#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python变量介绍
本模块介绍Python变量的基本概念、命名规则、赋值操作及其在测试开发中的应用
"""

# ===============================
# 第一部分：什么是变量
# ===============================
print("=" * 50)
print("第一部分：什么是变量")
print("=" * 50)

# 变量是存储数据的容器
name = "张三"
age = 30
is_tester = True

print(f"变量示例：")
print(f"姓名: {name}, 类型: {type(name)}")
print(f"年龄: {age}, 类型: {type(age)}")
print(f"是否测试人员: {is_tester}, 类型: {type(is_tester)}")

print("\n变量的特点：")
print("1. 变量是数据的引用，而非数据本身")
print("2. 变量的类型由所引用的数据决定")
print("3. Python是动态类型语言，变量类型可以改变")

# 动态类型示例
x = 10
print(f"\n变量x初始值: {x}, 类型: {type(x)}")
x = "测试开发"
print(f"变量x现在的值: {x}, 类型: {type(x)}")

# ===============================
# 第二部分：变量命名规则
# ===============================
print("\n" + "=" * 50)
print("第二部分：变量命名规则")
print("=" * 50)

print("Python变量命名规则：")
print("1. 只能包含字母、数字和下划线")
print("2. 不能以数字开头")
print("3. 区分大小写")
print("4. 不能使用Python关键字")

# 有效的变量名示例
valid_name = "有效变量名"
user_1 = "用户1"
_private = "以下划线开头的变量"
camelCase = "驼峰命名法"
snake_case = "蛇形命名法（推荐）"

print("\n命名约定：")
print("1. 类名使用驼峰命名法（首字母大写）：TestCase")
print("2. 函数和变量名使用蛇形命名法（全小写，下划线分隔）：test_result")
print("3. 常量通常全大写：MAX_RETRY_COUNT = 3")
print("4. 私有变量/方法前加单下划线：_internal_method")
print("5. 强制私有（名称改写）变量/方法前加双下划线：__private_var")

# 关键字示例
import keyword
print("\nPython关键字（不能用作变量名）:")
print(keyword.kwlist)

# ===============================
# 第三部分：变量赋值操作
# ===============================
print("\n" + "=" * 50)
print("第三部分：变量赋值操作")
print("=" * 50)

# 基本赋值
a = 10
print(f"基本赋值: a = 10, 结果: a = {a}")

# 多重赋值
b, c = 20, 30
print(f"多重赋值: b, c = 20, 30, 结果: b = {b}, c = {c}")

# 交换变量值
b, c = c, b
print(f"交换变量值: b, c = c, b, 结果: b = {b}, c = {c}")

# 增强赋值运算符
d = 5
d += 3  # 等同于 d = d + 3
print(f"增强赋值: d += 3, 结果: d = {d}")

d -= 2  # 等同于 d = d - 2
print(f"增强赋值: d -= 2, 结果: d = {d}")

d *= 4  # 等同于 d = d * 4
print(f"增强赋值: d *= 4, 结果: d = {d}")

# 解包赋值
fruits = ["苹果", "香蕉", "橙子"]
fruit1, fruit2, fruit3 = fruits
print(f"\n解包赋值: fruit1, fruit2, fruit3 = {fruits}")
print(f"结果: fruit1 = {fruit1}, fruit2 = {fruit2}, fruit3 = {fruit3}")

# 使用_忽略某些值
first, *_, last = [1, 2, 3, 4, 5]
print(f"\n使用*_忽略中间值: first, *_, last = [1, 2, 3, 4, 5]")
print(f"结果: first = {first}, last = {last}")

# ===============================
# 第四部分：变量在测试开发中的应用
# ===============================
print("\n" + "=" * 50)
print("第四部分：变量在测试开发中的应用")
print("=" * 50)

# 1. 测试数据管理
print("\n1. 测试数据管理:")
test_user = {
    "id": 12345,
    "username": "test_user",
    "email": "test@example.com",
    "is_active": True
}

print(f"测试用户数据: {test_user}")

# 2. 测试配置
print("\n2. 测试配置:")
BASE_URL = "https://api.example.com"
MAX_RETRIES = 3
TIMEOUT = 30  # 秒
DEBUG_MODE = True

print(f"基础URL: {BASE_URL}")
print(f"最大重试次数: {MAX_RETRIES}")
print(f"超时时间: {TIMEOUT}秒")
print(f"调试模式: {'开启' if DEBUG_MODE else '关闭'}")

# 3. 测试结果断言
print("\n3. 测试结果断言:")
expected_status_code = 200
actual_status_code = 200
is_test_passed = expected_status_code == actual_status_code

print(f"预期状态码: {expected_status_code}")
print(f"实际状态码: {actual_status_code}")
print(f"测试通过: {is_test_passed}")

# 4. 测试环境切换
print("\n4. 测试环境切换:")
environments = {
    "dev": "https://dev.example.com",
    "test": "https://test.example.com",
    "staging": "https://staging.example.com",
    "prod": "https://example.com"
}

current_env = "test"
api_base_url = environments[current_env]

print(f"当前环境: {current_env}")
print(f"API基础URL: {api_base_url}")

# 5. 测试用例参数化
print("\n5. 测试用例参数化:")
test_cases = [
    {"input": 5, "expected": 25},
    {"input": 10, "expected": 100},
    {"input": 0, "expected": 0}
]

def square(x):
    return x * x

for tc in test_cases:
    input_value = tc["input"]
    expected_value = tc["expected"]
    actual_value = square(input_value)
    result = "通过" if actual_value == expected_value else "失败"
    print(f"测试: square({input_value}) = {actual_value}, 预期: {expected_value}, 结果: {result}")

print("\n总结：")
print("变量是Python编程的基础，在测试开发中扮演着重要角色。")
print("良好的变量命名和使用习惯可以提高代码的可读性和可维护性。")
print("在测试开发中，变量常用于管理测试数据、配置测试环境、断言测试结果等场景。")