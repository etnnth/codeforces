package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
    "strconv"
)

/*
Eshag has an array a consisting of n integers.

Eshag can perform the following operation any number of times: 
choose some subsequence of a and delete every element from it 
which is strictly larger than AVG, where AVG is the average of 
the numbers in the chosen subsequence.

For example, if a=[1,4,3,2,4] and Eshag applies the operation 
to the subsequence containing a1, a2, a4 and a5, then he will 
delete those of these 4 elements which are larger than 
a1+a2+a4+a54=114, so after the operation, the array a will become a=[1,3,2]

Your task is to find the maximum number of elements Eshag can delete from the array a
by applying the operation described above some number (maybe, zero) times.

A sequence b is a subsequence of an array c if b can be obtained from c
by deletion of several (possibly, zero or all) elements.

Input

The first line contains an integer t (1≤t≤100)

— the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n (1≤n≤100)
the length of the array a

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤100) 
the elements of the array a

Output

For each test case print a single integer
the maximum number of elements Eshag can delete from the array a
*/
func main() {
    scanner := bufio.NewScanner(os.Stdin)
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
        fmt.Println(max_removed(array))
    }
}


func max_removed(a []int) int {
    n := len(a)
    for i:=0; i < n; i++ { // brute force it max itereation is the len of a
        a = filter(a)
    }
    return n - len(a)
}


func filter(a []int) []int {
    av := average_uniques(a)
    var na []int
    for _, v := range a {
        if v <= av {
            na = append(na, v)
        }
    }
    return na
}


func average_uniques(a []int) int {
    s := 0
    u := make(map[int]bool)
    n := 0
    for _, v := range a{
        if !u[v] {
            s += v
            n ++
            u[v] = true
        }
    }
    return s / n
}


