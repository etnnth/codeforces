package main

import (
	"bufio"
	"fmt"
	"os"
)

/*
# Palindrome Game (easy version)

The only difference between the easy and hard versions is that the given string s
in the easy version is initially a palindrome, this condition is not always true
for the hard version.

A palindrome is a string that reads the same left to right and right to left.
For example, "101101" is a palindrome, while "0101" is not.

Alice and Bob are playing a game on a string s
(which is initially a palindrome in this version) of length n
consisting of the characters '0' and '1'. Both players take alternate turns with Alice going first.

In each turn, the player can perform one of the following operations:

* Choose any i (1≤i≤n), where s[i]= '0' and change s[i] to '1'. Pay 1 dollar.
* Reverse the whole string, pay 0 dollars. This operation is only
  allowed if the string is currently not a palindrome, and the last
  operation was not reverse. That is, if Alice reverses the string,
  then Bob can't reverse in the next move, and vice versa.

Reversing a string means reordering its letters from the last to the first.
For example, "01001" becomes "10010" after reversing.

The game ends when every character of string becomes '1'.
The player who spends minimum dollars till this point wins the
game and it is a draw if both spend equal dollars.
If both players play optimally, output whether Alice wins, Bob wins, or if it is a draw.


## Input

The first line contains a single integer t (1≤t≤103). Then t test cases follow.

The first line of each test case contains a single integer n (1≤n≤103).

The second line of each test case contains the string s
of length n, consisting of the characters '0' and '1'.
It is guaranteed that the string s is a palindrome and contains at least one '0'.

Note that there is no limit on the sum of n over test cases.

## Output

For each test case print a single word in a new line:

* "ALICE", if Alice will win the game,
* "BOB", if Bob will win the game,
* "DRAW", if the game ends in a draw.
*/
func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	var number_test_case int // number of test case
	fmt.Sscan(scanner.Text(), &number_test_case)
	for i := 0; i < number_test_case; i++ {
		var l int // lenght of the string
		var s string
		scanner.Scan()
		fmt.Sscan(scanner.Text(), &l)
		scanner.Scan()
		s = scanner.Text()
		fmt.Println(whoWin(s))
	}
}

// Alice who is starting wins if the number of 0 in the string
// is greater than 1 and odd
// She wins by chosing to change from 0 => 1 the 0 located in the
// center of the palindrome, giving Bob a palindrome with an even number
// of zero which is a losing position
func whoWin(s string) string {
	count0 := 0
	for _, c := range s {
		if c == '0' {
			count0++
		}
	}
	if count0 > 1 && count0%2 == 1 {
        return "ALICE"
	} else {
		return "BOB"
	}
}
