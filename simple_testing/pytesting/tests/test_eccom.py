from app.ecommerce import ShoppingCart
import pytest

@pytest.fixture
def cart():
    return ShoppingCart()


def test_add_item(cart):
    
    cart.add_item("ipad",2)
    assert cart.get_item_count("ipad")==2
    assert cart.get_total_items() == 2
    
def test_remove_item(cart):
   
    cart.add_item("samsung",3)
    cart.remove_item("samsung",2)
    assert cart.get_item_count("samsung")==1
    assert cart.get_total_items() == 1
    
def test_get_cart_items(cart):
   
    cart.add_item("mango",3)
    cart.add_item("pineapple",2)
    items = cart.get_cart_items()
    assert "mango" in items
    assert "pineapple" in items
    
def test_clear_item(cart):
  
    cart.add_item("hp laptop",3)
    cart.clear_cart()
    assert cart.get_total_items() == 0
    assert cart.get_cart_items() == []
    

