`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:08:53 11/01/2023 
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
	input clk,
	input reset
    );
	 
    wire [31:0] f_pc, f_instr, npc;

    wire fd_stall, de_stall, em_stall;

    wire [4:0] d_a3;
	wire [31:0] d_pc, d_instr, d_rd1, d_rd2, FW_d_d1, FW_d_d2, ext_imm32d;

	wire [31:0] de_out, em_out, mw_out;
	
    wire [4:0] e_a3;
	wire [31:0] e_out, e_pc, e_instr, e_rd1, e_rd2, FW_e_d1, FW_e_d2, ext_imm32e, e_aluout, e_DMinput;

    wire [4:0] m_a3;
	wire [31:0] m_pc, m_instr, FW_m_d, m_aluout, m_DMinput, m_out;

    wire w_we;
    wire [4:0] w_a3;
    wire [31:0] w_pc, w_instr, w_out;
	
	Process process_mips (
    .clk(clk), 
    .reset(reset), 
    .d_instr(d_instr), 
    .d_rd1(d_rd1), 
    .d_rd2(d_rd2), 
    .FW_d_d1(FW_d_d1), 
    .FW_d_d2(FW_d_d2), 
    .e_instr(e_instr), 
    .e_rd1(e_rd1), 
    .e_rd2(e_rd2), 
    .e_out(e_out), 
    .e_a3(e_a3), 
    .FW_e_d1(FW_e_d1), 
    .FW_e_d2(FW_e_d2), 
    .m_instr(m_instr), 
    .m_out(m_out), 
    .m_a3(m_a3), 
    .m_DMinput(m_DMinput), 
    .FW_m_d(FW_m_d), 
    .w_instr(w_instr), 
    .w_out(w_out), 
    .w_a3(w_a3)
    );
	 
	 Stall stall_mips (
    .d_instr(d_instr), 
    .e_instr(e_instr), 
    .m_instr(m_instr), 
    .e_a3(e_a3), 
    .m_a3(m_a3), 
    .e_out(e_out), 
    .m_out(m_out), 
    .fd_stall(fd_stall), 
    .de_stall(de_stall), 
    .em_stall(em_stall)
    );
	
	PC pc_mips (
    .clk(clk), 
    .reset(reset), 
    .npc(npc), 
    .fd_stall(fd_stall), 
    .f_pc(f_pc)
    );
	 
	 IM im_mips (
    .f_pc(f_pc), 
    .f_instr(f_instr)
    );
	 
	 FDreg fd_mips (
    .clk(clk), 
    .reset(reset), 
    .f_instr(f_instr), 
    .f_pc(f_pc), 
    .fd_stall(fd_stall), 
    .d_instr(d_instr), 
    .d_pc(d_pc)
    );
	 
	 Decode decode_mips (
    .clk(clk), 
    .reset(reset), 
    .f_pc(f_pc), 
    .d_pc(d_pc), 
    .d_instr(d_instr), 
    .FW_d_d1(FW_d_d1), 
    .FW_d_d2(FW_d_d2), 
    .w_we(w_we), 
    .w_pc(w_pc), 
    .w_out(w_out), 
    .w_a3(w_a3), 
    .d_rd1(d_rd1), 
    .d_rd2(d_rd2), 
    .d_a3(d_a3), 
    .ext_imm32d(ext_imm32d), 
    .de_out(de_out), 
    .npc(npc)
    );
	 
	 DEreg de_mips (
    .clk(clk), 
    .reset(reset), 
    .d_instr(d_instr), 
    .ext_imm32d(ext_imm32d), 
    .d_pc(d_pc), 
    .FW_d_d1(FW_d_d1), 
    .FW_d_d2(FW_d_d2), 
    .d_a3(d_a3), 
    .de_out(de_out), 
    .de_stall(de_stall), 
    .em_stall(em_stall), 
    .e_a3(e_a3), 
    .e_pc(e_pc), 
    .e_rd1(e_rd1), 
    .e_rd2(e_rd2), 
    .e_instr(e_instr), 
    .ext_imm32e(ext_imm32e), 
    .e_out(e_out)
    );
	 
	 Execute execute_mips (
    .e_instr(e_instr), 
    .ext_imm32e(ext_imm32e), 
    .FW_e_d1(FW_e_d1), 
    .FW_e_d2(FW_e_d2), 
    .e_out(e_out), 
    .e_aluout(e_aluout), 
    .e_DMinput(e_DMinput), 
    .em_out(em_out)
    );
	 
	 EMreg em_mips (
    .clk(clk), 
    .reset(reset), 
    .e_a3(e_a3), 
    .e_aluout(e_aluout), 
    .e_pc(e_pc), 
    .e_instr(e_instr), 
    .e_DMinput(e_DMinput), 
    .em_out(em_out), 
    .em_stall(em_stall), 
    .m_a3(m_a3), 
    .m_aluout(m_aluout), 
    .m_pc(m_pc), 
    .m_instr(m_instr), 
    .m_out(m_out), 
    .m_DMinput(m_DMinput)
    );
	 
	 Memory memory_mips (
    .clk(clk), 
    .reset(reset), 
    .m_aluout(m_aluout), 
    .m_instr(m_instr), 
    .m_pc(m_pc), 
    .m_out(m_out), 
    .FW_m_d(FW_m_d), 
    .mw_out(mw_out)
    );
	 
	 MWreg mw_mips (
    .clk(clk), 
    .reset(reset), 
    .m_a3(m_a3), 
    .mw_out(mw_out), 
    .m_instr(m_instr), 
    .m_pc(m_pc), 
    .w_a3(w_a3), 
    .w_out(w_out), 
    .w_instr(w_instr), 
    .w_pc(w_pc)
    );
	 
	 Writeback wb_mips (
    .w_instr(w_instr), 
    .w_we(w_we)
    );

endmodule
