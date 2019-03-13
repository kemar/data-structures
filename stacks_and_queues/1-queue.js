/*
A queue uses FIFO (first-in first-out) ordering.

Operations:

- add(item) Add an item to the end of the queue
- remove() Remove the first item from the queue
- peek() Return the top of the queue
- isEmpty() Return true if the queue is empty
*/

class Queue extends Array {

    add (item) {
        this.push(item)
    }

    remove () {
        // Slow because all of the other elements have to be shifted by one.
        this.shift()
    }

    peek () {
        let top = this[this.length - 1]
        console.log(top)
        return top
    }

    isEmpty () {
        return this.length === 0
    }

}

let q = new Queue()

console.log(q.isEmpty())

q.add(2)
q.add(5)
q.peek()

console.log(q.isEmpty())

console.log(q.length)
