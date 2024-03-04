`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    23:59:19 12/14/2023 
// Design Name: 
// Module Name:    Fetch 
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
module Fetch(
	input clk,
	input reset,
	input [31:0] npc,
	input [31:0] EPC,
	input fd_stall,
	input eret,
	input req,
	input [31:0] i_inst_rdata, // f_instr
	output [31:0] f_pc,
	output [4:0] f_exc,
	output [31:0] f_instr
    );
	 
	 wire [31:0] pc_in;
	 assign pc_in = eret ? EPC : req ? 32'h00004180 : npc;
	 assign f_exc = ((f_pc[1:0] != 0) || (f_pc < 32'h00003000) || (f_pc > 32'h00006ffc)) ? 5'd4 : 0;
	assign f_instr = (f_exc == 0) ? i_inst_rdata : 0;
	PC pc (
    .clk(clk), 
    .reset(reset), 
    .pc_in(pc_in), 
    .en(!fd_stall || eret || req), 
    .pc_out(f_pc)
    );

endmodule
