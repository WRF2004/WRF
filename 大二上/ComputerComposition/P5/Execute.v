module Execute (
    input [31:0] e_instr,
    input [31:0] ext_imm32e,
    input [31:0] FW_e_d1,
    input [31:0] FW_e_d2,
	 input [31:0] e_out,
    
    output [31:0] e_aluout,
    output [31:0] e_DMinput,
	 output [31:0] em_out
);
    wire [31:0] e_v1;
    wire [31:0] e_v2;
    wire Bsel;
    wire cin;
    wire aluop;
    wire lui;
    wire add, jal;
    assign e_v1 = FW_e_d1;
    assign e_v2 = (Bsel == 0) ? FW_e_d2 : ext_imm32e;
    assign e_DMinput = FW_e_d2;
	 assign em_out = (jal == 1) ? e_out : e_aluout;
	 
    Controller e_ctrl (
    .instr(e_instr), 
    .Bsel(Bsel),
    .cin(cin),
    .aluop(aluop),
    .lui(lui),
    .add(add),
	 .jal(jal)
    );

    ALU alu_inst (
	.add(add),
    .w1(e_v1), 
    .w2(e_v2), 
    .cin(cin), 
    .aluop(aluop), 
    .lui(lui), 
    .aluout(e_aluout)
    );
    
endmodule