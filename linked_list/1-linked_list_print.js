// Write code to print a linked list forward and backward.

class LinkedList {

    constructor () {
        this.length = 0
        this.head = null
    }

    dumpHead () {
        console.log(`Head = ${this.head.cargo}`)
    }

    add (cargo) {
        let next = this.head
        this.head = new Node(cargo, next)
        this.length += 1
    }

    print () {
        console.log(`------------------print`)
        if (this.head) {
            this.head.print()
        }
    }

    printBack () {
        console.log(`------------------printBack`)
        if (this.head) {
            this.head.printBack()
        }
    }

}

class Node {

    constructor (cargo, next = null) {
        this.cargo = cargo
        this.next = next
    }

    print () {
        console.log(this.cargo)
        if (this.next) {
            this.next.print()
        }
    }

    printBack () {
        if (this.next) {
            this.next.printBack()
        }
        console.log(this.cargo)
    }

}

let list = new LinkedList()

list.add('Arivederci')
list.add('Flutchen krugen')
list.add('Guten morge')
list.add('Konnichonwa')
list.add('Hello')

list.dumpHead()

list.print()

list.printBack()
