`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:10:58 11/01/2023 
// Design Name: 
// Module Name:    DM 
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
module DM(
	input [31:0] aluout,
	input [31:0] DMinput,
	input [31:0] pc,
	input sw,
	input clk,
	input reset,
	output [31:0] DMout
    );
	reg [31:0] DMreg[3071:0];
	integer i;
	initial begin
		for (i = 0; i < 3072; i = i + 1) begin
			DMreg[i] = 0;
		end
	end
	assign DMout = DMreg[aluout[13:2]];
	always @(posedge clk) begin
		if (reset) begin
			for (i = 0; i <= 3071; i = i + 1) begin
				DMreg[i] <= 0;
		   end
		end
		else begin
			if (sw) begin
				DMreg[aluout[13:2]] <= DMinput;
				$display("%d@%h: *%h <= %h", $time, pc, aluout, DMinput);
			end
		end
	end
endmodule
