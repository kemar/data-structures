// Write code to add, search and remove items from an unsorted linked list.

class LinkedList {

    constructor () {
        this.head = null
        this.size = 0
    }

    dump () {
        console.log(`Head is ${this.head.cargo}, size is ${this.size}`)
    }

    add (cargo) {
        let node = new Node(cargo, this.head)
        this.head = node
        this.size += 1
        return this.head
    }

    search (cargo) {

        if (!this.head) return null

        let node = this.head

        while (node) {
            if (node.cargo === cargo) {
                console.log(`Found ${cargo}`)
                return node
            }
            node = node.next
        }

        return `node with cargo ${v} not found`

    }

    delete (cargo) {

        if (!this.head) return null

        let node = this.head

        if (node.cargo === cargo) {
            this.head = node.next
            this.size -= 1
            console.log(`Deleted ${cargo}`)
            return
        }

        while (node.next) {
            if (node.next.cargo === cargo) {
                node.next = node.next.next
                this.size -= 1
                console.log(`Deleted ${cargo}`)
                return
            }
            node = node.next
        }

    }

    print () {
        console.log(`---------- printing`)
        if (this.head) {
            this.head.print()
        }
    }

}

class Node {

    constructor (cargo, next) {
        this.cargo = cargo
        this.next = next
    }

    print () {
        console.log(this.cargo)
        if (this.next) {
            this.next.print()
        }
    }

}

let l = new LinkedList()

l.add('1')
l.add('2')
l.add('3')
l.add('4')
l.add('5')
l.add('6')

l.dump()

l.print()

l.search('2')

l.delete('2')

l.print()
