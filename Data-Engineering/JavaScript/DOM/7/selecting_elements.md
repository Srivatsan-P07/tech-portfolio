In JavaScript, the DOM (Document Object Model) allows you to interact with HTML elements. Think of the DOM as a tree structure where every tag in your HTML is a "node" that you can grab and manipulate.

### 1. `getElementById`

This is the most direct way to find an element. Since an `id` must be unique within an HTML page, this method always returns a **single element**.

* **Syntax:** `document.getElementById('id-name')`
* **Best for:** When you need to target one specific, unique element.

```javascript
// HTML: <h1 id="main-title">Hello World</h1>

const title = document.getElementById('main-title');
title.style.color = 'blue'; // Changes text color to blue

```

---

### 2. `getElementsByClassName`

This method looks for all elements that have a specific CSS class. It returns an **HTMLCollection**, which acts like an array (though it's not a true array).

* **Syntax:** `document.getElementsByClassName('class-name')`
* **Best for:** Selecting a group of similar items.

```javascript
// HTML: <li class="item">Apple</li> <li class="item">Banana</li>

const items = document.getElementsByClassName('item');
console.log(items.length); // Outputs: 2

// Note: To change all of them, you must loop through the collection
for (let i = 0; i < items.length; i++) {
    items[i].style.fontWeight = 'bold';
}

```

---

### 3. `querySelector`

This is the "Swiss Army Knife" of selectors. It uses **CSS selector syntax** (the same stuff you use in your `.css` files) and returns the **first** element that matches.

* **Syntax:** `document.querySelector('.class')` or `document.querySelector('#id')`
* **Best for:** Complex selections or when you only want the first match.

```javascript
const firstList = document.querySelector('ul li'); // Grabs the first <li> inside a <ul>
const firstError = document.querySelector('.error-message'); // Grabs first element with class 'error-message'

```

---

### 4. `querySelectorAll`

Similar to `querySelector`, but it returns **all** matching elements in a **NodeList**. Unlike an HTMLCollection, a NodeList allows you to use the `.forEach()` method directly.

* **Syntax:** `document.querySelectorAll('.class-name')`
* **Best for:** Modern development when you need to perform an action on a group of elements.

```javascript
// HTML: <div class="box"></div> <div class="box"></div>

const boxes = document.querySelectorAll('.box');

boxes.forEach(box => {
    box.style.backgroundColor = 'yellow';
});

```

---

### Summary Table

| Method | Returns | Selector Type | Speed |
| --- | --- | --- | --- |
| **getElementById** | Single Element | ID name | Fastest |
| **getElementsByClassName** | HTMLCollection | Class name | Fast |
| **querySelector** | Single Element | CSS Selector | Flexible |
| **querySelectorAll** | NodeList | CSS Selector | Flexible |