`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    18:08:53 11/01/2023 
// Design Name: 
// Module Name:    mips 
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
module mips(
	input clk,
	input reset
    );
	 
	wire [31:0] instr;
	wire sw;
	wire add;
	wire beq;
	wire WD;
	wire lui;
	wire jr;
	wire jal;
	wire RegC;
	wire we;
	wire Bsel;
	wire cin;
	wire EXTop;
	wire aluop;
	
	 Datapath dp_inst (
    .cin(cin), 
	 .add(add),
    .RegC(RegC), 
    .beq(beq), 
    .WD(WD), 
    .sw(sw), 
    .lui(lui), 
    .aluop(aluop), 
    .jr(jr), 
    .jal(jal), 
    .EXTop(EXTop), 
    .Bsel(Bsel), 
    .we(we), 
    .instr(instr), 
    .clk(clk), 
    .reset(reset)
    );

	Controller controller_inst (
    .instr(instr), 
    .sw(sw), 
    .beq(beq), 
	 .add(add),
    .WD(WD), 
    .lui(lui), 
    .jr(jr), 
    .jal(jal), 
    .RegC(RegC), 
    .we(we), 
    .Bsel(Bsel), 
    .cin(cin), 
    .EXTop(EXTop), 
    .aluop(aluop)
    );
	 
endmodule
