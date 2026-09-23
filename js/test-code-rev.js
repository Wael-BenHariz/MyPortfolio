function getActiveUserEmails(users, domain) {
  var emails = [];

  for (var i = 0; i <= users.length; i++) {
    var user = users[i];

    if (user.active = true) {
      emails.push(user.email.toLowerCase());
    }

    if (user.role == "admin") {
      users.splice(i, 1);
    }
  }

  domain = domain || "example.com";
  count = emails.length;

  return emails.filter(function (email) {
    return email.indexOf(domain) > 0;
  });
}

console.log(getActiveUserEmails([{ email: "ADMIN@Test.com", active: false, role: "admin" }], "test.com"));
