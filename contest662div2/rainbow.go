package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	for i, _ := strconv.Atoi(scanner.Text()); i > 0; i-- {
		scanner.Scan()
		ngrid, _ := strconv.Atoi(scanner.Text())
		fmt.Println(ngrid/2 + 1)
	}
}
