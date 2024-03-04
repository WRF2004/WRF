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
	 input clk,
	 input reset,
    input [31:0] m_aluout,
    input [31:0] m_instr,
    input [31:0] m_pc,
	 input [31:0] m_out,
    input [31:0] FW_m_d,
	 
	 input [31:0] f_pc,
	 input [31:0] d_pc,
	 input [31:0] e_pc,
	 
	 input [4:0] d_exc,
	 input [4:0] e_exc,
	 
	 input d_bd,
	 input e_bd,
	 input m_bd,
	 
	 input [4:0] m_exc,
	 input [5:0] HWInt,
	 input [31:0] m_data_rdata, //DMout
	 
	 output [31:0] m_data_addr, // m_aluout
	 output [31:0] m_data_wdata, // FW_m_d
	 output [31:0] m_inst_addr, // m_pc
	 output [3:0] m_data_byteen, // enable 
	 output [31:0] m_int_addr,
	 output [3:0] m_int_byteen,
	 output [31:0] macroscopic_pc,
	 output [31:0] mw_out,
	 output eret,
	 output req,
	 output [31:0] EPC,
	 
	 input [31:0] br_in,
	 output br_we,
	 output [31:0] br_addr,
	 output [31:0] br_wd
    );
	 wire WD, bd, cp0we, st, cp0;
	 wire [2:0] Op, space_sel;
	 wire [1:0] bits;
	 wire [4:0] exc;
	 wire [31:0] Dout, CP0out, ext_in;
	 assign br_we = (st && (space_sel == 3'b011 || space_sel == 3'b010) && !req);
	 assign br_addr = m_aluout;
	 assign br_wd = m_data_wdata;
	 assign space_sel = (m_aluout < 32'h3000) ? 3'b001 : 
							  (m_aluout >= 32'h7f00 && m_aluout <= 32'h7f0b) ? 3'b010 :
							  (m_aluout >= 32'h7f10 && m_aluout <= 32'h7f1b) ? 3'b011 :
							  (m_aluout >= 32'h7f20 && m_aluout <= 32'h7f23) ? 3'b100 : 0;
							  
	assign ext_in = (space_sel == 3'b001) ? m_data_rdata : 
						 (space_sel == 3'b011 || space_sel == 3'b010) ? br_in : 0;
	
	assign exc = (WD && space_sel == 0 && m_exc == 0) ? 5'd4 :
					 (WD && bits == 2'b01 && m_aluout[1:0] != 0 && m_exc == 0) ? 5'd4 :
					 (WD && bits == 2'b10 && m_aluout[0] != 0 && m_exc == 0) ? 5'd4 :
					 (WD && (bits == 2'b10 || bits == 2'b11) && (space_sel == 3'b010 || space_sel == 3'b011) && m_exc == 0) ? 5'd4 : 
					 (st && space_sel == 0 && m_exc == 0) ? 5'd5 :
					 (st && bits == 2'b01 && m_aluout[1:0] != 0 && m_exc == 0) ? 5'd5 :
					 (st && bits == 2'b10 && m_aluout[0] != 0 && m_exc == 0) ? 5'd5 :
					 (st && (bits == 2'b10 || bits == 2'b11) && (space_sel == 3'b010 || space_sel == 3'b011) && m_exc == 0) ? 5'd5 : 
					 (st && ((m_aluout >= 32'h7f08 && m_aluout <= 32'h7f0b) || (m_aluout >= 32'h7f18 && m_aluout <= 32'h7f1b)) && m_exc == 0) ? 5'd5 : m_exc;
	
	assign m_data_addr = m_aluout;
	
	assign m_int_byteen = m_data_byteen;
	assign m_int_addr = m_aluout;
	assign m_data_wdata = (m_data_byteen == 4'b1111) ? FW_m_d : 
								 ((m_data_byteen == 4'b1100) || (m_data_byteen == 4'b0011)) ? {2{FW_m_d[15:0]}} :
								 ((m_data_byteen == 4'b0001) || (m_data_byteen == 4'b0010) || (m_data_byteen == 4'b0100) || (m_data_byteen == 4'b1000)) ? {4{FW_m_d[7:0]}} : 0;
								  
	assign m_inst_addr = m_pc;
	assign mw_out = (WD == 1 && req == 1) ? 0 : (WD == 1 && !req) ? Dout : (cp0 == 1) ? CP0out : m_out;
	assign macroscopic_pc = (m_pc != 32'h00003000 || m_exc == 5'd4) ? m_pc :
									(e_pc != 32'h00003000 || e_exc == 5'd4) ? e_pc :
									(d_pc != 32'h00003000 || d_exc == 5'd4) ? d_pc :
									f_pc;
									
	assign bd = (m_pc != 32'h00003000 || m_exc == 5'd4) ? m_bd :
					(e_pc != 32'h00003000 || e_exc == 5'd4) ? e_bd :
					(d_pc != 32'h00003000 || d_exc == 5'd4) ? d_bd : 0;
					
	CP0 Cp0 (
    .clk(clk), 
    .reset(reset), 
    .we(cp0we), 
    .CP0reg(m_instr[15:11]), 
    .CP0in(FW_m_d), 
    .CP0out(CP0out), 
    .vpc(macroscopic_pc), 
    .BDin(bd), 
    .ExcCodeIn(exc), 
    .HWInt(HWInt), 
    .eret(eret), 
    .EPCout(EPC), 
    .req(req)
    );
									
	EXT m_ext(
	.A(m_aluout[1:0]),
	.Op(Op),
	.Dout(Dout),
	.m_data_rdata(ext_in)
	);
	
	Controller m_ctrl (
	 .req(req),
	 .cp0(cp0),
	 .st(st),
	 .eret(eret),
	 .cp0we(cp0we),
	 .m_aluout(m_aluout),
    .instr(m_instr), 
    .Op(Op),
	 .WD(WD),
	 .bits(bits),
	 .m_data_byteen(m_data_byteen)
    );
	 
endmodule