let quicksort = (arr, lo=0, hi=null) => {

    if (hi === null) {
        hi = arr.length - 1;
    }

    // `lo < hi` means there is at least 2 elements.
    if (lo < hi) {
        // `p` is the position of the pivot in the array after partitioning.
        p = partition(arr, lo, hi);
        // Recursively sort the part that is "less than" pivot.
        quicksort(arr, lo, p - 1);
        // Recursively sort the part that is "greater than" pivot.
        quicksort(arr, p + 1, hi);
    }

    return arr;

}

let partition = (arr, lo, hi) => {

    // Lomuto algorithm: pick the last item as the pivot.
    let pivot_index = hi;

    // We want to find the position of the pivot in the array.
    // `l` keeps track of this position. Start at `lo`.
    let l = lo;

    // Iterate through the array from `lo` to `hi - 1` (`hi - 1` because the pivot is at `hi`).
    for (let i = lo; i < hi; i++) {
        if (arr[i] <= arr[pivot_index]) {
            // Put elements smaller than the pivot on the left.
            swap(arr, i, l);
            l = l + 1
        }
    }

    // Move the pivot at its correct position.
    swap(arr, l, pivot_index);
    return l;

}

let swap = (arr, left, right) => {
    tmp_left = arr[left];
    arr[left] = arr[right];
    arr[right] = tmp_left;
}


let a = [1,-2,-2,5,8,1254,654,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,7,5,-589.4,1,4,9,20,-2,-2,-2,-2,-2,-2];
let b = quicksort(a);
console.log(b.toString());
