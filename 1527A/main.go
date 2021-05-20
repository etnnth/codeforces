package main

import (
    "bufio"
    "fmt"
    "os"
    "math/bits"
)

/*
And then there were K

Given an integer n, find the maximum value of integer k
such that the following condition holds:
n & (n−1) & (n−2) & (n−3) & ... (k) = 0
where & denotes the bitwise AND operation.

Input

The first line contains a single integer t: (1≤t≤3⋅104). 
Then t test cases follow.

The first line of each test case contains a single integer n: (1≤n≤109).

Output
For each test case, output a single integer, the required integer k.
*/
func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    var number_test_case int
    fmt.Sscan(scanner.Text(), &number_test_case)
    for i:=0; i < number_test_case; i++ {
        var n uint64
        scanner.Scan()
        fmt.Sscan(scanner.Text(), &n)
        fmt.Println(findK(n))
    }
}

// The value of k is the 2^(b-1) - 1
// With b the highest bit of n
func findK(n uint64) int{
    b := bits.Len64(n)
    return (1 << (b-1)) - 1
}
