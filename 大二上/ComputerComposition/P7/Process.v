module Process (
	 input clk,
	 input reset,
	 
    input [31:0] d_instr,
    input [31:0] d_rd1,
    input [31:0] d_rd2,
    output [31:0] FW_d_d1,
    output [31:0] FW_d_d2,

    input [31:0] e_instr,
    input [31:0] e_rd1,
    input [31:0] e_rd2,
    input [31:0] e_out,
    input [4:0] e_a3,
    output [31:0] FW_e_d1,
    output [31:0] FW_e_d2,

    input [31:0] m_instr,
    input [31:0] m_out,
    input [4:0] m_a3,
	 input [31:0] m_DMinput,
    output [31:0] FW_m_d,

    input [31:0] w_instr,
    input [31:0] w_out,
    input [4:0] w_a3
);
    wire e_we, m_we, w_we;
	 reg [31:0] b_out;
	 reg [4:0] b_a3;
	 reg b_we;
	 initial begin
		b_out = 0;
		b_a3 = 0;
		b_we = 0;
	 end
	 
	 always @(posedge clk) begin
		if (reset) begin
			b_a3 <= 0;
			b_out <= 0;
			b_we <= 0;
		end
		else begin
			b_a3 <= w_a3;
			b_out <= w_out;
			b_we <= w_we;
		end
	 end
	 
	 assign FW_d_d1 = (d_instr[25:21] == 0) ? 0 :
                     (d_instr[25:21] == e_a3 && e_we == 1) ? e_out :
                     (d_instr[25:21] == m_a3 && m_we == 1) ? m_out :
							(d_instr[25:21] == w_a3 && w_we == 1) ? w_out :
							//(d_instr[25:21] == b_a3 && b_we == 1) ? b_out :
                     d_rd1;

    assign FW_d_d2 = (d_instr[20:16] == 0) ? 0 :
                     (d_instr[20:16] == e_a3 && e_we == 1) ? e_out :
                     (d_instr[20:16] == m_a3 && m_we == 1) ? m_out :
							(d_instr[20:16] == w_a3 && w_we == 1) ? w_out :
							//(d_instr[20:16] == b_a3 && b_we == 1) ? b_out :
                     d_rd2;

    assign FW_e_d1 = (e_instr[25:21] == 0) ? 0 :
                     (e_instr[25:21] == m_a3 && m_we == 1) ? m_out :
                     (e_instr[25:21] == w_a3 && w_we == 1) ? w_out :
							(e_instr[25:21] == b_a3 && b_we == 1) ? b_out :
                     e_rd1;

    assign FW_e_d2 = (e_instr[20:16] == 0) ? 0 :
                     (e_instr[20:16] == m_a3 && m_we == 1) ? m_out :
                     (e_instr[20:16] == w_a3 && w_we == 1) ? w_out :
							(e_instr[20:16] == b_a3 && b_we == 1) ? b_out :
                     e_rd2;

    assign FW_m_d = (m_instr[20:16] == 0) ? 0 : 
                    (m_instr[20:16] == w_a3 && w_we == 1) ? w_out :
						  (m_instr[20:16] == b_a3 && b_we == 1) ? b_out :
                    m_DMinput;

    Controller e_process (
    .instr(e_instr),
    .we(e_we)
    );

    Controller m_process (
    .instr(m_instr),
    .we(m_we)
    );

    Controller w_process (
    .instr(w_instr),
    .we(w_we)
    );

endmodule