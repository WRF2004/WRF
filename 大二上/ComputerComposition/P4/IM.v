`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:09:56 11/01/2023 
// Design Name: 
// Module Name:    IM 
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
module IM(
	input [31:0] pc,
	output [31:0] instr 
    );
	 reg [31:0] IMreg[4095:0];
	 wire [31:0] temp;
	 assign temp = pc - 32'h00003000;
	 assign instr = IMreg[temp[13:2]];
	 integer i;
	 initial begin
		for (i = 0; i < 4096; i = i + 1) begin
			IMreg[i] = 0;
		end
		$readmemh("code.txt", IMreg);
	 end
	
endmodule
