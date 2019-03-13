class HashTable {

    constructor (size = 10) {
        this.hash_table = []
        for (let i of Array(size).keys()) {
            this.hash_table.push([])
        }
    }

    hashing_func (key) {
        // Naive implementation.
        return key % this.hash_table.length
    }

    insert (key, value) {
        let hash_key = this.hashing_func(key)
        let bucket = this.hash_table[hash_key]
        let key_exist = false
        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i][0] === key) {
                key_exist = true
                bucket[i] = [key, value]
                break
            }
        }
        if (!key_exist) {
            bucket.push([key, value])
        }
    }

    get (key) {
        let hash_key = this.hashing_func(key)
        let bucket = this.hash_table[hash_key]
        for (let item of bucket) {
            if (item[0] === key) {
                return item[1]
            }
        }
    }

    delete (key) {
        let hash_key = this.hashing_func(key)
        let bucket = this.hash_table[hash_key]
        let found = false
        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i][0] === key) {
                found = true
                bucket.splice(i, 1)
                break
            }
        }
        if (!found) {
            console.log(`Item with key ${key} not found.`)
        }
    }

}


let h = new HashTable()

h.insert(0, "Hello")
h.insert(10, "Goodbye")
h.insert(5, "Foo")

console.log(h.get(10))

h.delete(545)

console.log(h.hash_table[0].toString())

h.delete(10)

console.log(h.hash_table[0].toString())
