const { username, balance, notifications, settings } = window.APP_DATA;

console.log(`User: ${username}, Balance: $${balance}`);

function checkBalance() {
    alert(`Hello ${username}, your current balance is $${balance}.`);
}

// List Handling
notification = JSON.parse(notifications);
console.log(notification);
notification.forEach(item => {
  console.log(item);
});

setting = JSON.parse(settings);
if (setting.theme === 'dark') {
    document.body.style.backgroundColor = "#2c3e50";
    document.body.style.color = "white";
}