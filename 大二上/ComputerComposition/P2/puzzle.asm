.data
	puzzle: .word 0 : 64
	dr: .word 0 : 4
	dc: .word 0 : 4
	visited: .word 0 : 64
	
.macro end
    li      $v0, 10
    syscall
.end_macro

.macro getInt(%des)
    li      $v0, 5
    syscall
    move    %des, $v0
.end_macro

.macro printInt(%src)
    move    $a0, %src
    li      $v0, 1
    syscall
.end_macro

.macro push(%src)
    sw      %src, 0($sp)
    subi    $sp, $sp, 4
.end_macro

.macro pop(%des)
    addi    $sp, $sp, 4
    lw      %des, 0($sp) 
.end_macro

.macro calc_addr(%dst, %row, %column, %rank)
    multu %row, %rank
    mflo %dst
    addu %dst, %dst, %column
    sll %dst, %dst, 2
.end_macro

.macro init()
	li $t0, 0
	sll $t1, $t0, 2
	li $t2, -1
	sw $t2, dr($t1)
	li $t2, 0
	sw $t2, dc($t1)
	addi $t0, $t0, 1
	sll $t1, $t0, 2
	li $t2, 1
	sw $t2, dr($t1)
	li $t2, 0
	sw $t2, dc($t1)
	addi $t0, $t0, 1
	sll $t1, $t0, 2
	li $t2, 0
	sw $t2, dr($t1)
	li $t2, -1
	sw $t2, dc($t1)
	addi $t0, $t0, 1
	sll $t1, $t0, 2
	li $t2, 0
	sw $t2, dr($t1)
	li $t2, 1
	sw $t2, dc($t1)
.end_macro

.text
	init()
	getInt($t0) # t0 = n
	getInt($t1) # t1 = m
	move $t2, $zero # i = t2
	move $t3, $zero # j = t3
	
for_in:
	getInt($t4)
	calc_addr($t5, $t2, $t3, $t1)
	sw $t4, puzzle($t5)
	addi $t3, $t3, 1
	bne $t3, $t1, for_in
	move $t3, $zero
	addi $t2, $t2, 1
	bne $t2, $t0, for_in
	
	getInt($s0) # s0 = s_r
	getInt($s1) # s1 = s_c
	getInt($s2) # s2 = e_r
	getInt($s3) # s3 = e_c
	addi $s0, $s0, -1
	addi $s1, $s1, -1
	addi $s2, $s2, -1
	addi $s3, $s3, -1
	move $s4, $zero # result
	move $t2, $zero 
	move $t3, $zero 
	move $a0, $s0
	move $a1, $s1
	jal count
	
print:
    move $s4, $v0
	printInt($s4)
	end
	
count:
	push($s4)
	push($t2)
	push($t3)
	push($t4)
	push($ra)
	move $t2, $a0
	move $t3, $a1
	bne $t2, $s2, if_1
	bne $t3, $s3, if_1
	
	li $v0, 1
	j return

if_1:
	calc_addr($t4, $t2, $t3, $t1)
	li $t5, 1
	sw $t5, visited($t4)
	move $s4, $zero # result
	li $t4, 0
	
for_1:
	sll $t5, $t4, 2
	lw $t6, dr($t5)
	add $s5, $t6, $t2
	lw $t6, dc($t5)
	add $s6, $t6, $t3
	bgt $zero, $s5, cycle
	bgt $zero, $s6, cycle
	bge $s5, $t0, cycle
	bge $s6, $t1, cycle
	
	calc_addr($t5, $s5, $s6, $t1)
	lw $t6, puzzle($t5)
	lw $t7, visited($t5)
	bne $t6, $zero, cycle
	bne $t7, $zero, cycle
	
	move $a0, $s5
	move $a1, $s6
	jal count
	add $s4, $s4, $v0
	
cycle:
	addi $t4, $t4, 1
	bne $t4, 4, for_1
	
	calc_addr($t5, $t2, $t3, $t1)
	sw $zero, visited($t5)
	move $v0, $s4
	
return:
	pop($ra)
	pop($t4)
	pop($t3)
	pop($t2)
	pop($s4)
	jr $ra
