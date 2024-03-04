`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:09:49 11/01/2023 
// Design Name: 
// Module Name:    PC 
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
module PC(
	input clk,
	input reset,
	input [31:0] npc,
	output reg [31:0] pc
    );
	initial begin
		pc = 32'h00003000;
	end
	always @(posedge clk) begin
		if (reset) begin
			pc = 32'h00003000;
		end
		else begin
			pc = npc;
		end
	end

endmodule
