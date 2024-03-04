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
	input [31:0] m_aluout,
	input [31:0] instr,
	input req,
	//output sw,
	output beq,
	output bne,
	output WD,
	output [2:0] Op,
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
	output yu,
	output [1:0] cmp,
	output d_rt,
	output d_rs,
	output e_rs,
	output e_rt,
	output e_not,
	output m_not,
	output [3:0] m_data_byteen,
	output [2:0] way,
	output LOw,
	output HIw,
	output start,
	output mh,
	output ml,
	output md,
	output ri,
	output ov,
	output st,
	output cp0we, 
	output syscall,
	output bd,
	output cp0,
	output eret,
	output [1:0] bits
    );
	wire [5:0] opcode;
	wire [5:0] funct;
	wire nop, add1, sub, beq1, lw, sw1, lui1, ori, jr1, jal1, bne1;
	wire sh, sb, lb, lh;
	wire and1, or1, slt, sltu, mult, multu, div, divu;
	wire addi, andi;
	wire mfhi, mflo, mthi, mtlo;
	wire mfc0, mtc0;

	assign opcode = instr[31:26];
	assign funct = instr[5:0];
	// AND
	assign nop = (opcode == 0 && funct == 0);
	assign add1 = (opcode == 0 && funct == 6'b100000);
	assign sub = (opcode == 0 && funct == 6'b100010) ? 1 : 0;
	assign beq1 = (opcode == 6'b000100) ? 1 : 0;
	assign bne1 = (opcode == 6'b000101);
	assign lw = (opcode == 6'b100011) ? 1 : 0;
	assign sw1 = (opcode == 6'b101011) ? 1 : 0;
	assign lui1 = (opcode == 6'b001111) ? 1 : 0;
	assign ori = (opcode == 6'b001101) ? 1 : 0;
	assign jr1 = (opcode == 0 && funct == 6'b001000) ? 1 : 0;
	assign jal1 = (opcode == 6'b000011) ? 1 : 0;
	assign sh = (opcode == 6'b101001);
	assign sb = (opcode == 6'b101000);
	assign lb = (opcode == 6'b100000);
	assign lh = (opcode == 6'b100001);
	assign and1 = (opcode == 0 && funct == 6'b100100);
	assign or1 = (opcode == 0 && funct == 6'b100101);
	assign slt = (opcode == 0 && funct == 6'b101010);
	assign sltu = (opcode == 0 && funct == 6'b101011); 
	
	assign addi = (opcode == 6'b001000);
	assign andi = (opcode == 6'b001100);
	
	assign mult = (opcode == 0 && funct == 6'b011000);
	assign multu = (opcode == 0 && funct == 6'b011001);
	assign div = (opcode == 0 && funct == 6'b011010);
	assign divu = (opcode == 0 && funct == 6'b011011);
	assign mfhi = (opcode == 0 && funct == 6'b010000);
	assign mflo = (opcode == 0 && funct == 6'b010010);
	assign mthi = (opcode == 0 && funct == 6'b010001);
	assign mtlo = (opcode == 0 && funct == 6'b010011);
	
	assign eret = (opcode == 6'b010000 && funct == 6'b011000);
	assign mfc0 = (opcode == 6'b010000 && instr[25:21] == 0);
	assign mtc0 = (opcode == 6'b010000 && instr[25:21] == 5'b00100);
	assign syscall = (opcode == 0 && funct == 6'b001100);
	// OR
	assign cp0 = mfc0;
	assign bits = (sw1 || lw) ? 2'b01 : (sh || lh) ? 2'b10 : (sb || lb) ? 2'b11 : 0; 
	assign md = mult | multu | div | divu | mthi | mtlo | mfhi | mflo;
	assign mh = mfhi;
	assign ml = mflo;
	assign cp0we = mtc0;
	assign bd = bne1 | beq1 | jal1 | jr1;
	assign way = (mult == 1) ? 3'b001 : (multu == 1) ? 3'b010 : (div == 1) ? 3'b011 : (divu == 1) ? 3'b100 : 0;
	assign start = mult | multu | div | divu;
	assign LOw = mtlo;
	assign HIw = mthi;
	assign aluop = ori | or1;
	assign yu = and1 | andi;
	assign cmp = (slt == 1) ? 2'b01 : (sltu == 1) ? 2'b10 : 0;
	assign st = sw1 | sh | sb;
	assign lui = lui1;
	assign jr = jr1;
	assign jal = jal1;
	assign beq = beq1;
	assign bne = bne1;
	assign WD = lw | lb | lh;
	assign ov = add1 | addi | sub;
	assign EXTop = sw1 | lw | sb | sh | lb | lh | addi;
	assign cin = sub;
	assign Bsel = ori | sw1 | lw | lui1 | sb | sh | lb | lh | addi | andi;
	assign we = jal1 | add1 | sub | lw | lui1 | ori | lb | lh | and1 | or1 | slt | sltu | addi | andi | mflo | mfhi | mfc0;
	assign RegC = add1 | sub | and1 | or1 | slt | sltu | mflo | mfhi;
	assign add = add1 | sw1 | lw | sb | sh | lb | lh | addi;
	assign d_rs = beq1 | jr1 | bne1;
	assign d_rt = beq1 | bne1;
	assign e_rs = add1 | sub | ori | lw | sw1 | sb | sh | lb | lh | and1 | or1 | slt | sltu | addi | andi | mult | multu | div | divu | mthi | mtlo;
	assign e_rt = add1 | sub | and1 | or1 | sltu | slt | mult | multu | div | divu;
	assign e_not = add1 | sub | ori | lui1 | lw | lb | lh | and1 | or1 | slt | sltu | addi | andi | mfhi | mflo;
	assign m_not = lw | lb | lh | mfc0;
	assign Op = (lb == 1) ? 3'b010 : 
					(lh == 1) ? 3'b100 : 0;
	assign m_data_byteen = (req == 1) ? 0 : (sw1 == 1) ? 4'b1111 : 
								(sh == 1 && m_aluout[1] == 0) ? 4'b0011 : 
								(sh == 1 && m_aluout[1] == 1) ? 4'b1100 :
								(sb == 1 && m_aluout[1:0] == 2'b00) ? 4'b0001 :
								(sb == 1 && m_aluout[1:0] == 2'b01) ? 4'b0010 :
								(sb == 1 && m_aluout[1:0] == 2'b10) ? 4'b0100 :
								(sb == 1 && m_aluout[1:0] == 2'b11) ? 4'b1000 : 0;
	assign ri = !(nop | add1 | sub | beq1 | bne1 | lw | sw1 | lui1 | ori | jr1 | jal1 | 
					  sh | sb | lb | lh | and1 | or1 | slt | sltu | addi | andi | mult | multu |
					  div | divu | mfhi | mflo | mthi | mtlo | eret | mfc0 | mtc0 | syscall);							
	
endmodule
