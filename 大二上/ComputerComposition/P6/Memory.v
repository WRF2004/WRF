`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    08:59:54 11/16/2023 
// Design Name: 
// Module Name:    Memory 
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
module Memory(
    input [31:0] m_aluout,
    input [31:0] m_instr,
    input [31:0] m_pc,
	 input [31:0] m_out,
    input [31:0] FW_m_d,
	 
	 input [31:0] m_data_rdata, //DMout
	 
	 output [31:0] m_data_addr, // m_aluout
	 output [31:0] m_data_wdata, // FW_m_d
	 output [31:0] m_inst_addr, // m_pc
	 output [3:0] m_data_byteen, // enable 
	 
	 output [31:0] mw_out
    );
	 wire WD;
	 wire [2:0] Op;
	 wire [31:0] Dout;
	assign m_data_addr = m_aluout;
	assign m_data_wdata = (m_data_byteen == 4'b1111) ? FW_m_d : 
								 ((m_data_byteen == 4'b1100) || (m_data_byteen == 4'b0011)) ? {2{FW_m_d[15:0]}} :
								 ((m_data_byteen == 4'b0001) || (m_data_byteen == 4'b0010) || (m_data_byteen == 4'b0100) || (m_data_byteen == 4'b1000)) ? {4{FW_m_d[7:0]}} : 0;
								  
	assign m_inst_addr = m_pc;
	assign mw_out = (WD == 1) ? Dout : m_out;
	
	EXT m_ext(
	.A(m_aluout[1:0]),
	.Op(Op),
	.Dout(Dout),
	.m_data_rdata(m_data_rdata)
	);
	
	Controller m_ctrl (
	 .m_aluout(m_aluout),
    .instr(m_instr), 
    .Op(Op),
	 .WD(WD),
	 .m_data_byteen(m_data_byteen)
    );
endmodule