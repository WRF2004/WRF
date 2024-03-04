.data
	c: .space 25
	equalC: .asciiz "1"
	inequalC: .asciiz "0"

.macro end
    li $v0, 10
    syscall
.end_macro

.macro getInt(%des)
    li $v0, 5
    syscall
    move %des, $v0
.end_macro

.macro getChar(%addr)
	li $v0, 12
	syscall
	sb $v0, c(%addr)
.end_macro

.text
	getInt($t0)
	move $t1, $zero
	
loop1:
	getChar($t1)
	addi $t1, $t1, 1
	bne $t1, $t0, loop1
	
	addi $t1, $t1, -1
	move $t2, $zero
	
loop2:
	lb $t3, c($t2)
	lb $t4, c($t1)
	bne $t3, $t4 ,inequal
	addi $t2, $t2, 1
	addi $t1, $t1, -1
	bne $t2, $t0, loop2 
	
	li $v0, 4
	la $a0, equalC
	syscall
	end
	
inequal:
	li $v0, 4
	la $a0, inequalC
	syscall
	end
