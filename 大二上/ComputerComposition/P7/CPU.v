`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    08:26:15 11/16/2023 
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
module CPU(
	input clk,
	input reset,
	input interrupt,
	input IRQ0,
	input IRQ1,
	output [31:0] i_inst_addr, // f_pc
	input [31:0] i_inst_rdata, // f_instr
	
	input [31:0] m_data_rdata, //DMout
	output [31:0] m_data_addr, // m_aluout
	output [31:0] m_data_wdata, // FW_m_d
	output [3:0] m_data_byteen, // 
	output [31:0] m_inst_addr, // m_pc
	
	output [31:0] macroscopic_pc,
	output [3:0] m_int_byteen,
	output [31:0] m_int_addr,
	input [31:0] br_in, 
	output [31:0] br_wd, 
	output [31:0] br_addr,
	output br_we,
	 
	output w_grf_we, // w_we
	output [4:0] w_grf_addr, // w_a3
	output [31:0] w_grf_wdata, // w_out
	output [31:0] w_inst_addr // w_pc
    );
	 
	 wire [31:0] f_pc, f_instr, npc;

    wire fd_stall, de_stall, em_stall, busy, start;

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
	 
	 wire [4:0] f_exc, d_exc, e_exc, m_exc, de_exc, em_exc;
	 wire [31:0] EPC;
	 wire eret, req;
	 wire f_bd, d_bd, e_bd, m_bd;
	 assign i_inst_addr = f_pc;
	 assign w_grf_we = w_we;
	 assign w_grf_addr = w_a3;
	 assign w_grf_wdata = w_out;
	 assign w_inst_addr = w_pc;
	 
	 Fetch f (
    .clk(clk), 
    .reset(reset), 
    .npc(npc), 
    .EPC(EPC), 
    .fd_stall(fd_stall), 
    .eret(eret), 
    .req(req), 
    .i_inst_rdata(i_inst_rdata), 
    .f_pc(f_pc), 
    .f_exc(f_exc), 
    .f_instr(f_instr)
    );
	 
	 FDreg fd (
    .clk(clk), 
    .reset(reset), 
    .eret(eret), 
    .req(req), 
    .f_bd(f_bd), 
    .f_exc(f_exc), 
    .f_instr(f_instr), 
    .f_pc(f_pc), 
    .fd_stall(fd_stall), 
    .d_instr(d_instr), 
    .d_pc(d_pc), 
    .d_bd(d_bd), 
    .d_exc(d_exc)
    );
	 
	 Decode d (
    .clk(clk), 
    .reset(reset), 
    .f_pc(f_pc), 
    .d_pc(d_pc), 
    .d_instr(d_instr), 
    .FW_d_d1(FW_d_d1), 
    .FW_d_d2(FW_d_d2), 
    .d_exc(d_exc), 
    .w_we(w_we), 
    .w_pc(w_pc), 
    .w_out(w_out), 
    .w_a3(w_a3), 
    .f_bd(f_bd), 
    .de_exc(de_exc), 
    .d_rd1(d_rd1), 
    .d_rd2(d_rd2), 
    .d_a3(d_a3), 
    .ext_imm32d(ext_imm32d), 
    .de_out(de_out), 
    .npc(npc)
    );
	 
	 DEreg de (
    .clk(clk), 
    .reset(reset), 
    .eret(eret), 
    .req(req), 
    .d_bd(d_bd), 
    .d_instr(d_instr), 
    .ext_imm32d(ext_imm32d), 
    .d_pc(d_pc), 
    .FW_d_d1(FW_d_d1), 
    .FW_d_d2(FW_d_d2), 
    .d_a3(d_a3), 
    .de_out(de_out), 
    .de_exc(de_exc), 
    .de_stall(de_stall), 
    .em_stall(em_stall), 
    .e_bd(e_bd), 
    .e_exc(e_exc), 
    .e_a3(e_a3), 
    .e_pc(e_pc), 
    .e_rd1(e_rd1), 
    .e_rd2(e_rd2), 
    .e_instr(e_instr), 
    .ext_imm32e(ext_imm32e), 
    .e_out(e_out)
    );
	 
	 Execute exe (
    .clk(clk), 
    .reset(reset), 
    .eret(eret), 
    .req(req), 
    .e_exc(e_exc), 
    .e_instr(e_instr), 
    .ext_imm32e(ext_imm32e), 
    .FW_e_d1(FW_e_d1), 
    .FW_e_d2(FW_e_d2), 
    .e_out(e_out), 
    .e_aluout(e_aluout), 
    .e_DMinput(e_DMinput), 
    .em_out(em_out), 
    .em_exc(em_exc), 
    .busy(busy), 
    .start(start)
    );
	 
	 EMreg em (
    .clk(clk), 
    .reset(reset), 
    .eret(eret), 
    .req(req), 
    .e_bd(e_bd), 
    .e_a3(e_a3), 
    .em_exc(em_exc), 
    .e_aluout(e_aluout), 
    .e_pc(e_pc), 
    .e_instr(e_instr), 
    .e_DMinput(e_DMinput), 
    .em_out(em_out), 
    .em_stall(em_stall), 
    .m_exc(m_exc), 
    .m_bd(m_bd), 
    .m_a3(m_a3), 
    .m_aluout(m_aluout), 
    .m_pc(m_pc), 
    .m_instr(m_instr), 
    .m_out(m_out), 
    .m_DMinput(m_DMinput)
    );
	 
	 Memory m (
    .clk(clk), 
    .reset(reset), 
    .m_aluout(m_aluout), 
    .m_instr(m_instr), 
    .m_pc(m_pc), 
    .m_out(m_out), 
    .FW_m_d(FW_m_d), 
    .f_pc(f_pc), 
    .d_pc(d_pc), 
    .e_pc(e_pc), 
    .d_exc(d_exc), 
    .e_exc(e_exc), 
    .d_bd(d_bd), 
    .e_bd(e_bd), 
    .m_bd(m_bd), 
    .m_exc(m_exc), 
    .HWInt({3'b0, interrupt, IRQ1, IRQ0}), 
    .m_data_rdata(m_data_rdata), 
    .m_data_addr(m_data_addr), 
    .m_data_wdata(m_data_wdata), 
    .m_inst_addr(m_inst_addr), 
    .m_data_byteen(m_data_byteen), 
    .m_int_addr(m_int_addr), 
    .m_int_byteen(m_int_byteen), 
    .macroscopic_pc(macroscopic_pc), 
    .mw_out(mw_out), 
    .eret(eret), 
    .req(req), 
    .EPC(EPC), 
    .br_in(br_in), 
    .br_we(br_we), 
    .br_addr(br_addr), 
    .br_wd(br_wd)
    );
	 
	 MWreg mw (
    .clk(clk), 
    .reset(reset || req), 
    .m_a3(m_a3), 
    .mw_out(mw_out), 
    .m_instr(m_instr), 
    .m_pc(m_pc), 
    .w_a3(w_a3), 
    .w_out(w_out), 
    .w_instr(w_instr), 
    .w_pc(w_pc)
    );

	 Writeback wb (
    .w_instr(w_instr), 
    .w_we(w_we)
    );
	 
	 Stall stall (
    .start(start), 
    .busy(busy), 
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
	 
	 Process process (
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
    .w_out(w_grf_wdata), 
    .w_a3(w_grf_addr)
    );
	 
	 

endmodule
