`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    10:05:18 11/16/2023 
// Design Name: 
// Module Name:    EXT 
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
module EXT(
	input [1:0] A,
	input [2:0] Op,
	input [31:0] m_data_rdata,
	
	output [31:0] Dout
    );
	
	assign Dout = (A == 2'b00 && Op == 3'b010) ? {{24{m_data_rdata[7]}}, m_data_rdata[7:0]} :
					  (A == 2'b01 && Op == 3'b010) ? {{24{m_data_rdata[15]}}, m_data_rdata[15:8]} :
					  (A == 2'b10 && Op == 3'b010) ? {{24{m_data_rdata[23]}}, m_data_rdata[23:16]} :
					  (A == 2'b11 && Op == 3'b010) ? {{24{m_data_rdata[31]}}, m_data_rdata[31:24]} :
					  (A[1] == 0 && Op == 3'b100) ? {{16{m_data_rdata[15]}}, m_data_rdata[15:0]} :
					  (A[1] == 1 && Op == 3'b100) ? {{16{m_data_rdata[31]}}, m_data_rdata[31:16]} : m_data_rdata;
endmodule
