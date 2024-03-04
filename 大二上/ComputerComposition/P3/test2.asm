.text
lui $t0, 1
beq $t0, $t1, for
add $t2, $t0, $t1
sub $t3, $t2, $t1
lw $t5, 0($t1)
sw $t1, 0($t6)
nop
for:
nop