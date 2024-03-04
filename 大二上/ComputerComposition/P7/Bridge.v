`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    09:28:40 12/14/2023 
// Design Name: 
// Module Name:    Bridge 
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
module Bridge(
	 output [31:0] br_in,
	 input br_we,
	 input [31:0] br_addr,
	 input [31:0] br_wd,
	 input [31:0] tc0,
	 input [31:0] tc1,
	 output tc0_we,
	 output tc1_we,
	 output [31:0] tc_in,
	 output [31:0] tc_addr
    ); 
	
	assign tc0_we = (br_we && (br_addr >= 32'h7f00 && br_addr <= 32'h7f0b));
	assign tc1_we = (br_we && (br_addr >= 32'h7f10 && br_addr <= 32'h7f1b));
	assign br_in = (br_addr[4] == 0) ? tc0 : tc1;
	assign tc_in = br_wd;
	assign tc_addr = br_addr;
	
endmodule
