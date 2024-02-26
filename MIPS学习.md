## MIPS学习

### Hello World

```MIPS
.data
str: .asciiz    "Hello World"

.text
la  $a0, str
li  $v0, 4
syscall

li  $v0, 10
syscall             
```

> ```MIPS
> # 分析
> .data	#代表变量的声明和分配从这里开始
> str: .asciiz    "Hello World"	
> # MIPS 汇编语言中的一条指令，用于定义一个字符串常量。
> # 在这里，str 是一个标签（label），用于标识这个字符串常量的地址。
> # .asciiz 是一个伪指令，用于定义一个以 null 结尾的 ASCII 字符串。
> # "Hello World" 是要定义的字符串常量。
> # 因此，这条指令的作用是将字符串常量 "Hello World" 存储在内存中，并将其地址与标签 str 关联起# 来，以便在程序中可以通过 str 来引用该字符串。这样，在需要使用这个字符串的地方，可以通过加载  # str 的地址，将该字符串的地址传递给系统调用或其他指令。
> 
> .text	#代表程序从这里开始
> 
> la  $a0, str	
> #la是MIPS汇编指令中的一个伪指令，用于将一个标签（label）的地址加载到寄存器中。$a0是一个MIPS寄存器，用于传递参数，通常在系统调用中用于传递字符串的地址。
> str是一个标签，用于表示某个字符串的地址。
> # 因此，la $a0, str的作用是将标签str所表示的字符串的地址加载到寄存器$a0中。这样，寄存器$a0中就存储了字符串的地址，可以在后续的系统调用中使用。
> 
> li  $v0, 4	
> # li 是 MIPS 汇编指令中的伪指令之一，用于将一个立即数（immediate value）加载到寄存器中。
> # $v0 是一个 MIPS 寄存器，通常用于保存系统调用的函数号。
> # 因此，li $v0, 5 的作用是将立即数 5 加载到寄存器 $v0 中。这样，寄存器 $v0 中就存储了函数号 # 5，可以在后续的系统调用中使用。
> 
> syscall
> syscall是一个MIPS汇编指令，用于发起系统调用（system call）。
> 系统调用允许程序与操作系统内核进行交互，执行一些需要特权级别或操作系统提供的功能，例如文件读写、进程创建等。
> 在MIPS汇编中，使用syscall指令时需要将要调用的系统调用号放入寄存器$V0中，并根据系统调用的需要，在其他寄存器中设置参数。然后执行syscall指令，就会触发相应的系统调用。
> 以下是一种常见的使用syscall的流程：
> 在$V0寄存器中设置系统调用号。
> 在$A0等其他寄存器中设置系统调用所需的参数。
> 执行syscall指令。
> 系统调用的返回值可能会被存储在$V0寄存器中（例如文件读写的返回值是文件操作的结果），程序可以根据需要使用返回值。
> 不同的操作系统和硬件平台有不同的系统调用号和参数约定，因此具体使用时需要参考相应的系统调用文档和平台特定的约定。
> 以下是一些常见的系统调用号：
> 1: 打印整数
> 4: 打印字符串
> 5: 读取整数
> 8: 读取字符串
> 9: 堆分配内存
> 10: 退出程序
> 需要根据具体情况使用相应的系统调用号和参数进行系统调用。
> 
> li  $v0, 10
> syscall           
> ```



### 循环

```MIPS
# 下面以一个简单题目为例，说明在 MIPS 中如何使用循环。
# 题目内容: 输入一个数n，输出1+2+3 + ... +n (保证n和输出结果都在 nt 的范围之内)
.text
li  $v0,5
syscall                 # 输入一个整数，输入的数存到 $v0 中
move $s0, $v0           # 赋值，$s0 = $v0
li  $s1, 0              # $s1 用于存储累加的值，$s1 = 0
li  $t0, 1              # $t0 是循环变量

loop:
bgt $t0, $s0, loop_end  # 这里用了一个扩展指令 bgt,当 $t0 > $s0 的时候跳转到 loop_end
add $s1, $s1, $t0       # $s1 = $s1 + $t0
addi $t0, $t0, 1        # $t0 = $t0 + 1
j   loop                # 无条件跳转到 loop 标签

loop_end:
move $a0, $s1           # 赋值，$a0 = $s1
li  $v0, 1              # $v0 = 1，在 syscall 中会输出 $a0 的值
syscall         
li  $v0,10              # $v0 = 10
syscall                 # 结束程序          
```

##### move用法

* move $s0, $v0` 是一个MIPS汇编指令，用于将一个寄存器的值复制到另一个寄存器中。

  `$s0` 和 `$v0` 都是MIPS寄存器。

  这条指令的作用是将寄存器 `$v0` 中的值复制到 `$s0` 中。通过这个指令，将 `$v0` 寄存器中的值赋给 `$s0` 寄存器。

  `move` 实际上是 `add` 指令的一个别名。由于 MIPS 架构的特性，采用了延迟槽指令的设计，在 `add` 和 `sub` 指令后的指令会延迟一个周期执行。为了避免延迟槽的影响，MIPS 提供了 `move` 伪指令，其效果与 `add` 相同，但没有延迟槽的问题。

  所以，`move $s0, $v0` 其实等同于 `add $s0, $v0, $zero`，其中 `$zero` 是一个常量值寄存器，值始终为0。

##### loop用法

* `loop:` 是一个MIPS汇编语言中的标签（label），用于标识一个循环的起始位置。

  在程序中可以使用标签来创建循环结构，以便在程序中可以通过跳转指令（例如 `j`、`beq`、`bne` 等）无条件或条件性地跳转到标签处继续执行代码，从而形成循环。

  通过使用标签，在循环的尾部可以使用跳转指令来回到循环的起始位置，从而实现重复执行一段代码的功能。例如：

  ```
  loop:
    # 循环体的代码
  
    # 条件判断
    # 如果满足条件，跳转回循环起始位置
    beq $t0, $t1, loop
    # beq $t0, $t1, loop 是一个MIPS汇编指令，表示当寄存器 $t0 的值等于寄存器 $t1 的值 
    # 时，跳转到标签 loop 处执行代码。
  
    # 循环结束后的代码
  ```

  在这段代码中，`loop` 标签标识了循环的起始位置。在循环体执行完毕后，通过 `beq` 指令进行条件判断，如果条件满足，则跳转回 `loop` 标签所在的位置，从而重复执行循环体。如果条件不满足，则继续执行循环后的代码。



### MIPS中使用数组

#### 一维数组

```MIPS
# 下面以一个简单题目为例，说明在MIPS中如何使用数组
题目内容:输入一个整数n(2<=n<=10)，接下来n行，每行一个整数(在int范围内)，在输出的时候先输出 The numbers are:，然后把这n 个整数按照输入顺序输出，两个数字中间一个空格，行末可以有空格.
样例输入:
4
2
3
1
4
样例输出:
The numbers are: 2 3 1 4
#

.data
array: .space 40           # 存储这些数需要用到数组，数组需要使用 10 * 4 = 40 字节
                           # 一个 int 整数需要占用 4 个字节，需要存储 10 个 int 整数
                           # 因此，array[0] 的地址为 0x00，array[1] 的地址为 0x04
                           # array[2] 的地址为 0x08，以此类推。

str:   .asciiz "The numbers are:\n"
space: .asciiz " "

.text
li $v0,5
syscall                    # 输入一个整数
move $s0, $v0              # $s0 is n
li $t0, 0                  # $t0 循环变量

loop_in:
beq $t0, $s0, loop_in_end  # $t0 == $s0 的时候跳出循环
li $v0, 5
syscall                    # 输入一个整数
sll $t1, $t0, 2            # $t1 = $t0 << 2，即 $t1 = $t0 * 4
sw $v0, array($t1)         # 把输入的数存入地址为 array + $t1 的内存中
addi $t0, $t0, 1           # $t0 = $t0 + 1
j loop_in                  # 跳转到 loop_in

loop_in_end:
la $a0, str
li $v0, 4
syscall                    # 输出提示信息
li $t0, 0
loop_out:
beq $t0, $s0, loop_out_end
sll $t1, $t0, 2            # $t1 = $t0 << 2，即 $t1 = $t0 * 4
lw $a0, array($t1)         # 把内存中地址为 array + $t1 的数取出到 $a0 中
li $v0, 1
syscall                    # 输出 $a0
la $a0, space
li $v0, 4
syscall                    # 输出一个空格
addi $t0, $t0, 1
j loop_out

loop_out_end:
li $v0, 10
syscall                    # 结束程序
```

##### sw用法

* sw $v0, array($t1)         # 把输入的数存入地址为 array + $t1 的内存中

##### lw用法

* lw $a0, array($t1)         # 把内存中地址为 array + $t1 的数取出到 $a0 中



#### 二维数组

```MIPS
下面再以一个简单题目为例，说明在MIPS中如何使用二维数组
题目内容: 输入两个数m和n(1<=m<=8,1<=n<=8)，代表有-个m行n列的矩阵，接下来m*n行每行一个int 范围内的整数，依次输入矩阵的元素，最后输出这个矩阵(每两个数字中间一个空格，行末可以有多余空格，最后可以有多余回车)
样例输入：
2
3
1
2
3
4
5
6
样例输出：
1 2 3 
4 5 6 

.data
matrix: .space  256             # int matrix[8][8]   8*8*4 字节
                                # matrix[0][0] 的地址为 0x00，matrix[0][1] 的地址为0x04，……
                                # matrix[1][0] 的地址为 0x20，matrix[1][1] 的地址为 0x24，……
                                # ……
str_enter:  .asciiz "\n"
str_space:  .asciiz " "

# 这里使用了宏，%i 为存储当前行数的寄存器，%j 为存储当前列数的寄存器
# 把 (%i * 8 + %j) * 4 存入 %ans 寄存器中
.macro  getindex(%ans, %i, %j)
    sll %ans, %i, 3             # %ans = %i * 8
    add %ans, %ans, %j          # %ans = %ans + %j
    sll %ans, %ans, 2           # %ans = %ans * 4
.end_macro

.text
li  $v0, 5
syscall
move $s0, $v0                   # 行数
li  $v0, 5
syscall
move $s1, $v0                   # 列数
# 这里使用了循环嵌套
li  $t0, 0                      # $t0 是一个循环变量

in_i:                           # 这是外层循环
beq $t0, $s0, in_i_end
li  $t1, 0                      # $t1 是另一个循环变量
in_j:                           # 这是内层循环
beq $t1, $s1, in_j_end
li  $v0, 5
syscall                         # 注意一下下面几行，在 Execute 页面中 Basic 列变成了什么
getindex($t2, $t0, $t1)         # 这里使用了宏，就不用写那么多行来算 ($t0 * 8 +syscallt1) * 4 了
sw  $v0, matrix($t2)            # matrix[$t0][$t1] = $v0
addi $t1, $t1, 1
j   in_j
in_j_end:
addi $t0, $t0, 1
j   in_i
in_i_end:
# 这里使用了循环嵌套，和输入的时候同理
li  $t0, 0

out_i:
beq $t0, $s0, out_i_end
li  $t1, 0
out_j:
beq $t1, $s1, out_j_end
getindex($t2, $t0, $t1)
lw  $a0, matrix($t2)            # $a0 = matrix[$t0][$t1]
li  $v0, 1
syscall
la  $a0, str_space
li  $v0, 4
syscall                         # 输出一个空格
addi $t1, $t1, 1
j   out_j
out_j_end:
la  $a0, str_enter
li  $v0, 4
syscall                         # 输出一个回车
addi $t0, $t0, 1
j   out_i

out_i_end:
li  $v0, 10
syscall
```

##### 宏

* 不带参数的宏定义：

  ​		.macro macro_name

  ​		代码... 

  ​		.end_macro

* 带参数的宏：

  ​		.macro macro_name(%parameter1, %parameter2, ...) 

  ​		代码...

  ​		.end_macro

* 在汇编程序中，还有一种和C语言中 #define 类似的宏定义，一般用于常量的定义上，那就是 `.eqv`。`.eqv` 用法如下：

  ```
  .eqv EQV_NAME string
  ```

  汇编器会把所有 EQV_NAME 的地方替换成 string，这可以用来定义一些常量。

### 计算Fibonacci 数

```MIPS
# 下面给出的是求前 12 个 Fibonacci 数的汇编程序。后面将以此为例，进行程序解析。

.data
fibs: .space   48           # "array" of 12 words to contain fib values
size: .word  12             # size of "array"
space:.asciiz  " "          # space to insert between numbers
head: .asciiz  "The Fibonacci numbers are:\n"

.text
la   $t0, fibs              # load address of array
la   $t5, size              # load address of size variable
lw   $t5, 0($t5)            # load array size
li   $t2, 1                 # 1 is first and second Fib. number
sw   $t2, 0($t0)            # F[0] = 1
sw   $t2, 4($t0)            # F[1] = F[0] = 1
addi $t1, $t5, -2           # Counter for loop, will execute (size-2) times

loop:
lw   $t3, 0($t0)            # Get value from array F[n]
lw   $t4, 4($t0)            # Get value from array F[n+1]
add  $t2, $t3, $t4          # $t2 = F[n] + F[n+1]
sw   $t2, 8($t0)            # Store F[n+2] = F[n] + F[n+1] in array
addi $t0, $t0, 4            # increment address of Fib. number source
addi $t1, $t1, -1           # decrement loop counter
bgtz $t1, loop              # repeat if not finished yet.
la   $a0, fibs              # first argument for print (array)
add  $a1, $zero, $t5        # second argument for print (size)
jal  print                  # call print routine.
li   $v0, 10                # system call for exit
syscall                     # we are out of here.

print:
add  $t0, $zero, $a0        # starting address of array
add  $t1, $zero, $a1        # initialize loop counter to array size
la   $a0, head              # load address of print heading
li   $v0, 4                 # specify Print String service
syscall                     # print heading

out:
lw   $a0, 0($t0)            # load fibonacci number for syscall
li   $v0, 1                 # specify Print Integer service
syscall                     # print fibonacci number
la   $a0, space             # load address of spacer for syscall
li   $v0, 4                 # specify Print String service
syscall                     # output string
addi $t0, $t0, 4            # increment address
addi $t1, $t1, -1           # decrement loop counter
bgtz $t1, out               # repeat if not finished
jr   $ra                    # return

1~7 行：变量声明与分配(伪指令)

8~14 行：初始化与寄存器分配

16~28 行：循环计算并保存 Fibonacci 数

30~47 行：输出提示语句和 Fibonacci 数
```

##### .word

* `size: .word 12` 是一个MIPS汇编指令，用于定义一个字（word）大小的数据并初始化为值 12。

  `size` 是一个标签，用于标识该数据。

  `.word` 是一个伪指令，用于定义一个字大小（32位）的数据。

  `12` 是要存储在内存中的初始化值。

  因此，这条指令的作用是在内存中分配一个字的空间，并将值 12 存储在该内存中。这样，在后续的代码中可以使用 `size` 标签引用该数据，例如通过 `lw` 指令将它加载到寄存器中。

##### .space

* `fibs: .space 48` 是一个MIPS汇编指令，用于分配一块连续的内存空间，大小为 48 字节。

  `fibs` 是一个标签，用于标识这块内存空间。

  `.space` 是一个伪指令，用于分配指定大小的连续内存空间。

  `48` 是要分配的内存空间的字节数，即 4 字节字大小的数量。

  因此，这条指令的作用是在内存中分配一块连续的内存空间，大小为 48 字节，这样在后续的代码中可以使用 `fibs` 标签引用这块内存空间。可以通过加载和存储指令（如 `lw`、`sw`）在这块内存空间中进行读写操作。

##### bgtz

* `bgtz $t1, loop` 是一个 MIPS 汇编指令，用于有条件地跳转到指定的标签。

  `$t1` 是一个 MIPS 寄存器，用于存储临时数据或其他数据。

  `loop` 是一个标签，通常用于标识一个代码块或循环的起始位置。

  这条指令的作用是比较寄存器 `$t1` 中的值和零，并根据结果进行条件性跳转。如果 `$t1` 的值大于零，则跳转到标签 `loop` 处执行代码。如果 `$t1` 的值小于等于零，则继续执行下一条指令。

  该指令主要用于条件分支，以根据比较结果来决定是否跳转到指定的标签继续执行代码。在这个例子中，如果 `$t1` 的值大于零，则会跳转到 `loop` 标签处，从而实现有条件地执行循环。

##### $zero

* `add $a1, $zero, $t5` 是一个MIPS汇编指令，用于将一个寄存器的值复制到另一个寄存器中。

  `$a1` 和 `$t5` 是MIPS寄存器。

  这条指令的作用是将寄存器 `$t5` 中的值复制到 `$a1` 中。通过这个指令，将 `$t5` 寄存器中的值赋给 `$a1` 寄存器。

  `add` 指令用于将两个寄存器的值相加，并将结果存储在目标寄存器中。在这个指令中，`$zero` 是一个伪寄存器，用于保存常量值 0，作为加法的第一个操作数。

  所以，`add $a1, $zero, $t5` 其实是将 `$t5` 的值复制到 `$a1` 中，相当于 `$a1 = $t5`。

##### jr

* `jr $ra` 是一个MIPS汇编指令，用于无条件跳转到 `$ra` 寄存器中存储的地址，即函数返回地址。

  `$ra` 是一个 MIPS 寄存器，用于保存函数返回地址。

  这条指令的作用是将程序的控制权无条件地转移到 `$ra` 寄存器中保存的地址，从而实现函数的返回操作。通常在函数的结尾处会使用这条指令来返回到调用函数的位置。

  `jr` 指令可以用于实现跳转、函数返回等控制流操作。在这个例子中，`jr $ra` 会将程序跳转到 `$ra` 寄存器中保存的地址，从而返回到函数的调用者。

### 控制流

以选择排序为例来了解MIPS

##### c语言选择排序

```C
void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
void selection_sort(int *a,int n){
    for(int i = 0; i < n; i++){
        int index = i;
        for(int j = i+1;j < n; j++){
            if(a[j] < a[index]){
                index = j;
            }
        }
        swap(&a[index],&a[i]);
    }
}
```



##### if_else

```MIPS
.data
	s1: .asciiz "t1>t2"
	s2: .asciiz "t1<t2"
.text
	li $t1, 300
	li $t2, 100
	slt $t3, $t2, $t1
	beq $t3, $zero, if_else
	nop
	
	la $a0, s1
	li $v0, 4
	syscall
	j if_end
	nop
	
	if_else:
		la $a0, s2
		li $v0, 4
		syscall
		
	if_end:
	
```





##### for循环

```MIPS
.text
li $t1, 100
li $t2, 0
for_begin:
	slt $t3, $t2, $t1
	beq $t3, $zero, for_end
	nop
	
	#################
	*   statement	*
	#################
	
	addi $t2, $t2, 1
	j for_begin
	nop
for_end:
```

##### input and output

```MIPS
.text

input:
	la $a0, message_input_n
	li $v0, 4
	syscall
	
	li $v0, 5
	syscall
	move $t0, $v0
	
	li $t1, 0
	for_1_begin:
		slt $t2, $t1, $t0
		beq $t2, $zero, for_1_end
		nop
		
		la $t2, array
		li $t3, 4
		mult $t3, $t1
		mflo $t3
		addu $t2, $t2, $t3
		
		la $a0, message_input_array
		li %v0, 4
		syscall
		
		li $v0, 5
		syscall
		
		sw $v0, 0($t2)
		
		addi $t1, $t1, 1
		j for_1_begin
		nop
	for_1_end:
	move $v0, $t0
#	jr $ra
	nop
move $a0, $v0

output:
	move $t0, $a0
	
	la $a0, message_output_array
	li $v0, 4
	syscall
	
	li $t1, 0
	for_2_begin:
		slt $t2, $t1, $t0
		beq $t2, $zero, for_2_end
		nop
		
		la $t2, array
		li $t3, 4
		mult $t3, $t1
		mflo $t3
		addu $t2, $t2, $t3
		
		lw $a0, 0($t2)
		li $v0, 1
		syscall
		
		la $a0, space
		li $v0, 4
		syscall
		
		addi $t1, $t1, 1
		j for_2_begin
		nop
	for_2_end:
#	jr $ra
	nop
```

##### sort

```MIPS
sort:
	addiu $sp, $sp, -32
	move $t0, $a0
	li $t1, 0
	for_4_begin:
		slt $t2, $t1, $t0
		beq $t2, $zero, for_4_end
		nop
		
		la $t2, array
		li $t3, 4
		mult $t1, $t3
		mflo $t3
		addu $t2, $t2, $t3
		
		move $a0, $t0
		move $a1, $t1
		
		sw $t2, 28($sp)
		sw $t1, 24($sp)
		sw $t0, 20($sp)
		sw $ra, 16($sp)
		
		jal findmin
		nop
		
		lw $ra, 16($sp)
		lw $t0, 20($sp)
		lw $t1, 24($sp)
		lw $t2, 28($sp)
		
		lw $t3, 0($v0)
		lw $t4, 0($t2)
		sw $t3, 0($t2)
		sw $t4, 0($v0)
		
		addi $t1, $t1, 1
		j for_4_begin
		nop
	for_4_end:
	addiu $sp, $sp, 32
	jr $ra
	nop
```

```MIPS
findmin:
	la $t0, array
	sll $a0, $a0, 2
	subi $a0, $a0, 4
	addu $t0, $t0, $a0
	
	lw $t1, 0($t0)
	move $t2, $t0
	
	move $t3, $t0
	la $t0, array
	sll $a1, $a1, 2
	addu $t0, $t0, $a1
	for_3_begin:
		sge $t4, $t3, $t0
		beq $t4, $zero, for_3_end
		nop
		
		lw $t5, 0($t3)
		
		slt $t6, $t5, $t1
		beq $t6, $zero, if_1_else
			nop
			move $t1, $t5
			move $t2, $t3
			j if_1_end
			nop
		if_1_else:
		if_1_end:
		
		subi $t3, $t3, 4
		j for_3_begin
		nop
	for_3_end:
	move $v0, $t2
	jr $ra
	nop
```

### 函数调用

> - 函数是一个**代码块**，可以由指定语句调用，并且在执行完毕后返回调用语句。
> - 函数通过传参，可以实现代码的**复用**。
> - 函数只能通过返回值等有限手段对函数外造成影响。
> - 函数里依然可以**嵌套调用**函数。