/*
A stack uses LIFO (last-in first-out) ordering.

Operations:

- push(item) Add an item to the top of the stack
- pop() Remove the top item from the stack
- peek() Return the top of the stack
- isEmpty() Return true if the stack is empty
*/

class Stack extends Array {

    // Default pop(): remove the top item from the stack.
    // Default push(item): add an item to the top of the stack.

    peek () {
        let top = this[this.length - 1]
        console.log(top)
        return top
    }

    isEmpty () {
        return this.length === 0
    }

}

let s = new Stack()

console.log(s.isEmpty())

s.push(2)
s.push(5)
s.peek()

console.log(s.isEmpty())

console.log(s.length)
