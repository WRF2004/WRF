module Decode (
    input clk,
    input reset,
    
    input [31:0] f_pc,
    input [31:0] d_pc,
    input [31:0] d_instr,

    input [31:0] FW_d_d1, // forward rs_value
    input [31:0] FW_d_d2, // forward rt_value 

	 // write back value
    input w_we,
    input [31:0] w_pc,
    input [31:0] w_out,
    input [4:0] w_a3,
    
    output [31:0] d_rd1,
    output [31:0] d_rd2, 
    output [4:0] d_a3,
    output [31:0] ext_imm32d,
	 output [31:0] de_out,
    output [31:0] npc
);
    wire [4:0] d_a1;
    wire [4:0] d_a2;
    wire EXTop, jal, jr;
    wire RegC, beq, result;
    assign d_a1 = d_instr[25:21];
    assign d_a2 = d_instr[20:16];
    assign d_a3 = (jal == 1) ? 5'b11111 : (RegC == 1) ? d_instr[15:11] : d_instr[20:16];
    assign ext_imm32d = (EXTop == 1) ? {{16{d_instr[15]}}, d_instr[15:0]} : {16'b0, d_instr[15:0]};
    assign result = (FW_d_d1 == FW_d_d2); //beq sign
	 assign de_out = (jal == 1) ? d_pc + 8 : 32'bz; // e_out
	
    NPC d_npc (
    .imm26(d_instr[25:0]), 
    .d_pc(d_pc), 
    .f_pc(f_pc),
    .jr(jr), 
    .RegRs(FW_d_d1), // jr sign
    .jal(jal), 
    .result(result), 
    .beq(beq), 
    .npc(npc)
    );

    Controller d_ctrl (
    .instr(d_instr), 
    .EXTop(EXTop), 
    .RegC(RegC),
    .beq(beq),
    .jal(jal),
    .jr(jr)
    );

    GRF d_grf (
    .pc(w_pc), 
    .a1(d_a1), 
    .a2(d_a2), 
    .a3(w_a3), 
    .wd(w_out), 
    .we(w_we), 
    .reset(reset), 
    .clk(clk), 
    .rd1(d_rd1), 
    .rd2(d_rd2)
    );

endmodule