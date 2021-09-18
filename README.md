# vending_machine
this program is vending machine (VM) operation system.

in contains such files as:
	products.tsv - this file is settings that should be maintained by operator. includes goods and their prices
	slots.tsv - this file is settings that should be maintained by operator. includes slot mapping and containings.
	embedded.py - python scripts for operating with VM hardware
	main.py - operation system

when VM switched ON the operation system is starting and waiting for a client.
it is working until it would be shutted down or storage would be empty.

first the client would see will be such like (includes only goods that are enable in storage):
---------------------------------------
		look at our goods
		1 juice 100
		2 water 50
		3 chocolate 150
		5 candies 300
		choose the product
---------------------------------------

you shoud type the number of product you want. if it is not valid number you have to type again.
after choosing valid number you should insert the money
---------------------------------------
		you choose ---juice--- the price is ---100---
		insert the money, the money avaiable is ---0---
---------------------------------------

if there are not enough money you would be asked to add more money
if it is match or higher then price VM will start giving you product

#for now there is no hardware thats why result is randomized as:
#	5% chance that the initial settings of VM is wrong and there are less goods then it is typed in file products.tsv
#	5% chance that slot in VM is broken and can not give the goods
#if it is ERROR from VM hardware it would be counted in Slots class and broken or empty slots will not be displayed again

after VM will success giving you product you will see something like:
---------------------------------------
take your change ---50---
take your goods ---water---
---------------------------------------

and the Sansara wheel spin again...

full log you can see on log.txt
