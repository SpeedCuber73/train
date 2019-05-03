package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"path"
)

func main() {
	out := os.Stdout
	if !(len(os.Args) == 2 || len(os.Args) == 3) {
		panic("usage go run main.go . [-f]")
	}
	dirPath := os.Args[1]
	printFiles := len(os.Args) == 3 && os.Args[2] == "-f"
	err := dirTree(out, dirPath, printFiles)
	if err != nil {
		panic(err.Error())
	}
}

func dirTree(out io.Writer, dirPath string, printFiles bool) error {
	var result string
	if printFiles {
		result = getTreeWithFiles(dirPath, "")
	} else {
		result = getTreeOnlyDirs(dirPath, "")
	}
	_, err := out.Write([]byte(result))
	if err != nil {
		return err
	}
	return nil
}

func getTreeWithFiles(dirPath string, prefix string) string {
	entities, err := ioutil.ReadDir(dirPath)
	if err != nil {
		panic("Can't read dir" + dirPath)
	}
	var result string
	countEntities := len(entities)
	lastIndex := countEntities - 1
	for i := 0; i < countEntities; i++ {
		if entities[i].IsDir() {
			pathToNewDir := path.Join(dirPath, entities[i].Name())
			var prefixToDir string
			if i == lastIndex {
				result += representLastEntity(entities[i], prefix)
				prefixToDir = prefix + "\t"
			} else {
				result += representEntity(entities[i], prefix)
				prefixToDir = prefix + "│\t"
			}
			result += getTreeWithFiles(pathToNewDir, prefixToDir)
		} else {
			if i == lastIndex {
				result += representLastEntity(entities[i], prefix)
			} else {
				result += representEntity(entities[i], prefix)
			}
		}
	}
	return result
}

func getTreeOnlyDirs(dirPath string, prefix string) string {
	entities, err := ioutil.ReadDir(dirPath)
	if err != nil {
		panic("Can't read dir" + dirPath)
	}
	var dirs []os.FileInfo
	for _, entity := range entities {
		if entity.IsDir() {
			dirs = append(dirs, entity)
		}
	}
	var result string
	countDirs := len(dirs)
	lastIndex := countDirs - 1
	for i, dir := range dirs {
		var prefixToDir string
		pathToNewDir := path.Join(dirPath, dir.Name())
		if i == lastIndex {
			result += representLastEntity(dir, prefix)
			prefixToDir = prefix + "\t"
		} else {
			result += representEntity(dir, prefix)
			prefixToDir = prefix + "│\t"
		}
		result += getTreeOnlyDirs(pathToNewDir, prefixToDir)
	}
	return result
}

func representEntity(file os.FileInfo, prefix string) string {
	return fmt.Sprintf("%s├───%s\n", prefix, getInfoEntity(file))
}

func representLastEntity(file os.FileInfo, prefix string) string {
	return fmt.Sprintf("%s└───%s\n", prefix, getInfoEntity(file))
}

func getInfoEntity(file os.FileInfo) string {
	if file.IsDir() {
		return file.Name()
	}
	if file.Size() == 0 {
		return fmt.Sprintf("%s (empty)", file.Name())
	}
	return fmt.Sprintf("%s (%db)", file.Name(), file.Size())
}
