module Memory (
    input clk,
    input reset,
    input [31:0] m_aluout,
    input [31:0] m_instr,
    input [31:0] m_pc,
	 input [31:0] m_out,
    
    input [31:0] FW_m_d,
    output [31:0] mw_out
);
    wire [31:0] DMout;
    wire sw, WD;
    assign mw_out = (WD == 1) ? DMout : m_out;

    Controller m_ctrl (
    .instr(m_instr), 
    .sw(sw),
    .WD(WD)
    );

    DM m_dm (
    .aluout(m_aluout), 
    .DMinput(FW_m_d), 
    .pc(m_pc), 
    .sw(sw), 
    .clk(clk), 
    .reset(reset), 
    .DMout(DMout)
    );

endmodule