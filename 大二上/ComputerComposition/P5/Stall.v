module Stall (
    input [31:0] d_instr,
    input [31:0] e_instr,
	 input [31:0] m_instr,
    input [4:0] e_a3,
	 input [4:0] m_a3,
	 input [31:0] e_out,
	 input [31:0] m_out,
    output fd_stall,
	 output de_stall,
	 output em_stall
);
    wire d_rt, d_rs;
	 wire e_rt, e_rs, e_not;
	 wire m_not;
	 
	 assign de_stall = ((d_rs && d_instr[25:21] == e_a3 && e_a3 != 0 && e_not) || (d_rs && d_instr[25:21] == m_a3 && m_a3 != 0 && m_not && !(d_rs && d_instr[25:21] == e_a3 && e_a3 != 0 && !e_not)) ||
							 (d_rt && d_instr[20:16] == e_a3 && e_a3 != 0 && e_not) || (d_rt && d_instr[20:16] == m_a3 && m_a3 != 0 && m_not && !(d_rt && d_instr[20:16] == e_a3 && e_a3 != 0 && !e_not))) && !em_stall;
	 
	 assign em_stall = (e_rs && e_instr[25:21] == m_a3 && m_a3 != 0 && m_not) || 
							 (e_rt && e_instr[20:16] == m_a3 && m_a3 != 0 && m_not);
							 
	 assign fd_stall = de_stall | em_stall;
	 
	 Controller d_stall_ctrl(
	 .instr(d_instr),
	 .d_rt(d_rt),
	 .d_rs(d_rs)
	 );
	 
	 Controller e_stall_ctrl(
	 .instr(e_instr),
	 .e_rt(e_rt),
	 .e_rs(e_rs),
	 .e_not(e_not)
	 );
    
	 Controller m_stall_ctrl(
	 .instr(m_instr),
	 .m_not(m_not)
	 );
	 
endmodule