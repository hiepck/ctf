const express = require("express");
const crypto = require("node:crypto");
const { spawnSync } = require("child_process");

const app = express();

app.post("/create-user", (req, res) => {
  const username = crypto.randomBytes(8).toString("hex");
  const password = crypto.randomBytes(8).toString("hex");

  const adduser = spawnSync("adduser", ["-D", username]);
  if (adduser.error || adduser.status !== 0) {
    res.status(409).send({ error: "Failed to create user" });
    return;
  }

  const changepwd = spawnSync("chpasswd", {
    input: `${username}:${password}`,
  });
  if (changepwd.error || changepwd.status !== 0) {
    res.status(409).send({ error: "Failed to create user" });
    return;
  }

  res.send({ username, password });
});

app.post("/flag", (req, res) => {
  if (!!req.headers["x-get-flag"]) {
    res.send(process.env.FLAG || "ptm{REDACTED}");
  } else {
    req.send("nope");
  }
});

app.get("*", (req, res) => {
  res.send("404 not found");
});

app.listen(3000, () => {
  console.log(`App listening on port 3000`);
});
