// Write code to remove duplicates from an unsorted linked list.

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

    removeDups () {
        if (!this.head) return null
        let seen = new Set()
        let prevNode = null
        let node = this.head
        while (node) {
            if (seen.has(node.cargo)) {
                prevNode.next = node.next
                this.size -= 1
            } else {
                seen.add(node.cargo)
                prevNode = node
            }
            node = node.next
        }

        console.log('removeDups')
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

l.add('5')
l.add('1')
l.add('2')
l.add('2')
l.add('3')
l.add('3')
l.add('3')
l.add('3')
l.add('3')
l.add('3')
l.add('3')
l.add('3')
l.add('3')
l.add('3')
l.add('4')
l.add('2')
l.add('5')
l.add('6')
l.add('6')
l.add('6')
l.add('6')

l.dump()

l.removeDups()

l.print()

l.dump()
