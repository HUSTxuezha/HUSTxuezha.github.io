# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:49:16 2023
@author: HUST学渣
"""

import mysql.connector
from jinja2 import Template
import os

# 连接到数据库
conn = mysql.connector.connect(
    host="10.21.4.201",
    user="remoteTest",
    password="dragon040326",
    database="istudy"
)
cursor = conn.cursor()

# 查询所有公式
cursor.execute("SELECT * FROM record")
formulas = cursor.fetchall()

# 使用Jinja2模板引擎渲染HTML页面
template_content = """
<!DOCTYPE html>
<html>
    <head>
        <title>record</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML" async></script>
        <style>
            * {
                box-sizing: border-box;
            }

            /* body 样式 */
            body {
                font-family: Arial;
                margin: 0;
            }

            /* 导航 */
            .navbar {
                overflow: hidden;
                background-color: #ffffff;
            }

            /* 导航栏样式 */
            .navbar a {
                float: left;
                display: block;
                color: #000000;
                text-align: center;
                padding: 14px 20px;
                text-decoration: none;
            }

            /* 右侧链接*/
            .navbar a.right {
                float: right;
            }

            /* 鼠标移动到链接的颜色 */
            .navbar a:hover {
                background-color: #ddd;
                color: #ef61cb;
            }

            /* 按钮 */
            .button {
                background-color: #ffffff;
                border: none;
                border-radius: 50%/100%;
                color: rgb(0, 0, 0);
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 18px;
                margin: 4px 2px;
                margin-right: 20px;
                margin-left: 20px;
                cursor: pointer;
                /*width: 20%;*/
            }

            .button:hover{
                background-color: #ff87e1;
                color: white;
            }

            .r{
                display: block;
            }

            .b{
                display: none;
            }

            .s{
                display: none;
            }

            /* 响应式布局 - 在屏幕设备宽度尺寸小于 700px 时, 让两栏上下堆叠显示 */
            @media screen and (max-width: 700px) {
                .row {   
                    flex-direction: column;
                }
            }

            /* 响应式布局 - 在屏幕设备宽度尺寸小于 400px 时, 让导航栏目上下堆叠显示 */
            @media screen and (max-width: 400px) {
                .navbar a {
                    float: none;
                    width: 100%;
                }
            }
        </style>
    </head>
    <body>

        <img src="decoration\logo.png" width="5%" style="float:left;"/>

        <div class="navbar">
            <a href="record.html">个人记录</a>
            <a href="../index.html" class="right">返回首页</a>
        </div>

        <div class="navbar navbar2">
            <button class="button" onmouseover="change('r')">学习记录</button>
            <button class="button" onmouseover="change('b')">错题本</button>
            <button class="button" onmouseover="change('s')">我的收藏</button>
        </div>

        <ul>
            <li class="r" id="r">
            <p>这里是学习记录</p>
            {% set index_space = namespace(value=0) %}
            {% for formula in formulas %}
                {% set index_space.value = index_space.value + 1 %}
                <div>
                    ({{ index_space.value }})<br>
                    <p>题目：</p>
                    <script type="math/tex">
                        {{ formula[1] }}
                    </script>
                    <p>答案：</p>
                    <script type="math/tex">
                        {{ formula[2] }}
                    </script>
                    <p>解析：</p>
                    <script type="math/tex">
                        {{ formula[3] }}
                    </script>
                </div>
                <div style="margin-bottom: 20px;"></div>
            {% endfor %}
            </li>
            <li class="b" id="b">
            <p>这里是错题本</p>
            {% set index_space = namespace(value=0) %}
            {% for formula in formulas %}
                {% if formula[4] %}
                {% set index_space.value = index_space.value + 1 %}
                <div>
                    ({{ index_space.value }})<br>
                    <p>题目：</p>
                    <script type="math/tex">
                        {{ formula[1] }}
                    </script>
                    <p>答案：</p>
                    <script type="math/tex">
                        {{ formula[2] }}
                    </script>
                    <p>解析：</p>
                    <script type="math/tex">
                        {{ formula[3] }}
                    </script>
                </div>
                <div style="margin-bottom: 20px;"></div>
                {% endif %}
            {% endfor %}
            </li>
            <li class="s" id="s">
            <p>这里是我的收藏</p>
            {% set index_space = namespace(value=0) %}
            {% for formula in formulas %}
                {% if formula[5] %}
                {% set index_space.value = index_space.value + 1 %}
                <div>
                    ({{ index_space.value }})<br>
                    <p>题目：</p>
                    <script type="math/tex">
                        {{ formula[1] }}
                    </script>
                    <p>答案：</p>
                    <script type="math/tex">
                        {{ formula[2] }}
                    </script>
                    <p>解析：</p>
                    <script type="math/tex">
                        {{ formula[3] }}
                    </script>
                </div>
                <div style="margin-bottom: 20px;"></div>
                {% endif %}
            {% endfor %}
            </li>
        </ul>
                
        <img src="decoration\AD0IlreXBhACGAAgj_vPxQUo3N3rsAcwsQk4yAE.jpg" width="100%"/>

        <script type="text/javascript">
            let r = document.getElementById('r')
            let b = document.getElementById('b')
            let s = document.getElementById('s')
            function change(name) {
                if (name =='r'){
                    r.style.display = 'block'
                    b.style.display = 'none'
                    s.style.display = 'none'
                }
                else if(name == 'b'){
                    r.style.display = 'none'
                    b.style.display = 'block'
                    s.style.display = 'none'
                }
                else if(name == 's'){
                    r.style.display = 'none'
                    b.style.display = 'none'
                    s.style.display = 'block'
                }
            }
        </script>
        
    </body>
</html>
"""

template = Template(template_content)
rendered_html = template.render(formulas=formulas)

# 创建 frontend 文件夹（如果不存在）
output_folder = "../frontend"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 将渲染后的HTML页面写入到输出文件中
output_file = os.path.join(output_folder, "record.html")
with open(output_file, "w") as file:
    file.write(rendered_html)

cursor.close()
conn.close()

os.system("start ../frontend/record.html")
