`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:10:53 12/15/2023 
// Design Name: 
// Module Name:    mips 
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
module mips(
    input clk,                    // 时钟信号
    input reset,                  // 同步复位信号
    input interrupt,              // 外部中断信号
    output [31:0] macroscopic_pc, // 宏观 PC

    output [31:0] i_inst_addr,    // IM 读取地址（取指 PC）
    input  [31:0] i_inst_rdata,   // IM 读取数据

    output [31:0] m_data_addr,    // DM 读写地址
    input  [31:0] m_data_rdata,   // DM 读取数据
    output [31:0] m_data_wdata,   // DM 待写入数据
    output [3 :0] m_data_byteen,  // DM 字节使能信号

    output [31:0] m_int_addr,     // 中断发生器待写入地址
    output [3 :0] m_int_byteen,   // 中断发生器字节使能信号

    output [31:0] m_inst_addr,    // M 级 PC

    output w_grf_we,              // GRF 写使能信号
    output [4 :0] w_grf_addr,     // GRF 待写入寄存器编号
    output [31:0] w_grf_wdata,    // GRF 待写入数据

    output [31:0] w_inst_addr     // W 级 PC
);

	wire [31:0] br_in, br_addr, br_wd, tc0, tc1, tc_in, tc_addr;
	wire br_we, tc0_we, tc1_we, IRQ0, IRQ1;
	
	CPU cpu (
    .clk(clk), 
    .reset(reset), 
    .interrupt(interrupt), 
    .IRQ0(IRQ0), 
    .IRQ1(IRQ1), 
    .i_inst_addr(i_inst_addr), 
    .i_inst_rdata(i_inst_rdata), 
    .m_data_rdata(m_data_rdata), 
    .m_data_addr(m_data_addr), 
    .m_data_wdata(m_data_wdata), 
    .m_data_byteen(m_data_byteen), 
    .m_inst_addr(m_inst_addr), 
    .macroscopic_pc(macroscopic_pc), 
    .m_int_byteen(m_int_byteen), 
    .m_int_addr(m_int_addr), 
    .br_in(br_in), 
    .br_wd(br_wd), 
    .br_addr(br_addr), 
    .br_we(br_we), 
    .w_grf_we(w_grf_we), 
    .w_grf_addr(w_grf_addr), 
    .w_grf_wdata(w_grf_wdata), 
    .w_inst_addr(w_inst_addr)
    );
	
	Bridge br (
    .br_in(br_in), 
    .br_we(br_we), 
    .br_addr(br_addr), 
    .br_wd(br_wd), 
    .tc0(tc0), 
    .tc1(tc1), 
    .tc0_we(tc0_we), 
    .tc1_we(tc1_we), 
    .tc_in(tc_in), 
    .tc_addr(tc_addr)
    );
	
	 TC Tc0 (
    .clk(clk), 
    .reset(reset), 
    .Addr(tc_addr[31:2]), 
    .WE(tc0_we), 
    .Din(tc_in), 
    .Dout(tc0), 
    .IRQ(IRQ0)
    );
	 
	  TC Tc1 (
    .clk(clk), 
    .reset(reset), 
    .Addr(tc_addr[31:2]), 
    .WE(tc1_we), 
    .Din(tc_in), 
    .Dout(tc1), 
    .IRQ(IRQ1)
    );

endmodule
