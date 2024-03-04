.data
	result: .word 0 : 1001
	
.macro end
    li      $v0, 10
    syscall
.end_macro

.macro getInt(%des)
    li      $v0, 5
    syscall
    move    %des, $v0
.end_macro

.text
	getInt($t0) # t0 = n

calc:
	li $t1, 1
	sw $t1 result($zero) # result[0] = 1
	li $t2, 1 # t2 = resultsize
	li $t3, 2 # i = t3
	
for_1:
	beq $t0, 0, for_0_print
	beq $t0, 1, for_1_print
	jal multiply
	addi $t3, $t3, 1
	bge $t0, $t3, for_1
	j print
	
multiply:
	move $s0, $zero # carry = s0
	li $t4, 0	# t4 = i

for_2:
	sll $t5, $t4, 2
	lw $t6, result($t5) # t6 = result[i]
	multu $t6, $t3 # t3 = multiplier
	mflo $t7 # t7 = result[i] * multiplier
	add $t1, $t7, $s0 # t1 = result[i] * multiplier + carry = product
	li $t6, 10
	div $t1, $t6
	mfhi $t7 # t7 = product % 10
	mflo $s0 # s0 = product / 10 = carry
	sw $t7, result($t5) # resutl[i] = product % 10
	addi $t4, $t4, 1
	bne $t4, $t2, for_2
	beq $zero, $s0, return
	
while:
	li $t5, 10
	div $s0, $t5
	mfhi $t6 # t6 = carry % 10
	mflo $s0
	sll $t1, $t2, 2
	sw $t6, result($t1)
	addi $t2, $t2, 1
	bne $s0, $zero, while

return:
	jr $ra
	
print: 	
	addi $t2, $t2, -1

for_print:
	sll $t5, $t2, 2
	lw $t6, result($t5)
	move $a0, $t6
	li $v0, 1
	syscall
	addi $t2, $t2, -1
	bge $t2, $zero, for_print
	end

for_0_print:
	li $a0, 1
	li $v0, 1
	syscall
	end

for_1_print:
	li $a0, 1
	li $v0, 1
	syscall
	end
	