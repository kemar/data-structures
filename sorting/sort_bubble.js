/*

Bubble Sort

A bubble sort takes an unsorted list and keeps comparing each element with its right side neighbour in order to sort the data. Whichever element is smaller gets shifted to the left. After completion of one round, the largest number ends up in its correct position. In other words, the largest number bubbles to the top. Then, the process is repeated again and again until all of the data is sorted.

1. For the first iteration, compare all the elements (n). For the subsequent runs, compare (n-1) (n-2) and so on
2. Compare each element with its right side neighbour
3. Swap the smallest element to the left
4. Keep repeating steps 1-3 until the whole list is covered

This algorithm is of O(n^2).

*/

let bubblesort = arr => {
    for (let i of [...Array(arr.length).keys()].reverse()) {
        for (let j of Array(i).keys()) {
            if (arr[j] > arr[j + 1]) {
                let tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
            }
        }
    }
    return arr
}

let bubblesort2 = arr => {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length - i; j++) {
            if (arr[j] > arr[j + 1]) {
                let tmp_left = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp_left
            }
        }
    }
    return arr;
}

let a = [1,-2,-2,5,8,1254,654,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,7,5,-589.4,1,4,9,20,-2,-2,-2,-2,-2,-2]

let b = bubblesort(a)
console.log(b.toString())

let c = [1,-2,-2,5,8,1254,654,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,7,5,-589.4,1,4,9,20,-2,-2,-2,-2,-2,-2]

let d = bubblesort2(c)
console.log(d.toString())
