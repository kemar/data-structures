/*
A stack is a LIFO (Last-In First-Out) data structure:
an item added last will be removed first.

- push() appends an item to the end of the array.
- pop() removes and returns the last item in the array.

A stack can also be simulated by using unshift()/shift().
*/

let stack = []
stack.push(2)
stack.push(5)
let i = stack.pop()

console.log(i)

/*
A queue is a FIFO (First-In First-Out) data structure:
the first item added will be the first item removed.

- push() inserts the passed argument at the end of the array.
- shift() removes and returns the first item.

A queue can also be simulated by using unshift()/pop().

With aliases:

let queue = []
queue.add = queue.push
queue.remove = queue.shift
*/

let queue = []
queue.push(2)
queue.push(5)
let j = queue.shift()

console.log(j)
