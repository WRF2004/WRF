`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    19:58:30 11/01/2023 
// Design Name: 
// Module Name:    Datapath 
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
module Datapath(
	input add,
	input cin,
	input RegC,
	input beq,
	input WD,
	input sw,
	input lui,
	input aluop,
	input jr,
	input jal,
	input EXTop,
	input Bsel,
	input we,
	output [31:0] instr,
	input clk,
	input reset
    );
	
	wire result; // ALU output1
	wire [31:0] pc;
	wire [31:0] npc;
	wire [31:0] rd2; // GRF second output && DM input data
	wire [31:0] w1; //GRF first output && ALU input1 && RegRs
	wire [31:0] aluout; // ALU output2 && DM address
	wire [31:0] DMout; // DM output
	wire [25:0] imm26; 
	wire [4:0] a1; //rs
	wire [4:0] a2; //rt
	wire [4:0] a3; // rd
	wire [31:0] w2; //ALU input2
	wire [31:0] wd;
	
	assign imm26 = instr[25:0]; 
	assign a1 = instr[25:21]; //rs
	assign a2 = instr[20:16]; //rt
	assign a3 = (jal == 1) ? 5'b11111 : (RegC == 1) ? instr[15:11] : instr[20:16]; // rd
	assign w2 = (Bsel == 0) ? rd2 : (EXTop == 1) ? {{16{instr[15]}}, instr[15:0]} : {16'b0, instr[15:0]}; //ALU input2
	assign wd = (jal == 1) ? pc + 4 : (WD == 1) ? DMout : aluout; //GRF input data
	
	PC pc_inst (
    .clk(clk), 
    .reset(reset), 
    .npc(npc), 
    .pc(pc)
    );
	
	NPC npc_inst (
    .imm26(imm26), 
    .pc(pc), 
    .jr(jr), 
    .RegRs(w1), 
    .jal(jal), 
    .result(result), 
    .beq(beq), 
    .npc(npc)
    );

	IM im_inst (
    .pc(pc), 
    .instr(instr)
    );
	 
	 GRF grf_inst (
    .pc(pc), 
    .a1(a1), 
    .a2(a2), 
    .a3(a3), 
    .wd(wd), 
    .we(we), 
    .reset(reset), 
    .clk(clk), 
    .rd1(w1), 
    .rd2(rd2)
    );
	 
	DM dm_inst (
    .aluout(aluout), 
    .DMinput(rd2), 
    .pc(pc), 
    .sw(sw), 
    .clk(clk), 
    .reset(reset), 
    .DMout(DMout)
    );
	 
	 ALU alu_inst (
	 .add(add),
    .w1(w1), 
    .w2(w2), 
    .cin(cin), 
    .aluop(aluop), 
    .lui(lui), 
    .result(result), 
    .aluout(aluout)
    );
	
endmodule
