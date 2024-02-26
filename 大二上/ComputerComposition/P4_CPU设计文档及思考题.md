## P4

### CPU设计文档及思考题

#### 设计草稿

顶层为mips，mips由模块Datapath和Controller组成，Datapath由PC、NPC、IM、GRF、DM、ALU组成。

##### mips

| 端口名称 | 方向 | 位宽 | 描述         |
| -------- | ---- | ---- | ------------ |
| clk      | I    | 1    | 时钟信号     |
| reset    | I    | 1    | 同步复位信号 |

###### Datapath

| 端口名称 | 方向 | 位宽 | 描述                             |
| -------- | ---- | ---- | -------------------------------- |
| add      | I    | 1    | 判断ALU是否进行加法              |
| cin      | I    | 1    | 判断ALU是否进行减法              |
| RegC     | I    | 1    | 判断GRF写入数据的地址为rs还是rd  |
| beq      | I    | 1    | 判断是否有beq信号                |
| WD       | I    | 1    | DM是否输出、GRF写入值是否为DMout |
| sw       | I    | 1    | DM是否写入                       |
| lui      | I    | 1    | 判断ALU是否进行lui计算           |
| aluop    | I    | 1    | 判断ALU是否进行ori计算           |
| jr       | I    | 1    | 判断NPC是否输出RegRs             |
| jal      | I    | 1    | 判断是否有jal信号                |
| EXTop    | I    | 1    | 判断0扩展还是符号扩展            |
| Bsel     | I    | 1    | 判断是否输出imm                  |
| we       | I    | 1    | 判断GRF是否写入                  |
| clk      | I    | 1    | 时钟信号                         |
| reset    | I    | 1    | 同步复位信号                     |
| instr    | O    | 32   | 输出命令                         |

###### Controller

Controller分为两部分，“AND”部分识别指令，“OR”部分输出命令信号。

| 端口名称 | 方向 | 位宽 | 描述                         |
| -------- | ---- | ---- | ---------------------------- |
| instr    | I    | 32   | 指令                         |
| jr       | O    | 1    | jr信号                       |
| aluop    | O    | 1    | 判断ALU计算类型              |
| EXTop    | O    | 1    | 判断立即数扩展类型           |
| cin      | O    | 1    | 判断加减法类型               |
| Bsel     | O    | 1    | 判断输出立即数还是寄存器的值 |
| we       | O    | 1    | 判断输出是否输入             |
| RegC     | O    | 1    | 判断输入到rt还是rd           |
| lui      | O    | 1    | 判断是否执行lui操作          |
| WD       | O    | 1    | 判断DM是否输出               |
| beq      | O    | 1    | 判断是否执行beq操作          |
| sw       | O    | 1    | 判断DM是否输入               |
| add      | O    | 1    | add信号                      |
| jal      | O    | 1    | jal信号                      |

#### 思考题

> 1、阅读下面给出的 DM 的输入示例中（示例 DM 容量为 4KB，即 32bit × 1024字），根据你的理解回答，这个 addr 信号又是从哪里来的？地址信号 addr 位数为什么是 [11:2] 而不是 [9:0] ？

addr信号是由ALU输出的值决定的，因为addr在DM中是字存储的，一个字等于四个字节，所以地址要乘以四，即从第2位开始取地址。

> 2、思考上述两种控制器设计的译码方式，给出代码示例，并尝试对比各方式的优劣。

```
第一种方法：指令对应的控制信号如何取值
// AND
	assign nop = (opcode == 0 && funct == 0);
	assign add1 = (opcode == 0 && funct == 6'b100000);
	assign sub = (opcode == 0 && funct == 6'b100010) ? 1 : 0;
	assign beq1 = (opcode == 6'b000100) ? 1 : 0;
	assign lw = (opcode == 6'b100011) ? 1 : 0;
	assign sw1 = (opcode == 6'b101011) ? 1 : 0;
	assign lui1 = (opcode == 6'b001111) ? 1 : 0;
	assign ori = (opcode == 6'b001101) ? 1 : 0;
	assign jr1 = (opcode == 0 && funct == 6'b001000) ? 1 : 0;
	assign jal1 = (opcode == 6'b000011) ? 1 : 0;
	// OR
	assign aluop = ori;
	assign sw = sw1;
	assign lui = lui1;
	assign jr = jr1;
	assign jal = jal1;
	assign beq = beq1;
	assign WD = lw;
	assign EXTop = sw1 | lw;
	assign cin = sub;
	assign Bsel = ori | sw1 | lw | lui1;
	assign we = jal1 | add1 | sub | lw | lui1 | ori;
	assign RegC = add1 | sub;
	assign add = add1 | sw1 | lw;
```

```
第二种方法：控制信号每种取值所对应的指令
if (WD == 1) {
	opcode = 6'b100011;
}
```

第一种方法通过opcode和funct的取值可以得到控制信号，适用于指令已知的时候；第二种方法通过控制信号可得到opcode和funct的取值，适用于已知控制信号的情况。

> 3、在相应的部件中，复位信号的设计都是**同步复位**，这与 P3 中的设计要求不同。请对比**同步复位**与**异步复位**这两种方式的 reset 信号与 clk 信号优先级的关系。

同步复位是在clk信号上升沿时再进行复位，而异步复位是不论clk信号是否处于上升沿都进行复位

> 4、C 语言是一种弱类型程序设计语言。C 语言中不对计算结果溢出进行处理，这意味着 C 语言要求程序员必须很清楚计算结果是否会导致溢出。因此，如果仅仅支持 C 语言，MIPS 指令的所有计算指令均可以忽略溢出。 请说明为什么在忽略溢出的前提下，addi 与 addiu 是等价的，add 与 addu 是等价的。提示：阅读《MIPS32® Architecture For Programmers Volume II: The MIPS32® Instruction Set》中相关指令的 Operation 部分。

addi和add在不忽略溢出时都会对结果进行判断是否溢出，溢出则输出异常，而addiu和addu则不会判断是否溢出，直接输出结果。因此，在忽略溢出时，add和addu、addi和addiu是等价的。