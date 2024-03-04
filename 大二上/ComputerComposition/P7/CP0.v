`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    09:30:05 12/14/2023 
// Design Name: 
// Module Name:    CP0 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
//`define IM SR[15:10] //分别对应六个外部中断，相应位置 1 表示允许中断，置 0 表示禁止中断。这是一个被动的功能，只能通过 mtc0 这个指令修改，通过修改这个功能域，我们可以屏蔽一些中断。
//`define EXL SR[1] //任何异常发生时置位，这会强制进入核心态（也就是进入异常处理程序）并禁止中断。
//`define IE SR[0] //全局中断使能，该位置 1 表示允许中断，置 0 表示禁止中断。
//`define BD Cause[31] //当该位置 1 的时候，EPC 指向当前指令的前一条指令（一定为跳转），否则指向当前指令。
//`define IP Cause[15:10] //为 6 位待决的中断位，分别对应 6 个外部中断，相应位置 1 表示有中断，置 0 表示无中断，将会每个周期被修改一次，修改的内容来自计时器和外部中断。
//`define ExcCode Cause[6:2] //异常编码，记录当前发生的是什么异常。
module CP0(
	input clk,
	input reset,
	input we, //写使能信号。
	input [4:0] CP0reg,//寄存器地址。
	input [31:0] CP0in,//CP0 写入数据。
	output [31:0] CP0out,//CP0 读出数据。
	input [31:0] vpc,//受害 PC。
	input BDin,//是否是延迟槽指令。
	input [4:0] ExcCodeIn,//记录异常类型。
	input [5:0] HWInt,//输入中断信号。
	input eret,//用来复位 EXL。
	output reg [31:0] EPCout,//EPC 的值。
	output req//进入处理程序请求。
    );
	reg [5:0] IM;
	reg EXL, IE, BD;
	reg [5:0] IP;
	reg [4:0] ExcCode;
	wire IntReq = (ExcCodeIn != 0);
	wire ExtReq = (|(HWInt[5:0] & IM[5:0])) & IE;
	
	assign req = (IntReq | ExtReq) & !EXL;
	
	assign CP0out = (CP0reg == 5'd12) ? {16'b0, IM, 8'b0, EXL, IE} :
						 (CP0reg == 5'd13) ? {BD, 15'b0, IP, 3'b0, ExcCode, 2'b0} :
						 (CP0reg == 5'd14) ? EPCout : 0;
						 
	always @(posedge clk) begin
		if (reset) begin
			IM <= 0;
			EXL <= 0;
			IE <= 0;
			BD <= 0;
			IP <= 0;
			ExcCode <= 0;
			EPCout <= 32'h00003000;
		end
		else if (eret) begin
			EXL <= 0;
		end
		else if (req) begin
			BD <= BDin;
			EPCout <= (BDin) ? vpc - 4 : vpc;
			ExcCode <= (ExtReq) ? 0 : ExcCodeIn;
			EXL <= 1;
		end
		else if (we) begin
			if (CP0reg == 5'd12) begin
				IM <= CP0in[15:10];
				EXL <= CP0in[1];
				IE <= CP0in[0];
			end
			else if (CP0reg == 5'd14) begin
				EPCout <= CP0in;
			end
		end
		
		if (!reset) begin
			IP <= HWInt;
		end
	end
endmodule
