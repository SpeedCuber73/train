package main

/*
import (
	"fmt"
	"runtime"
	"time"
)

const goroutinesNum = 3

func startWorker(workerNum int, in <-chan string) {
	for input := range in {
		fmt.Printf(formatWork(workerNum, input))
		runtime.Gosched() // попробуйте закомментировать
	}
	printFinishWork(workerNum)
}

func main() {
	worketInput := make(chan string, 2) // попробуйте увеличить размер канала
	for i := 0; i < goroutinesNum; i++ {
		go startWorker(i, worketInput)
	}
	months := []string{"Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"}
	for _, monthName := range months {
		worketInput <- monthName
	}
	close(worketInput) // попробуйте закомментировать
	time.Sleep(time.Millisecond)
}

func formatWork(i int, str string) string {
	return fmt.Sprintf("worker %v %s\n", i, str)
}

func printFinishWork(i int) {
	fmt.Println("Finish Worker", i)
}
*/
