# I study平台——版本0.1

> 这是I study的极简版本，仅包含休闲模式（单人刷题）和个人记录。
>
> **基本功能介绍**：首先，用户可以导入题库并存储题库，也可利用AI生成题库。其次，AI判定题目难度和考察的知识点，对题目进行分类，根据用户的选择抽取题目。最后，记录用户的作答情况，并利用AI进行批改。

### 后端开发

- 建立数据库，导入并存储题库
- 训练AI对题目难度和知识点进行判定（如较难，则人为设置）
- 训练AI随机生成题目
- 根据难度和知识点抽取题目
- 利用数据库记录用户作答情况
- 训练AI批改用户答案
- 设计并实现后端API接口，用于前端与后端的数据交互

### 前端开发

- 用户界面设计，包括图标、按键、表单等基本元素的设计
- 实现用户导入题库文件的功能
- 创建界面供用户生成题库，选择生成题目的类型和数量
- 题目分类和抽取功能：展示题目分类选项，允许用户根据难度和知识点选择题目。根据用户的选择，向后端发送请求以抽取相应的题目。
- 根据作答情况生成评价报告，反馈用户的得分、正确率、进步等信息。