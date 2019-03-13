class LinkedList {

    constructor () {
        this.length = 0
        this.head = null
    }

    add (cargo) {
        let next = this.head
        this.head = new Node(cargo, next)
        this.length += 1
    }

}

class Node {

    constructor (cargo, next = null) {
        this.cargo = cargo
        this.next = next
    }

}

let list = new LinkedList()

list.add('Arivederci')
list.add('Flutchen krugen')
list.add('Guten morge')
list.add('Konnichonwa')
list.add('Hello')

console.log(list.head.cargo)
