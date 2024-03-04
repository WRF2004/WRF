module EMreg (
    input clk,
    input reset,
    input [4:0] e_a3,
    input [31:0] e_aluout,
    input [31:0] e_pc,
    input [31:0] e_instr,
    input [31:0] e_DMinput,
	 input [31:0] em_out,
	 input em_stall,
    
    output reg [4:0] m_a3,
    output reg [31:0] m_aluout,
    output reg [31:0] m_pc,
    output reg [31:0] m_instr,
	 output reg [31:0] m_out,
    output reg [31:0] m_DMinput 
);
    initial begin
        m_a3 = 0;
        m_aluout = 0;
        m_pc = 32'h00003000;
        m_instr = 0;
        m_DMinput = 0;
		  m_out = 0;
    end
    always @(posedge clk) begin
        if (reset || em_stall) begin
            m_a3 <= 0;
            m_aluout <= 0;
            m_pc <= 32'h00003000;
            m_instr <= 0;
            m_DMinput <= 0;
				m_out <= 0;
        end
        else begin
            m_a3 <= e_a3;
            m_aluout <= e_aluout;
            m_pc <= e_pc;
            m_instr <= e_instr;
            m_DMinput <= e_DMinput;
				m_out <= em_out;
        end
    end
endmodule