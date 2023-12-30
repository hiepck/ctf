const fs             = require('fs');
const express        = require('express');
const router         = express.Router();
const JWTHelper      = require('../helpers/JWTHelper');
const MDHelper       = require('../helpers/MDHelper');
const AuthMiddleware = require('../middleware/AuthMiddleware');
const { v4: uuidv4 } = require('uuid')
const { execSync }   = require('child_process');

let db;

const response = data => ({ message: data });

const uuidPattern = /^[0-9A-F]{8}-[0-9A-F]{4}-[4][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$/i;

router.get('/', (req, res) => {
    return res.render('login.html');
});

router.post('/api/register', async (req, res) => {
    const { username, password } = req.body;

    if (username && password) {
        return db.getUser(username)
            .then(user => {
                if (user.length) return res.status(401).send(response('User already registered!'));

                return db.registerUser(username, password)
                    .then(()  => res.send(response('User registered successfully!')))
            })
            .catch(() => res.send(response('Something went wrong!')));
    }

    return res.status(401).send(response('Please fill out all the required fields!'));
});

router.post('/api/login', async (req, res) => {
    const { username, password } = req.body;
    if (username && password) {
        return db.loginUser(username, password)
            .then(user => {
                if (!user.length) return res.status(403).send(response('Invalid username or password!'));

                JWTHelper.sign({ username: user[0].username })
                    .then(token => {
                        res.cookie('session', token, { maxAge: 43200000 });
                        res.send(response('User authenticated successfully!'));
                    })
            })
            .catch(e => {
                res.send(response('Something went wrong!'));
            });
    }

    return res.status(500).send(response('Missing parameters!'));
});

router.get('/admin', AuthMiddleware, async (req, res) => {
    if (req.user.username !== 'admin') return res.redirect('/dashboard');

    let flag = execSync('/readflag').toString();

    return res.render('admin.html', { flag });
});

router.get('/dashboard', AuthMiddleware, async (req, res) => {
    if (req.user.username == 'admin') return res.redirect('/admin');

    return db.listInvoice(req.user.username)
        .then(invoices => {
            return res.render('dashboard.html', {user: req.user, invoices});
        })
        .catch(e => {
            res.send(response('Something went wrong!'));
        });
});

router.get('/invoice/markdown/:invoice', AuthMiddleware, (req, res) => {
    const { invoice } = req.params;

    try {
        mdContent = fs.readFileSync(`/app/static/user_files/markdown/${invoice}`).toString();

        return res.json({content: mdContent});
    }
    catch (e) {
        res.send(response('Invoice not found!'));
    }
});

router.post('/api/invoice/add', AuthMiddleware, async (req, res) => {
    const { markdown_content } = req.body;

    if (markdown_content) {
        let invoice = uuidv4();

        return MDHelper.makePDF(markdown_content, invoice)
            .then(() => {
                db.addInvoice(req.user.username, invoice)
					.then(() => {
						res.send(response('Invoice saved successfully!'));
					})
					.catch(e => {
						res.send(response('Something went wrong!'));
					})
            })
            .catch(() => {
                res.send(response('Something went wrong!'));
            })
    }

    return res.status(401).send(response('Missing required parameters!'));
});


router.post('/api/invoice/update', AuthMiddleware, async (req, res) => {
    const { markdown_content, invoice } = req.body;

    if (!uuidPattern.test(invoice)) return res.status(401).send(response('Missing required parameters!'));

    if (markdown_content) {
        return MDHelper.makePDF(markdown_content, invoice)
            .then(() => {
                res.send(response('Invoice saved successfully!'));
            })
            .catch(() => {
                res.send(response('Something went wrong!'));
            })
    }

    return res.status(401).send(response('Missing required parameters!'));
});

router.post('/api/invoice/delete', AuthMiddleware, async (req, res) => {
	const { invoice } = req.body;

	if (invoice) {
		return db.deleteInvoice(req.user.username, invoice)
		.then(() => {
			res.send(response('Invoice removed successfully!'))
		})
		.catch(e => {
			res.send(response('Something went wrong!'));
		})
	}

	return res.status(401).send(response('Missing required parameters!'));
});

router.get('/logout', (req, res) => {
    res.clearCookie('session');
    return res.redirect('/');
});

module.exports = database => {
    db = database;
    return router;
};