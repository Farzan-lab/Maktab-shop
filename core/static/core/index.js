//selectors
const addCartButtons = document.querySelectorAll(".add-cart");
const cart = document.querySelector("#cart-list");



//global variables
let cartItems = [];


const removeFromCart = (e) => {
    e.preventDefault();
    const index = cartItems.indexOf(e.target.id);
    if (index > -1) {
        cartItems.splice(index, 1);
        addCartButtons.forEach(element => {
            if (element.id == e.target.id){
                element.disabled = false;
                element.innerHTML = "Add To Cart"
            }
            
        })
        
    }
    updateCart()
}

//functions
const updateCart = () => {
    cart.innerHTML = ""
    cartItems.forEach(id => {
        let element = document.querySelector(`#cart-${id}`).cloneNode(true)
        element.classList.remove('d-none')
        cart.appendChild(element)
    })
    if (!cartItems.length){
        cart.innerHTML = "<div class='text-center'>No items in your cart!</div>"
    }else{
        cart.innerHTML = cart.innerHTML + `
        <div class="mt-3">
            <lable for="discount">Discount Code</lable>
            <input name="discount" class="form-control" type="text" id="discount">
        </div>
        <div class="mt-3">Addres Info:</div>
        <div class="row px-1 mb-3">

            <div class="col-6">
                <lable for="province">Province</lable>
                <input name="province" class="form-control" type="text" id="province">
            </div>
            <div class="col-6">
                <lable for="city">City</lable>
                <input name="city" class="form-control" type="text" id="city">
            </div> 
            <div class="col-12">
                <lable for="detail">Complete Address</lable>
                <input name="detail" class="form-control" type="text" id="detail">
            </div> 
        </div>
        <div>
            <button type="submit" class="btn btn-primary">Order</button>
        </div>
        `
    }
}

const addToCart = (e) => {
    if (!cartItems.includes(e.target.id)){
        cartItems.push(e.target.id)
        e.target.disabled = true;
        e.target.innerHTML = "Added To Cart"
        updateCart()
    }
}

//listeners
addCartButtons.forEach(element => {
    element.addEventListener('click', addToCart)
});

updateCart()

