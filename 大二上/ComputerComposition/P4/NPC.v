`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:10:08 11/01/2023 
// Design Name: 
// Module Name:    NPC 
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
module NPC(
	input [25:0] imm26,
	input [31:0] pc,
	input jr,
	input [31:0] RegRs,
	input jal,
	input result,
	input beq,
	output reg [31:0] npc
    );
	always @(*) begin
		if (beq == 1 && result == 1) begin
			npc = pc + 4 + {{14{imm26[15]}}, imm26[15:0], 2'b00};
		end
		else if (jr == 1) begin
			npc = RegRs;
		end
		else if (jal == 1) begin
			npc = {pc[31:28], imm26, 2'b00};
		end
		else npc = pc + 4;
	end

endmodule
