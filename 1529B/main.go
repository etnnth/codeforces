package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
    "strconv"
    "sort"
)

/*
A sequence (b1,b2,…,bk) is called strange, if the absolute difference 
between any pair of its elements is greater than or equal to the 
maximum element in the sequence. Formally speaking, it's strange if 
for every pair (i,j) with 1≤i<j≤k, we have |ai−aj|≥MAX, where MAX is 
the largest element of the sequence. In particular, any sequence of length 
at most 1 is strange.

For example, the sequences (−2021,−1,−1,−1)
and (−1,0,1) are strange, but (3,0,1) is not, because |0−1|<3

Sifid has an array a of n integers. Sifid likes everything big, 
so among all the strange subsequences of a, he wants to find 
the length of the longest one. Can you help him?

A sequence c is a subsequence of an array d if c can be obtained from d
by deletion of several (possibly, zero or all) elements.

## Input

The first line contains an integer t (1≤t≤104) — the number 
of test cases. The description of the test cases follows.

The first line of each test case contains an integer n
(1≤n≤105) — the length of the array a

The second line of each test case contains n
integers a1,a2,…,an (−109≤ai≤109) — the elements of the array a

It is guaranteed that the sum of nover all test cases doesn't exceed 105

## Output

For each test case output a single integer — 
the length of the longest strange subsequence of a
*/
func main() {
    scanner := bufio.NewScanner(os.Stdin)
    // Need big buffer because some line can be really big
    scanner.Buffer(make([]byte, 20000000), 20000000)
    scanner.Scan()
    var number_test_case int
    fmt.Sscan(scanner.Text(), &number_test_case)
    for i:=0; i < number_test_case; i++ {
        var number_elements uint64
        scanner.Scan()
        fmt.Sscan(scanner.Text(), &number_elements)
        scanner.Scan()
        array := make([]int, number_elements)
        for i, v := range strings.Split(scanner.Text(), " ") {
            array[i], _ = strconv.Atoi(v)
        }
        fmt.Println(len(longest_strange(array)))
    }
}


func longest_strange(a []int) []int {
    sort.Ints(a)
    var ls []int
    minD := 2000000011 // Minimum distance between two number
    // add the smallest number that will alwais be part of the stange sequence
    ls = append(ls, a[0])
    // loop over all the number until we find a number bigger than
    // the minimum distance between two element of the sequence
    for i, v := range a[1:] {
        if v - ls[i] < minD {
            minD = v - ls[i]
        }
        if v <= minD {
            ls = append(ls, v)
        } else {
            return ls
        }
    }
    return ls
}


