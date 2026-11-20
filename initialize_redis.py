import redis

products = [
    {
        "id" : "0",
        "name" : "Bread",
        "price" : 3,
        "description" : "A loaf of bread",
        "stock" : 100
    },
    {
        "id" : "1",
        "name" : "Apple",
        "price" : 2,
        "description" : "Red, round fruit",
        "stock" : 120
    },
    {
        "id" : "2",
        "name" : "Orange",
        "price" : 4,
        "description" : "Quite juicy",
        "stock" : 80
    },
    {
        "id" : "3",
        "name" : "Chicken",
        "price" : 8,
        "description" : "Whole chicken, uncooked",
        "stock" : 50
    },
    {
        "id" : "4",
        "name" : "Hamburger",
        "price" : 5,
        "description" : "A puck of minced meat",
        "stock" : 60
    },
    {
        "id" : "5",
        "name" : "Fish",
        "price" : 10,
        "description" : "Straight from the sea",
        "stock" : 40
    },
    {
        "id" : "6",
        "name" : "Lettuce",
        "price" : 4,
        "description" : "Vegetable, green",
        "stock" : 70
    },
    {
        "id" : "7",
        "name" : "Soup",
        "price" : 5,
        "description" : "Broth, a whole liter of it",
        "stock" : 100
    },
    {
        "id" : "8",
        "name" : "Eggs",
        "price" : 6,
        "description" : "Chicken-made",
        "stock" : 60
    },
    {
        "id" : "9",
        "name" : "Coffee",
        "price" : 4,
        "description" : "Brown energy powder",
        "stock" : 100
    }
]

def initialize_products(redis_client):
    for i in range(10):
        for key in products[i].keys():
            redis_client.hset(f"product:{i}", key, products[i][key])

if __name__ == "__main__":
    try:
        #TODO: Configura la conexión a Redis 
        #redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)

        # Inicializa los productos en Redis
        initialize_products(redis_client)
        print("¡Productos inicializados en Redis!")

    except Exception as e:
        print(f"Error al conectarse a Redis: {e}")
