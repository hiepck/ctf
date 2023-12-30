function verifyRole(role) {
    if (role.charCodeAt(0) != 64) {
        return false;
    }
    if ((role.charCodeAt(1) + role.charCodeAt(2) != 209) && (role.charCodeAt(2) - role.charCodeAt(1) != 9)) {
        return false
    }
    if ((role.charCodeAt(3).toString() + role.charCodeAt(4).toString() != "10578") && (role.charCodeAt(3) - role.charCodeAt(4) != 27)) {
        return false
    }
    return true
}

/*
role[0] = 64
role[1] = 100
role[2] = 109
role[3] = 105
role[4] = 78
*/