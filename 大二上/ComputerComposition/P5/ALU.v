`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:11:05 11/01/2023 
// Design Name: 
// Module Name:    ALU 
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
module ALU(
	input [31:0] w1,
	input [31:0] w2,
	input cin,
	input aluop,
	input lui,
	input add,
	output reg [31:0] aluout
    );
	always @(*) begin
		if (cin) begin
			aluout <= w1 - w2;
		end
		else if (aluop) begin
			aluout <= w1 | w2;
		end
		else if (lui) begin
			aluout <= {w2[15:0], 16'b0};
		end
		else if (add) begin
			aluout <= w1 + w2;
		end
	end

endmodule
