`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:09:25 11/01/2023 
// Design Name: 
// Module Name:    Controller 
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
module Controller(
	input [31:0] instr,
	output sw,
	output beq,
	output WD,
	output lui,
	output jr,
	output jal,
	output RegC,
	output we,
	output Bsel,
	output cin,
	output EXTop,
	output add,
	output aluop,
	output d_rt,
	output d_rs,
	output e_rs,
	output e_rt,
	output e_not,
	output m_not
    );
	wire [5:0] opcode;
	wire [5:0] funct;
	wire nop, add1, sub, beq1, lw, sw1, lui1, ori, jr1, jal1;
	assign opcode = instr[31:26];
	assign funct = instr[5:0];
	// AND
	assign nop = (opcode == 0 && funct == 0);
	assign add1 = (opcode == 0 && funct == 6'b100000);
	assign sub = (opcode == 0 && funct == 6'b100010) ? 1 : 0;
	assign beq1 = (opcode == 6'b000100) ? 1 : 0;
	assign lw = (opcode == 6'b100011) ? 1 : 0;
	assign sw1 = (opcode == 6'b101011) ? 1 : 0;
	assign lui1 = (opcode == 6'b001111) ? 1 : 0;
	assign ori = (opcode == 6'b001101) ? 1 : 0;
	assign jr1 = (opcode == 0 && funct == 6'b001000) ? 1 : 0;
	assign jal1 = (opcode == 6'b000011) ? 1 : 0;
	// OR
	assign aluop = ori;
	assign sw = sw1;
	assign lui = lui1;
	assign jr = jr1;
	assign jal = jal1;
	assign beq = beq1;
	assign WD = lw;
	assign EXTop = sw1 | lw;
	assign cin = sub;
	assign Bsel = ori | sw1 | lw | lui1;
	assign we = jal1 | add1 | sub | lw | lui1 | ori;
	assign RegC = add1 | sub;
	assign add = add1 | sw1 | lw;
	assign d_rs = beq1 | jr1;
	assign d_rt = beq1;
	assign e_rs = add1 | sub | ori | lw | sw1;
	assign e_rt = add1 | sub;
	assign e_not = add1 | sub | ori | lui1 | lw;
	assign m_not = lw;
endmodule
