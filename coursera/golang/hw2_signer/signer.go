package main

import (
	"fmt"
	"sort"
	"strings"
	"sync"
)

func myGoroutine(in, out chan interface{}, oneJob job, wg *sync.WaitGroup) {
	defer wg.Done()
	oneJob(in, out)
	close(out)
}

// ExecutePipeline executes jobs in pipeline style
func ExecutePipeline(jobs ...job) {
	wg := &sync.WaitGroup{}
	countJobs := len(jobs)
	out := make(chan interface{})
	for i := 0; i < countJobs; i++ {
		in := out
		out = make(chan interface{})
		wg.Add(1)
		go myGoroutine(in, out, jobs[i], wg)
	}
	wg.Wait()
}

func startCrc32(data string, out chan string) {
	out <- DataSignerCrc32(data)
}

func startCrc32WithMd5(data string, out chan string, quotaMd5 chan struct{}) {
	quotaMd5 <- struct{}{}
	md5 := DataSignerMd5(data)
	<-quotaMd5
	out <- DataSignerCrc32(md5)
}

func startSingleHash(data string, out chan string, quotaMd5 chan struct{}) {
	firstChan := make(chan string)
	go startCrc32(data, firstChan)
	secondChan := make(chan string)
	go startCrc32WithMd5(data, secondChan, quotaMd5)
	firstRes := <-firstChan
	secondRes := <-secondChan
	out <- firstRes + "~" + secondRes
}

func SingleHash(in, out chan interface{}) {
	quotaMd5 := make(chan struct{}, 1)
	var resultsChan []chan string
	for input := range in {
		inputInt := input.(int)
		data := fmt.Sprintf("%v", inputInt)
		newChan := make(chan string)
		go startSingleHash(data, newChan, quotaMd5)
		resultsChan = append(resultsChan, newChan)
	}
	for _, resChan := range resultsChan {
		out <- <-resChan
	}
}

func startMultiHash(data string, out chan string) {
	var resultsChan []chan string
	for i := 0; i < 6; i++ {
		th := fmt.Sprintf("%v", i)
		newChan := make(chan string)
		go startCrc32(th+data, newChan)
		resultsChan = append(resultsChan, newChan)
	}
	var result string
	for _, resChan := range resultsChan {
		result += <-resChan
	}
	out <- result
}

func MultiHash(in, out chan interface{}) {
	var resultsChan []chan string
	for input := range in {
		data := input.(string)
		newChan := make(chan string)
		go startMultiHash(data, newChan)
		resultsChan = append(resultsChan, newChan)
	}
	for _, resChan := range resultsChan {
		out <- <-resChan
	}
}

func CombineResults(in, out chan interface{}) {
	var strs []string
	for input := range in {
		data := input.(string)
		strs = append(strs, data)
	}
	sort.Strings(strs)
	result := strings.Join(strs, "_")
	out <- result
}

func main() {

}
