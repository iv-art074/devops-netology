##### Задача 1. Установите golang.
![Screenshot 2022-01-17 205833](https://user-images.githubusercontent.com/87374285/149757813-45e76d50-d8af-4685-9843-8ff2bd9c05bb.png)

##### Задача 3. Написание кода.

1. Программа для перевода метров в футы.
 ```
package main

import "fmt"

func main() {
	fmt.Print("Число в футах: ")
	var num_foot float64
	fmt.Scanf("%f", &num_foot)
	num_met := num_foot * float64(0.3048)
	fmt.Println("в метрах:", num_met)
}
```

2. Программа для поиска наименьшего элемента в любом заданном списке
x := []int{48,96,86,68,57,82,63,70,37,34,83,27,19,97,9,17,}
```
        package main
        
        import "fmt"
        
        func main() {
            x := []int{48,2, 96,86,3,68,57,82,63,70,37,34,83,27,19,97,9,17,1}
            mininimum := 0
            fmt.Println ("Список значений : ", x)
            for i, value := range x {
                if (i == 0) {
                   mininimum = value 
                } else {
                    if (value < mininimum){
                        mininimum = value
                    }
                }
            }
            fmt.Println("Минимальное число : ", mininimum)
        }    
```
![Снимок3](https://user-images.githubusercontent.com/87374285/149880499-4e94be53-d6d2-4280-b215-cf4257b7c00e.PNG)

3. Программа, которая выводит числа от 1 до 100, которые делятся на 3.
```
package main

import "fmt"

func main() {
	fmt.Printf("Числа, делящиеся на 3: \n 1й вариант \n")
	for i := 0; i < 99; {
		i = i + 3
		fmt.Printf("%v ", i)
	}
	fmt.Printf("\n 2й вариант \n")
	for i := 1; i <= 100; i++ {
		if (i % 3) == 0 {
			fmt.Print(i, " ")
		}
	}
}
```
![Снимок](https://user-images.githubusercontent.com/87374285/149880307-a1ee02f3-a7c0-4b96-9c44-dd481a1dc863.PNG)
