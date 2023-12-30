let mysql = require('mysql')

class Database {

    constructor() {
        this.connection = mysql.createConnection({
            host: '127.0.0.1',
            user: 'dinvoice',
            password: 'dinvoice',
            database: 'dinvoice'
        });
    }

    async connect() {
        return new Promise((resolve, reject)=> {
            this.connection.connect((err)=> {
                if(err)
                    reject(err);
                resolve();
            });
        })
    }

    async registerUser(username, password) {
        return new Promise(async (resolve, reject) => {
            let stmt = `INSERT INTO users(username, password) VALUES(?, ?)`;
            this.connection.query(
                stmt,
                [
                    String(username),
                    String(password)
                ],
                (err, _) => {
                    if(err)
                        reject(err);
                    resolve();
                }
            )
        });
    }

    async loginUser(username, password) {
        return new Promise(async (resolve, reject) => {
            let stmt = `SELECT * FROM users WHERE username = ? and password = ?`;
            this.connection.query(
                stmt,
                [
                    String(username),
                    String(password)
                ],
                (err, result) => {
                    if(err)
                        reject(err);
                    try {
                        resolve(JSON.parse(JSON.stringify(result)));
                    }
                    catch (e) {
                        reject(e);
                    }
                }
            )
        });
    }

    async getUser(username) {
        return new Promise(async (resolve, reject) => {
            let stmt = `SELECT * FROM users WHERE username = ?`;
            this.connection.query(
                stmt,
                [
                    String(username)
                ],
                (err, result) => {
                    if(err)
                        reject(err);
                    try {
                        resolve(JSON.parse(JSON.stringify(result)));
                    }
                    catch (e) {
                        reject(e);
                    }
            })
        });
    }

    async listInvoice(username) {
        return new Promise(async (resolve, reject) => {
            let stmt = 'SELECT * FROM invoices where username = ?';
            this.connection.query(
                stmt,
                [
                    String(username)
                ],
                (err, result) => {
                    if(err)
                        reject(err);
                    try {
                        resolve(JSON.parse(JSON.stringify(result)));
                    }
                    catch (e) {
                        reject(e);
                    }
            })

        });
    }

    async addInvoice(username, invoice) {
        return new Promise(async (resolve, reject) => {
            let stmt = 'INSERT INTO invoices (username, invoice) VALUES(?, ?)';
            this.connection.query(
                stmt,
                [
                    String(username),
                    String(invoice)
                ],
                (err, _) => {
                    if(err)
                        reject(err);
                    try {
                        resolve();
                    }
                    catch (e) {
                        reject(e);
                    }
            })

        });
    }

    async deleteInvoice(username, invoice) {
        return new Promise(async (resolve, reject) => {
            let stmt = 'DELETE FROM invoices WHERE username = ? and invoice = ?';
            this.connection.query(
                stmt,
                [
                    String(username),
                    String(invoice)
                ],
                (err, _) => {
                    if(err)
                        reject(err);
                    try {
                        resolve();
                    }
                    catch (e) {
                        reject(e);
                    }
            })

        });
    }

}

module.exports = Database;