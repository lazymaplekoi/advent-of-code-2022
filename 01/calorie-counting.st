| input |
input := 'input.txt'.

Transcript clear.

(input asFileReference) readStreamDo:  [ :stream |
	| line sum elves max |
	"Initialize variables"
	sum := 0.

	elves := SortedCollection new.
	elves := SortedCollection sortBlock: [:a :c | a > c].
	
	"Iterate through file and sum the lines as you go"
	[ (line := stream nextLine) notNil ] whileTrue: [ 
		line isEmpty
			ifFalse: [ sum := sum + (line asInteger). ]
			ifTrue: [ elves add: sum. sum := 0. ].
	 	].

		elves add: sum.
		max := elves first.
		
		"Part one: calculate max calories"
		Transcript show: max; cr.
		
		"Part two: calculate for total calories of the top three elves"
		max := 0.
		(1 to: 3) do: [ :i |
			max := max + (elves at: i). 
        ].
		
		Transcript show: max; cr.
    ].