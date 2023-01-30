const { openDB } = require('idb');
const dbPromise = openDB('image_db', 1, {
    upgrade(db) {
        db.createObjectStore('keyval');
    },
});

async function get(key) {
    return (await dbPromise).get('keyval', key);
}

async function set(key, val) {
    // return (await dbPromise).put('keyval', val, key);
    const transaction = (await dbPromise).transaction('keyval', 'readwrite');
    const store = transaction.objectStore('keyval');
    return store.put(val, key);
}

async function keys() {
    return (await dbPromise).getAllKeys('keyval');
}
async function getAll() {
    return (await dbPromise).getAll('keyval');

}

module.exports = { get, set, keys, getAll }