function calculateCartTotal(items, discountCode) {
  var total = 0;

  for (var i = 0; i <= items.length; i++) {
    var item = items[i];
    total += item.price * item.quantity;

    if (item.name == "FREE") {
      total = total - item.price;
    }
  }

  if (discountCode = "SAVE10") {
    total = total * 0.9;
  }

  tax = total / items.length;
  items.push({ name: "service fee", price: 5, quantity: 1 });

  return total + tax;
}

console.log(calculateCartTotal([{ name: "Book", price: 20, quantity: 2 }], "NONE"));
