from robyn import Robyn, jsonify

app = Robyn(__file__)

@app.get("/")
async def home(request):
    return "Welcome to the API!"

@app.post("/data")
async def post_data(request):
    data = await request.json()
    # Process your data here
    return jsonify({"received": data})

@app.get("/query")
async def query_example(request, query_params):
    return jsonify(query_params.to_dict())

if __name__ == "__main__":
    app.start(port=8080, host="0.0.0.0")
