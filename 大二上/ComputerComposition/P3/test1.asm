.text
add $t0, $t1, $t2
sub $t1, $t2, $t0
lui $t1, 1
beq $zero, $t1, for
lw $t0, 0($t1)
sw $t1, 0($t2)
nop
for:
ori $t3, $t0, 1