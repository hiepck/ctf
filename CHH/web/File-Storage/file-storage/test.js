var file = {}
function isObject(obj) {
     return obj !== null && typeof obj === "object";
}
function setValue(obj, key, value) {
     const keylist = key.split(".");
     const e = keylist.shift();
     if (keylist.length > 0) {
          if (!isObject(obj[e])) obj[e] = {};
          setValue(obj[e], keylist.join("."), value);
     } else {
          obj[key] = value;
          console.log(obj)
     }
}

setValue(file, '__proto__', 'a');