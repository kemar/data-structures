let mergeSort = arr => {

    if (arr.length > 1) {

        let middle =  parseInt(arr.length / 2)
        let left = arr.slice(0, middle)
        let right = arr.slice(middle)

        mergeSort(left)
        mergeSort(right)

        let i = 0
        let j = 0
        let k = 0

        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                arr[k] = left[i]
                i = i + 1
            } else {
                arr[k] = right[j]
                j = j + 1
            }
            k = k + 1
        }

        while (i < left.length) {
            arr[k] = left[i]
            i = i + 1
            k = k + 1
        }

        while (j < right.length) {
            arr[k] = right[j]
            j = j + 1
            k = k + 1
        }

    }

    return arr

}

let a = [1,-2,-2,5,8,1254,654,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,7,5,-589.4,1,4,9,20,-2,-2,-2,-2,-2,-2]
// let a = [5,9,1,2,7,0]

let b = mergeSort(a)

console.log(b.toString())
