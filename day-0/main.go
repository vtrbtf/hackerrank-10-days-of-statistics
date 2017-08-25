package main
import "fmt"

func read(n int) ([]int, error) {
  in := make([]int, n)
  for i := range in {
    _, err := fmt.Scan(&in[i])
    if err != nil {
       return in[:i], err
    }
  }
  return in, nil
}

func main(){
    var size int
    fmt.Scanln(&size)
    fmt.Print(read(size))
}


