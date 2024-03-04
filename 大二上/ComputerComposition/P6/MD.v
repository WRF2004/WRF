`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    13:52:55 11/16/2023 
// Design Name: 
// Module Name:    MD 
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
module MD(
	input clk,
	input reset,
	input [31:0] w1,
	input [31:0] w2,

	input HIw,
	input LOw,
	input [2:0] way,
	input start,
	output busy,
	
	output reg [31:0] hi,
	output reg [31:0] lo
    );
	 
	 reg [3:0] sign;
	 reg [31:0] hi_temp;
	 reg [31:0] lo_temp;
	 
	initial begin
		hi = 0;
		lo = 0;
		sign = 0;
		hi_temp = 0;
		lo_temp = 0;
	end
	
	assign busy = (sign != 0);
	
	always @(posedge clk) begin
		if (reset) begin
			hi <= 0;
			lo <= 0;
			sign <= 0;
			hi_temp <= 0;
			lo_temp <= 0;
		end
		else if (start) begin
			if (way == 3'b001) begin // mult
				{hi_temp, lo_temp} <= $signed(w1) * $signed(w2);
				sign <= 5;
			end
			else if (way == 3'b010) begin // multu
				{hi_temp, lo_temp} <= w1 * w2;
				sign <= 5;
			end
			else if (way == 3'b011) begin // div
				lo_temp <= $signed(w1) / $signed(w2);
				hi_temp <= $signed(w1) % $signed(w2);
				sign <= 10;
			end
			else if (way == 3'b100) begin // divu
				lo_temp <= w1 / w2;
				hi_temp <= w1 % w2;
				sign <= 10;
			end
		end
		else if (HIw) begin
			hi <= w1;
		end
		else if (LOw) begin
			lo <= w1;
		end
		else if (sign != 0) begin
			if (sign == 1) begin
				hi <= hi_temp;
				lo <= lo_temp;
				sign <= 0;
			end
			else begin
				sign <= sign - 1;
			end
		end
		//if (sign != 0 && reset == 0 && start == 0) begin
			//if (sign == 1) begin
				//hi <= hi_temp;
				//lo <= lo_temp;
				//sign <= 0;
			//end
			//else begin
				//sign <= sign - 1;
			//end
		//end
	end
	
endmodule
