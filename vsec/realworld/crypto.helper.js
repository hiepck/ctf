const nodeForge = require('node-forge');
const fs = require('fs')

const defaultPrivateKey = fs.readFileSync('./key/private.pem')

function decryptAESRequest(e) {
    let arr = e.split("@@@@@@")
    const privateKey = nodeForge.pki.privateKeyFromPem(defaultPrivateKey);
    var keyAES = nodeForge.util.decodeUtf8(privateKey.decrypt(nodeForge.util.decode64(arr[0])));
    var data = Buffer.from(arr[1], 'base64');
    var decipher = nodeForge.cipher.createDecipher('AES-ECB', Buffer.from(keyAES, 'base64').toString('binary'));
    decipher.start();
    decipher.update(nodeForge.util.createBuffer(data));
    decipher.finish();
    return nodeForge.util.decodeUtf8(decipher.output.data);
}

function encryptAESResponse(e, publicKey) {
    const key = nodeForge.random.getBytesSync(32);
    var cipher = nodeForge.cipher.createCipher('AES-ECB', key);
    cipher.start();
    cipher.update(nodeForge.util.createBuffer(JSON.stringify(e), 'utf8'));
    cipher.finish();
    const res = Buffer.from(cipher.output.data, 'binary');
    encKey = nodeForge.pki.publicKeyFromPem(publicKey).encrypt(nodeForge.util.encode64(key))
    return (nodeForge.util.encode64(encKey) + res.toString('base64'));
}

module.exports = {
    encryptResponse: encryptAESResponse,
    decryptRequest: decryptAESRequest

}
