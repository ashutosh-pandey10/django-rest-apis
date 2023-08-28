# With this we have seen all of the CRUD operations using generic 
# APIViews of rest framework
import requests
product_id = input("What product id do you wish to delete?")

try:
    product_id = int(product_id)
except Exception:
    product_id = None
    print(f"{product_id} is invalid!")


if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint)

    print(get_response.status_code, get_response.status_code == 204)
