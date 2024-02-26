# markdown语法

## 标题

*斜体文本*

_斜体文本_

**粗体文本**

__粗体文本__

***粗斜体文本***

___粗斜体文本___

***

- 

* 

--------

~~bushi~~

---

<u>带下划线文本</u>

---

创建脚注格式类似这样 [^WRF]。

[^WRF]:pain

----

### 无序表

* 

+ 

- 

---

### 有序表

1. 
2.  
3. 

---

### 列表嵌套

1. 第一项：
    	- 嵌套1
    	- 嵌套2
2. 第二项：
    - 第二项嵌套的第一个元素
    - 第二项嵌套的第二个元素

---

### 区块

> 最外层
>
> > 第一层
> >
> > > 第二层

> 区块中使用列表
>
> 1. 第一项
> 2. 第二项
> 3. 第三项
>    + 第一项
>    + 第二项

#### 列表中使用区块

* 第一项

  >wrf

* 第二项

  > WRF

---

### 代码

`printf`函数

```c
#include <stdio.h>
int main()
{
    printf("Hello World");
    return 0;
}
```

### 链接

这是一个链接 [北航校园网](gw.buaa.edu.cn)

<www.baidu.com>

[Google][1]

[Youtube][you]

[1]: www.google.com
[you]: www.youtube.com

---

### 图片

![alt 美女](D:\Desktop\照片\Pictures\Saved Pictures\adaeac9489b44c2fb21110d74e98f572~tplv-dy-aweme-images_q75.webp "章若楠")

---

### 表格

| 左对齐 | 右对齐 | 居中对齐 |
| ------ | ------ | -------- |
|        |        |          |
|        |        |          |

---

### 公式

$$ f(x)=sin(x)+12 $$




$$
\begin{Bmatrix}
   a & b \\
   c & d
\end{Bmatrix}
$$
$$
\begin{CD}
   A @>a>> B \\
@VbVV @AAcA \\
   C @= D
\end{CD}
$$

---

### 画图

**1. 横向流程图源码格式：**

```mermaid
graph LR
A[方形] -->B(圆角)
    B --> C{条件a}
    C -->|a=1| D[结果1]
    C -->|a=2| E[结果2]
    F[横向流程图]
```

**2、竖向流程图源码格式：**

```mermaid
graph TD
A[方形] --> B(圆角)
    B --> C{条件a}
    C --> |a=1| D[结果1]
    C --> |a=2| E[结果2]
    F[竖向流程图]
```

**3、标准流程图源码格式：**

```flow
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st->op->cond
cond(yes)->io->e
cond(no)->sub1(right)->op
```

**4、标准流程图源码格式（横向）：**

```flow
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st(right)->op(right)->cond
cond(yes)->io(bottom)->e
cond(no)->sub1(right)->op
```

**5、UML时序图源码样例：**

```sequence
对象A->对象B: 对象B你好吗?（请求）
Note right of 对象B: 对象B的描述
Note left of 对象A: 对象A的描述(提示)
对象B-->对象A: 我很好(响应)
对象A->对象B: 你真的好吗？
```

**6、UML时序图源码复杂样例：**

```sequence
Title: 标题：复杂使用
对象A->对象B: 对象B你好吗?（请求）
Note right of 对象B: 对象B的描述
Note left of 对象A: 对象A的描述(提示)
对象B-->对象A: 我很好(响应)
对象B->小三: 你好吗
小三-->>对象A: 对象B找我了
对象A->对象B: 你真的好吗？
Note over 小三,对象B: 我们是朋友
participant C
Note right of C: 没人陪我玩
```

**7、UML标准时序图样例：**

```mermaid
%% 时序图例子,-> 直线，-->虚线，->>实线箭头
  sequenceDiagram
    participant 张三
    participant 李四
    张三->王五: 王五你好吗？
    loop 健康检查
        王五->王五: 与疾病战斗
    end
    Note right of 王五: 合理 食物 <br/>看医生...
    李四-->>张三: 很好!
    王五->李四: 你怎么样?
    李四-->王五: 很好!
```

**8、甘特图样例：**

```mermaid
%% 语法示例
        gantt
        dateFormat  YYYY-MM-DD
        title 软件开发甘特图
        section 设计
        需求                      :done,    des1, 2014-01-06,2014-01-08
        原型                      :active,  des2, 2014-01-09, 3d
        UI设计                     :         des3, after des2, 5d
    未来任务                     :         des4, after des3, 5d
        section 开发
        学习准备理解需求                      :crit, done, 2014-01-06,24h
        设计框架                             :crit, done, after des2, 2d
        开发                                 :crit, active, 3d
        未来任务                              :crit, 5d
        耍                                   :2d
        section 测试
        功能测试                              :active, a1, after des3, 3d
        压力测试                               :after a1  , 20h
        测试报告                               : 48h
```