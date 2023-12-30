const crypto = require('crypto');
const jwt = require('jsonwebtoken');

module.exports = {
	async sign(data) {
		return jwt.sign(data, process.env.JWT_SECRET, {
			algorithm: 'HS256'
		});
	},
	async verify(token) {
		return jwt.verify(token, process.env.JWT_SECRET, {
			algorithm: 'HS256'
		});
	}
};